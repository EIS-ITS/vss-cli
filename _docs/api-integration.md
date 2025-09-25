# VSS CLI API Integration

## Overview

VSS CLI integrates with the ITS Private Cloud API through the `pyvss` library, extending `VssManager` for CLI-specific functionality.

## API Architecture

### Base Integration
```python
class Configuration(VssManager):
    def __init__(self, tk: str = ''):
        super().__init__(tk)
        # CLI-specific extensions
        self.user_agent = self._default_user_agent()
        self.verbose = False
        self.output = "auto"
        # ... CLI settings
```

### Endpoint Management
```python
# Multiple endpoint support
DEFAULT_ENDPOINT = "https://cloud-api.eis.utoronto.ca"
self.api_endpoint = f'{endpoint}/v2'
self.token_endpoint = f'{endpoint}/auth/request-token'
```

## Authentication System

### Token-Based Authentication
```python
# JWT token workflow
def get_token(self, user, password, otp=None):
    """Generate JWT token from credentials."""
    self.api_token = super().get_token(user, password, otp)
    return self.api_token
```

### Multi-Factor Authentication Support
```python
# MFA challenge handling
def _get_token_with_mfa(self, token=None, spinner_cls=None):
    try:
        token = self.get_token(username, password, totp)
    except VssError as ex:
        if 'InvalidParameterValue: otp' in ex.message:
            # Request TOTP from user
            self.totp = click.prompt('MFA enabled. Provide TOTP')
            token = self.get_token(username, password, self.totp)
```

### Configuration Management
```yaml
# ~/.vss-cli/config.yaml
endpoints:
  - name: "cloud-api"
    url: "https://cloud-api.eis.utoronto.ca"
    auth: "base64_encoded_credentials"  # username:password
    token: "jwt_token"
    tf_enabled: true  # MFA enabled
```

## API Request Patterns

### Synchronous Operations
```python
# Direct API calls
vms = ctx.get_vms(filter='folder.path=prod')
vm_details = ctx.get_vm(vm_id)
networks = ctx.get_networks(show_all=True)
```

### Asynchronous Operations
```python
# Request-based operations
result = ctx.create_vm_from_template(
    source='template-id',
    name='new-vm',
    folder='vm-folder'
)

# Monitor request completion
if ctx.wait_for_requests:
    ctx.wait_for_request_to(result,
                           required=['PROCESSED', 'SCHEDULED'])
```

### Bulk Operations
```python
# Multiple parallel requests
def wait_for_requests_to(self, objs, required=['PROCESSED']):
    wq = WorkerQueue(max_workers=len(objs))

    with wq.join(debug=self.debug):
        for obj in objs:
            wq.put(functools.partial(
                self.wait_for_request_to,
                obj=obj,
                required=required
            ))
            wq.spawn_worker()
```

## Data Processing

### Smart Resource Resolution
```python
def get_vm_by_id_or_name(self, vm_id, silent=False, instance_type='vm'):
    """Resolve VM by moref, UUID, or name."""
    is_moref = validate_vm_moref('', '', vm_id)
    is_uuid = validate_uuid('', '', vm_id)

    if is_moref or is_uuid:
        # Direct lookup by ID
        attr = 'moref' if is_moref else 'uuid'
        filters = f'{attr},eq,{vm_id}'
        return lookup_f(filter=filters)
    else:
        # Search by name with interactive selection
        vms = lookup_f(per_page=3000)
        matches = [vm for vm in vms
                  if vm_id.lower() in vm['name'].lower()]

        if len(matches) > 1:
            return self.pick(matches)  # Interactive selection
        return matches
```

### Filter Processing
```python
# API filter expressions
vms = ctx.get_vms(filter='status,eq,POWERED_ON')
templates = ctx.get_templates(filter='folder.path,like,/templates/')
requests = ctx.get_requests(filter='status,in,PENDING,IN_PROGRESS')
```

### Pagination Handling
```python
# Large dataset retrieval
all_vms = ctx.get_vms(
    per_page=3000,     # Large page size
    show_all=True      # Bypass pagination limits
)
```

## Request Management

### Request Status Monitoring
```python
def wait_for_request_to(self, obj, required=['PROCESSED'],
                       wait=5, max_tries=720):
    """Monitor request until completion."""
    request_id = obj["request"]["id"]

    while tries < max_tries:
        request = self.request(obj['_links']['request'])
        status = request['data']['status']

        if status in required:
            return True
        elif status in ['ERROR', 'CANCELLED']:
            return False

        sleep(wait)
        tries += 1
```

### Request Types
- **VM Operations**: Create, modify, delete
- **Storage Operations**: Disk expansion, snapshot management
- **Network Operations**: NIC configuration, network assignment
- **Infrastructure**: Folder operations, inventory requests

## API Error Handling

### Exception Hierarchy
```python
try:
    result = ctx.api_operation()
except VssError as ex:
    # API-specific errors
    if ex.http_code == 404:
        raise VssCliError(f"Resource not found: {resource_id}")
    elif ex.http_code == 403:
        raise VssCliError("Permission denied")
    else:
        raise VssCliError(f"API error: {ex.message}")
except Exception as ex:
    raise VssCliError(f"Unexpected error: {ex}")
```

