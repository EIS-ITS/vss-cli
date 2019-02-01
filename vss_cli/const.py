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
    ('CREATED_ON', 'created_on'),
    ('UPDATED_ON', 'updated_on'),
    ('STATUS', 'status')
]
