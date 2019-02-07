"""Constants used by VSS CLI (vss-cli)."""
import os

PACKAGE_NAME = 'vss_cli'

__version__ = '0.1.0.dev0'

REQUIRED_PYTHON_VER = (3, 5, 3)

DEFAULT_TIMEOUT = 30
DEFAULT_SERVER = 'https://cloud-api.eis.utoronto.ca'
DEFAULT_WEBDAV_SERVER = 'https://vskey-stor.eis.utoronto.ca'
DEFAULT_CONFIG = os.path.expanduser(os.path.join('~', '.vss-cli', 'config.json'))
DEFAULT_HISTORY = os.path.expanduser(os.path.join('~', '.vss-cli', 'history'))

DEFAULT_DATAOUTPUT = 'table'

DEFAULT_HOST_REGEX = "^[a-z][a-z0-9+\\-.]*://([a-z0-9\\" \
                     "-._~%!$&'()*+,;=]+@)?([a-z0-9\\-." \
                     "_~%]+|\\[[a-z0-9\\-._~%!$&'()*+,;" \
                     "=:]+\\])"

COLUMNS_TWO_FMT = "{0:<20}: {1:<20}"

COLUMNS_DEFAULT = [('ALL', '*')]
COLUMNS_VM_MIN = [
    ('UUID', 'uuid'),
    ('NAME', 'name')
]
COLUMNS_VIM_REQUEST = [
    ('UUID', 'vm_uuid'),
    ('NAME', 'vm_name')
]
COLUMNS_MOID = [
    ('MOREF', 'moref'),
    ('NAME', 'name')
]
COLUMNS_FOLDER = [
    *COLUMNS_MOID,
    ('PARENT', 'parent'),
    ('PATH', 'path')
]
COLUMNS_NET_MIN = [
    *COLUMNS_MOID,
    ('DESCRIPTION', 'description'),
    ('SUBNET', 'subnet'),
    ('PORTS', 'ports')
]
COLUMNS_NET = [
    *COLUMNS_NET_MIN,
    ('ACCESSIBLE', 'accessible'),
    ('ADMIN', 'admin'),
    ('ADMIN', 'client'),
]
COLUMNS_PERMISSION = [
    ('PRINCIPAL', 'principal'),
    ('GROUP', 'group'),
    ('PROPAGATE', 'propagate')
]
COLUMNS_MIN = [
    ('ID', 'id'),
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
]
COLUMNS_IMAGE = [
    ('ID', 'id'),
    ('PATH', 'path'),
    ('NAME', 'name')
]
COLUMNS_OS = [
    ('ID', 'id'),
    ('GUESTID', 'guestId'),
    ('NAME', 'guestFullName')
]
COLUMNS_REQUEST = [
    *COLUMNS_MIN,
    ('STATUS', 'status'),
]
COLUMNS_REQUEST_MAX = [
    ('ERRORS', 'message.errors[*]'),
    ('WARNINGS', 'message.warnings[*]'),
    ('TASK', 'task_id'),
    ('USER', 'user.username')
]
COLUMNS_REQUEST_IMAGE_SYNC_MIN = [
    *COLUMNS_REQUEST,
    ('TYPE', 'type')
]
COLUMNS_REQUEST_IMAGE_SYNC = [
    *COLUMNS_REQUEST,
    ('TYPE', 'type'),
    ('DELETED', 'deleted'),
    ('ADDED', 'added'),
    *COLUMNS_REQUEST_MAX
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
    *COLUMNS_VIM_REQUEST,
    *COLUMNS_REQUEST_MAX
]
COLUMNS_REQUEST_CHANGE_MIN = [
    *COLUMNS_REQUEST,
    *COLUMNS_VIM_REQUEST,
    ('APPROVED', 'approval.approved'),
    ('ATTRIBUTE', 'attribute'),
]
COLUMNS_REQUEST_CHANGE = [
    *COLUMNS_REQUEST_CHANGE_MIN,
    ('VALUE', 'value[*]'),
    ('SCHEDULED', 'scheduled_datetime'),
    *COLUMNS_REQUEST_MAX,
]
COLUMNS_REQUEST_EXPORT_MIN = [
    *COLUMNS_REQUEST,
    *COLUMNS_VIM_REQUEST,
    ('TRANSFERRED', 'transferred'),
]
COLUMNS_REQUEST_EXPORT = [
    *COLUMNS_REQUEST_EXPORT_MIN,
    ('FILES', 'files[*]'),
    *COLUMNS_REQUEST_MAX
]
COLUMNS_REQUEST_FOLDER_MIN = [
    *COLUMNS_REQUEST,
    ('ACTION', 'action'),
    ('MOREF', 'moref'),
]
COLUMNS_REQUEST_FOLDER = [
    *COLUMNS_REQUEST_FOLDER_MIN,
    *COLUMNS_REQUEST_MAX
]
COLUMNS_REQUEST_INVENTORY_MIN = [
    *COLUMNS_REQUEST,
    ('NAME', 'name'),
    ('FORMAT', 'format')
]
COLUMNS_REQUEST_INVENTORY = [
    *COLUMNS_REQUEST_INVENTORY_MIN,
    ('PROPS', 'properties.data[*]'),
    ('FILTERS', 'filters'),
    ('HITS', 'hits'),
    *COLUMNS_REQUEST_MAX
]
COLUMNS_REQUEST_NEW_MIN = [
    *COLUMNS_REQUEST,
    *COLUMNS_VIM_REQUEST,
    ('APPROVED', 'approval.approved'),
    ('BUILT', 'built_from')
]
COLUMNS_REQUEST_NEW = [
    *COLUMNS_REQUEST_NEW_MIN,
    ('DOMAIN', 'domain'),
    ('SOURCE', 'source_vm'),
    ('SOURCE', 'source_template'),
    ('SOURCE', 'source_image'),
    ('FOLDER', 'folder'),
    ('CPU', 'cpu'),
    ('MEMORY', 'memory'),
    ('DISKS', 'disks[*]'),
    ('NETWORKS', 'networks[*]'),
    *COLUMNS_REQUEST_MAX
]
COLUMNS_TK_MIN = [
    ('ID', 'id'),
    ('CREATED', 'status.created_on'),
    ('UPDATED', 'status.updated_on'),
    ('LAST ACCESS', 'status.last_access'),
    ('LAST IP', 'status.ip_address'),
    ('VALID', 'status.valid')
]
COLUMNS_TK = [
    *COLUMNS_TK_MIN,

]
COLUMNS_MESSAGE_MIN = [
    *COLUMNS_MIN,
    ('KIND', 'kind'),
    ('SUBJECT', 'subject'),
    ('STATUS', 'status')
]
COLUMNS_MESSAGE = [
    *COLUMNS_MIN,
    ('KIND', 'kind'),
    ('STATUS', 'status'),
    ('FROM', 'user.username'),
    ('SUBJECT', 'subject'),
    ('TEXT', 'text')
]
COLUMNS_VM = [
    *COLUMNS_VM_MIN,
    ('FOLDER', 'folder'),
    ('CPU', 'cpuCount'),
    ('MEMORY', 'memoryGB'),
    ('POWER', 'powerState'),
    ('GUEST', 'guestFullName'),
    ('VERSION', 'version')
]
COLUMNS_VM_INFO = [
    ('UUID', 'uuid'),
    ('NAME', 'name.full_name'),
    ('FOLDER', 'folder.path'),
    ('GUEST OS', 'config.os.guestId'),
    ('VERSION', 'hardware.version'),
    ('STATUS', 'state.overallStatus'),
    ('STATE', 'state.powerState'),
    ('ALARMS', 'state.alarms'),
    ('CPU', 'hardware.cpu.cpuCount'),
    ('MEMORY (GB)', 'hardware.memory.memoryGB'),
    ('PROVISIONED (GB)', 'storage.provisionedGB'),
    ('SNAPSHOT', 'snapshot.exist'),
    ('DISKS', 'hardware.devices.disks[*].unit'),
    ('NICS', 'hardware.devices.nics[*].unit')
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
COLUMNS_SSH_KEY_MIN = [
    *COLUMNS_MIN,
    ('TYPE', 'type'),
    ('COMMENT', 'comment')
]
COLUMNS_SSH_KEY = [
    *COLUMNS_SSH_KEY_MIN,
    ('FINGERPRINT', 'fingerprint'),
    ('VALUE', 'value')

]