### HTTP Status Handling
- **200-299**: Success responses
- **400**: Bad request (validation errors)
- **401**: Authentication required
- **403**: Authorization denied
- **404**: Resource not found
- **500+**: Server errors

## Performance Optimization

### Connection Management
```python
# Persistent session
self.session = requests.Session()
self.session.headers.update({
    'User-Agent': self.user_agent,
    'Authorization': f'Bearer {self.api_token}'
})
```

### Request Batching
```python
# Batch multiple operations
operations = [
    ('vm1', 'power-on'),
    ('vm2', 'power-on'),
    ('vm3', 'power-off')
]

results = []
for vm_id, operation in operations:
    result = ctx.set_vm_power_state(vm_id, operation)
    results.append(result)

# Wait for all operations
ctx.wait_for_requests_to(results)
```

### Caching Strategy
- **Token Caching**: In-memory for session duration
- **Config Caching**: File-based with mtime check
- **No Response Caching**: Real-time data requirements

## API Response Processing

### Column Extraction
```python
# JSONPath for nested data
COLUMNS_VM = [
    ("name",),                      # Direct field
    ("folder.path",),               # Nested field
    ("hardware.cpu.cpu_count", "cpu"),  # Alias
    ("storage.provisioned_gb",)     # Deep nesting
]
```

### Data Transformation
```python
def format_output(ctx, data, columns, single=False):
    """Transform API response to formatted output."""
    # Extract columns using JSONPath
    # Apply formatting based on output type
    # Return formatted string
```

## Integration with External Services

### Storage Integration (vskey-stor)
```python
def get_vskey_stor(self, **kwargs):
    """Initialize MinIO client for storage operations."""
    from minio import Minio

    super().get_vskey_stor(
        user=self.username,
        password=self.password,
        s3_endpoint=self.s3_server
    )
```

### VPN Integration
```python
def enable_vss_vpn(self, **kwargs):
    """Enable VPN for secure access."""
    self.init_vss_vpn(self.vpn_server)
    return super().enable_vss_vpn(
        user=self.username,
        password=self.password,
        otp=self.totp
    )
```

### AI Assistant Integration (UTORcloudy)

#### Dynamic Authentication
```python
def _generate_assistant_api_key(self) -> str:
    """Generate session-specific API key."""
    ip_address = self._get_client_ip()
    client_name = f'{self.user_agent}/{ip_address}'

    # Request new API key for this session
    auth_endpoint = f'{self.gpt_server}/api/generate-key'
    payload = {'client_name': client_name}

    response = requests.post(auth_endpoint, json=payload)
    return response.json().get('api_key')
```

#### Session Management
```python
def ask_assistant(self, message, spinner_cls=None) -> Tuple[str, str]:
    """Query AI assistant with session tracking."""
    # Generate session-specific API key
    api_key = self._generate_assistant_api_key()

    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }

    # Create chat session
    chat_id = self.get_new_chat_id(
        chat_endpoint=f'{self.gpt_server}/api/chat/create-chat-session',
        persona_id=self.gpt_persona,
        description=message[:20],
        headers=headers
    )

    # Send message with streamlined payload
    payload = {
        "chat_session_id": chat_id,
        "message": message,
        "parent_message_id": None
    }

    # Stream response and capture assistant_message_id
    assistant_message_id = None
    with requests.post(f'{self.gpt_server}/api/chat/send-message',
                       json=payload, stream=True, headers=headers) as response:
        # Process streaming response...
        # Capture assistant_message_id from response

    return assistant_message_id, api_key  # For feedback tracking
```

#### Feedback System
```python
def provide_assistant_feedback(self, chat_message_id: str,
                              api_key: str, is_positive: bool,
                              feedback_text: Optional[str] = None) -> bool:
    """Submit user feedback for assistant response."""
    headers = {'api-key': api_key}

    payload = {
        "chat_message_id": chat_message_id,
        "is_positive": is_positive,
        "feedback_text": feedback_text or ("Helpful" if is_positive else "Not helpful"),
        "predefined_feedback": None
    }

    response = requests.post(
        f'{self.gpt_server}/api/chat/create-chat-feedback',
        headers=headers,
        json=payload
    )
    return response.status_code in [200, 201]
```

## API Testing Patterns

### Mock API Responses
```python
from unittest.mock import Mock, patch

@patch('vss_cli.config.Configuration.get_vms')
def test_vm_listing(mock_get_vms):
    mock_get_vms.return_value = [
        {'moref': 'vm-1', 'name': 'test-vm'}
    ]

    result = list_vms()
    assert 'test-vm' in result
```

### Integration Testing
```python
# Test with real API (dev environment)
def test_vm_operations():
    ctx = Configuration()
    ctx.load_config()

    # Test read operations
    vms = ctx.get_vms(per_page=1)
    assert len(vms) <= 1
```

This API integration provides robust, extensible access to ITS Private Cloud resources with comprehensive error handling and performance optimization.