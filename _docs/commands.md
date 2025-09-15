# VSS CLI Command Reference

## Command Structure

VSS CLI follows a hierarchical command structure: `vss-cli <category> <resource> <action>`

## Core Command Categories

### 1. Compute Commands

#### Virtual Machine Management
```bash
# VM Lifecycle
vss compute vm ls                           # List virtual machines
vss compute vm ls -f "folder.path=prod"    # Filter by folder
vss compute vm get VM_ID                   # Get VM details
vss compute vm mk from-template            # Deploy from template
vss compute vm mk from-spec               # Deploy from specification
vss compute vm rm VM_ID                   # Delete VM

# VM Configuration
vss compute vm set power-on VM_ID          # Power on VM
vss compute vm set power-off VM_ID         # Power off VM
vss compute vm set cpu VM_ID --count 4     # Modify CPU
vss compute vm set memory VM_ID --gb 8     # Modify memory
vss compute vm set nic VM_ID --add         # Add network interface
vss compute vm set disk VM_ID --add        # Add disk

# VM Information
vss compute vm get VM_ID --attr guest      # Guest OS info
vss compute vm get VM_ID --attr hardware   # Hardware config
vss compute vm get VM_ID --attr snapshot   # Snapshot info
```

#### Template Management
```bash
vss compute template ls                     # List templates
vss compute template get TEMPLATE_ID       # Template details
vss compute template set TEMPLATE_ID       # Modify template
```

#### Network Management
```bash
vss compute net ls                          # List networks
vss compute net get NETWORK_ID             # Network details
vss compute net ls --show-all              # All networks
```

#### Folder Management
```bash
vss compute folder ls                       # List folders
vss compute folder get FOLDER_ID           # Folder details
vss compute folder mk                       # Create folder
vss compute folder rm FOLDER_ID            # Delete folder
```

#### Infrastructure
```bash
vss compute domain ls                       # List compute domains
vss compute os ls                          # List operating systems
vss compute inventory export               # Export inventory
```

### 2. Request Management

#### Request Lifecycle
```bash
vss request ls                             # List requests
vss request ls -f "status=PENDING"        # Filter by status
vss request get REQUEST_ID                 # Request details
vss request get REQUEST_ID --wait          # Wait for completion
```

#### Request Types
```bash
# New VM requests
vss request new ls                         # List VM requests
vss request new get REQUEST_ID             # New VM request details

# Change requests
vss request change ls                      # List change requests
vss request change get REQUEST_ID          # Change request details

# Snapshot requests
vss request snapshot mk VM_ID              # Create snapshot
vss request snapshot rm VM_ID SNAPSHOT_ID  # Delete snapshot
vss request snapshot revert VM_ID SNAP_ID  # Revert to snapshot

# Retirement requests
vss request retirement mk VM_ID            # Schedule retirement
vss request retirement cancel REQUEST_ID   # Cancel retirement
```

### 3. Account Management

#### User Account
```bash
vss account get                            # Account information
vss account set                            # Update account settings
vss account set notification             # Notification preferences
vss account set mfa mk EMAIL             # Enable MFA
vss account set mfa rm                   # Disable MFA
```

#### SSH Key Management
```bash
vss key ls                                # List SSH keys
vss key mk                                # Add SSH key
vss key rm KEY_ID                         # Remove SSH key
```

### 4. Storage Management

#### Object Storage (vskey-stor)
```bash
vss stor ls                               # List storage buckets
vss stor get BUCKET_NAME                  # Bucket contents
vss stor up FILE BUCKET_NAME              # Upload file
vss stor down BUCKET_NAME/FILE            # Download file
vss stor rm BUCKET_NAME/FILE              # Delete file
vss stor share BUCKET_NAME/FILE           # Generate share link
```

### 5. Token Management

#### Authentication Tokens
```bash
vss token ls                              # List active tokens
vss token mk                              # Create new token
vss token rm TOKEN_ID                     # Revoke token
vss token get TOKEN_ID                    # Token details
```

### 6. Configuration

#### CLI Configuration
```bash
vss configure mk                          # Initial setup
vss configure upgrade                     # Upgrade config format
vss configure get                         # Show configuration
vss configure set                         # Update settings
```

#### Shell Integration
```bash
vss shell                                 # Interactive shell
vss completion bash                       # Bash completion
vss completion zsh                        # Zsh completion
```

### 7. Assistant & AI

#### GPT Assistant
```bash
vss assist "How to deploy Ubuntu VM?"     # Ask question
vss assist                                # Interactive mode
```

