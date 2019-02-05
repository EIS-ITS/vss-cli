"""Constants used by VSS CLI (vss-cli)."""
import os

PACKAGE_NAME = 'vss_cli'

__version__ = '0.1.0.dev0'

REQUIRED_PYTHON_VER = (3, 5, 3)

DEFAULT_OUTPUT = 'json'
DEFAULT_TIMEOUT = 30
DEFAULT_SERVER = 'https://cloud-api.eis.utoronto.ca'
DEFAULT_WEBDAV_SERVER = 'https://vskey-stor.eis.utoronto.ca'
DEFAULT_CONFIG = os.path.expanduser(os.path.join('~', '.vss-cli', 'config.json'))
DEFAULT_HISTORY = os.path.expanduser(os.path.join('~', '.vss-cli', 'history'))

DEFAULT_DATAOUTPUT = 'yaml'

DEFAULT_HOST_REGEX = "^[a-z][a-z0-9+\\-.]*://([a-z0-9\\" \
                     "-._~%!$&'()*+,;=]+@)?([a-z0-9\\-." \
                     "_~%]+|\\[[a-z0-9\\-._~%!$&'()*+,;" \
                     "=:]+\\])"

COLUMNS_TWO_FMT = "{0:<20}: {1:<20}"

COLUMNS_DEFAULT = [('ALL', '*')]
COLUMNS_VIM = [
    ('UUID', 'uuid'),
    ('NAME', 'name')
]
COLUMNS_MOID = [
    ('MOREF', 'moref'),
    ('NAME', 'name')
]
COLUMNS_MIN = [
    ('ID', 'id'),
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
]
COLUMNS_REQUEST = [
    ('ID', 'id'),
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
    ('STATUS', 'status'),
]
COLUMNS_REQUEST_SUBMITTED = [
    ('ID', 'request.id'),
    ('STATUS', 'request.status'),
    ('TASK ID', 'request.task_id'),
    ('MESSAGE', 'message')
]
COLUMNS_REQUEST_SNAP = [
    ('DESCRIPTION', 'snapshot.description'),
    ('ID', 'snapshot.snap_id'),
    ('EXTENSIONS', 'extensions'),
    ('ACTION', 'action'),
    ('VM NAME', 'vm_name'),
    ('VM UUID', 'vm_uuid'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
]
COLUMNS_REQUEST_CHANGE = [
    ('VM NAME', 'vm_name'),
    ('VM UUID', 'vm_uuid'),
    ('ATTRIBUTE', 'attribute'),
    ('VALUE', 'value[*]'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('SCHEDULED', 'scheduled_datetime'),
    ('APPROVED', 'approval.approved')
]
COLUMNS_REQUEST_EXPORT = [
    ('VM NAME', 'vm_name'),
    ('VM UUID', 'vm_uuid'),
    ('TRANSFERRED', 'transferred'),
    ('FILES', 'files[*]'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
]
COLUMNS_REQUEST_FOLDER = [
    ('ACTION', 'action'),
    ('MOREF', 'moref'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
]
COLUMNS_REQUEST_INVENTORY = [
    ('NAME', 'name'),
    ('FORMAT', 'format'),
    ('PROPS', 'properties.data[*]'),
    ('FILTERS', 'filters'),
    ('HITS', 'hits'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
]
COLUMNS_REQUEST_NEW = [
    ('VM NAME', 'vm_name'),
    ('VM UUID', 'vm_uuid'),
    ('DOMAIN', 'domain'),
    ('SOURCE', 'source_vm'),
    ('SOURCE', 'source_template'),
    ('SOURCE', 'source_image'),
    ('FOLDER', 'folder'),
    ('CPU', 'cpu'),
    ('MEMORY', 'memory'),
    ('DISKS', 'disks[*]'),
    ('NETWORKS', 'networks[*]'),
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('APPROVED', 'approval.approved')
]
COLUMNS_TK = [
    ('ID', 'id'),
    ('CREATED', 'status.created_on'),
    ('UPDATED', 'status.updated_on'),
    ('LAST ACCESS', 'status.last_access'),
    ('LAST IP', 'status.ip_address')
]
COLUMNS_MESSAGE = [
    ('ID', 'id'),
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
    ('KIND', 'kind'),
    ('STATUS', 'status'),
    ('FROM', 'user.username'),
    ('SUBJECT', 'subject'),
    ('TEXT', 'text')
]
COLUMNS_VM = [
    ('UUID', 'uuid'),
    ('NAME', 'name')
]
COLUMNS_GROUP = [
    ('NAME', 'cn'),
    ('DESCRIPTION', 'description'),
    ('CREATED', 'createTimestamp'),
    ('MODIFIED', 'modifyTimestamp'),
    ('MEMBERS', 'uniqueMemberCount'),
    ('MEMBER', 'uniqueMember[*].uid')
]
COLUMNS_GROUPS = [
    ('GROUPS', 'groups[*]')
]
COLUMNS_ROLE = [
    ('NAME', 'name'),
    ('DESCRIPTION', 'description'),
    ('ENTITLEMENTS', 'entitlements[*]')
]
COLUMNS_USER_PERSONAL = [
    ('USERNAME', 'username'),
    ('NAME', 'full_name'),
    ('EMAIL', 'email'),
    ('PHONE', 'phone'),
    ('AUTH', 'authTimestamp'),
    ('PWDCHANGE', 'pwdChangeTime'),
    ('LOCKED', 'pwdAccountLockedTime')
]
COLUMNS_USER_STATUS = [
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
    ('LAST ACCESS', 'last_access'),
    ('LAST IP', 'ip_address')
]
COLUMNS_MESSAGE_DIGEST = [
    ('MESSAGE', 'message')
]
COLUMNS_NOT_REQUEST = [
    ('ALL', 'all'),
    ('NONE', 'none'),
    ('COMPLETION', 'completion'),
    ('ERROR', 'error'),
    ('SUBMISSION', 'submission')

]
COLUMNS_WEBDAV = [
    ('FILES', '[*]')
]
COLUMNS_WEBDAV_INFO = [
    ('CREATED', 'created'),
    ('MODIFIED', 'modified'),
    ('NAME', 'name'),
    ('SIZE', 'size')
]
