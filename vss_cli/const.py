"""Constants used by VSS CLI (vss-cli)."""
import os

PACKAGE_NAME = 'vss_cli'

__version__ = '0.1.0.dev0'

REQUIRED_PYTHON_VER = (3, 5, 3)

DEFAULT_OUTPUT = 'json'
DEFAULT_TIMEOUT = 30
DEFAULT_SERVER = 'https://cloud-api.eis.utoronto.ca'
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
    ('MOID', 'moref'),
    ('NAME', 'name')
]
COLUMNS_REQUEST = [
    ('ID', 'id'),
    ('STATUS', 'status'),
    ('CREATED', 'created_on'),
    ('UPDATED', 'updated_on'),
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
    ('ERRORS', 'message.errors'),
    ('WARNINGS', 'message.warnings'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
]
COLUMNS_REQUEST_CHANGE = [
    ('VM NAME', 'vm_name'),
    ('VM UUID', 'vm_uuid'),
    ('ATTRIBUTE', 'attribute'),
    ('VALUE', 'value[*]'),
    ('ERRORS', 'message.errors'),
    ('WARNINGS', 'message.warnings'),
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
    ('ERRORS', 'message.errors'),
    ('WARNINGS', 'message.warnings'),
]
COLUMNS_REQUEST_FOLDER = [
    ('ACTION', 'action'),
    ('MOREF', 'moref'),
    ('TASK', 'task_id'),
    ('USER', 'user.username'),
    ('ERRORS', 'message.errors'),
    ('WARNINGS', 'message.warnings'),
]