#### Model Context Protocol
```bash
vss mcp install                           # Install MCP server
vss mcp start                             # Start MCP server
vss mcp status                           # Check MCP status
```

## Common Command Patterns

### Filtering and Pagination
```bash
# Filter expressions
vss compute vm ls -f "status,eq,POWERED_ON"
vss compute vm ls -f "folder.path,like,/prod/"
vss compute vm ls -f "name,in,web-01,web-02"

# Pagination
vss compute vm ls --page-size 50          # Custom page size
vss compute vm ls --all                   # All results

# Sorting
vss compute vm ls --sort-by name          # Sort by name
vss compute vm ls --sort-by created_on    # Sort by creation date
```

### Output Formatting
```bash
# Output formats
vss compute vm ls --output json           # JSON output
vss compute vm ls --output yaml           # YAML output
vss compute vm ls --output table          # Table output (default)

# Custom columns
vss compute vm ls --columns "NAME=name,CPU=cpu_count,MEM=memory_gb"

# Table formatting
vss compute vm ls --table-format grid     # Grid table format
vss compute vm ls --no-headers            # No column headers
```

### File Input
```bash
# JSON/YAML file input
vss compute vm mk from-spec vm-spec.yaml
vss compute vm set nic VM_ID --spec nic-config.json

# Custom specification example
cat > vm-spec.yaml << EOF
name: "web-server-01"
template: "Ubuntu-22.04"
cpu: 4
memory: 8
networks:
  - name: "production"
    dhcp: true
custom_spec:
  hostname: "web01"
  domain: "example.com"
EOF
```

### Async Operations
```bash
# Fire and forget
vss compute vm mk from-template --source "Ubuntu-22.04" --no-wait

# Wait for completion
vss compute vm mk from-template --source "Ubuntu-22.04" --wait

# Monitor separately
vss request get REQUEST_ID --wait
```

## Advanced Command Usage

### Bulk Operations
```bash
# Deploy multiple VMs
for i in {1..3}; do
  vss compute vm mk from-template \
    --source "Ubuntu-22.04" \
    --name "web-$i" \
    --no-wait
done

# Power off multiple VMs
vss compute vm ls -f "folder.path=/dev/" --output json | \
  jq -r '.[].moref' | \
  xargs -I {} vss compute vm set power-off {}
```

### Complex Filtering
```bash
# Complex filter expressions
vss compute vm ls \
  -f "status,eq,POWERED_ON" \
  -f "folder.path,like,/production/" \
  -f "memory_gb,gt,8"

# Date-based filtering
vss request ls \
  -f "created_on,gt,2025-01-01" \
  -f "status,in,PROCESSED,SCHEDULED"
```

### Pipeline Integration
```bash
# Extract specific data
vss compute vm ls --output json | \
  jq '.[] | select(.power_state == "POWERED_ON") | .name'

# Generate reports
vss compute vm ls --all --output json | \
  jq -r '.[] | [.name, .cpu_count, .memory_gb, .power_state] | @csv' > vm-report.csv
```

### Configuration Management
```bash
# Environment-specific configs
export VSS_CONFIG=/path/to/dev-config.yaml
vss compute vm ls

# Multiple endpoint usage
vss configure mk --endpoint https://dev-api.example.com
vss --endpoint https://prod-api.example.com compute vm ls
```

## Error Handling

### Common Error Scenarios
```bash
# Invalid credentials
vss compute vm ls
# Error: Invalid configuration. Run "vss-cli configure mk"

# Resource not found
vss compute vm get invalid-vm-id
# Error: VM invalid-vm-id could not be found

# Permission denied
vss compute vm rm vm-123
# Error: Permission denied for operation
```

### Debug Mode
```bash
# Enable debug output
vss --debug compute vm get VM_ID

# Verbose logging
vss --verbose compute vm mk from-template ...

# Exception details
vss -x compute vm mk from-template ...
```

## Shell Integration

### Interactive Shell
```bash
vss shell
# Enters interactive mode with:
# - Tab completion
# - Command history
# - Persistent session
```

### Bash/Zsh Completion
```bash
# Enable completion
eval "$(_VSS_CLI_COMPLETE=bash_source vss-cli)"

# Tab completion examples
vss compute vm <TAB>        # Shows: ls, get, mk, set, rm
vss compute vm set <TAB>    # Shows: power-on, power-off, cpu, memory
```

This command reference provides comprehensive coverage of VSS CLI capabilities for effective cloud resource management.