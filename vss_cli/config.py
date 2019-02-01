"""Configuration for VSS CLI (vss-cli)."""
import logging
import sys
from typing import Any, Dict, List, Optional, Tuple, cast  # noqa: F401
import platform
import click
import os
import json
from base64 import b64decode, b64encode
import vss_cli.const as const
from pyvss.manager import VssManager
from vss_cli.exceptions import VssCliError
from pyvss import __version__ as pyvss_version


_LOGGING = logging.getLogger(__name__)


class Configuration(VssManager):
    """The configuration context for the VSS CLI."""

    def __init__(self, tk: str = '') -> None:
        """Initialize the configuration."""
        super(Configuration, self).__init__(tk)
        self.user_agent = self._default_user_agent(
            extensions=f'pyvss/{pyvss_version}'
        )
        self.verbose = False  # type: bool
        self.server = const.DEFAULT_SERVER  # type: str
        self.output = const.DEFAULT_OUTPUT  # type: str
        self.config = const.DEFAULT_CONFIG  # type: str
        self.history = const.DEFAULT_HISTORY  # type: str
        self.username = None  # type: Optional[str]
        self.password = None  # type: Optional[str]
        self.token = None  # type: Optional[str]
        self.timeout = const.DEFAULT_TIMEOUT  # type: int
        self.debug = False  # type: bool
        self.showexceptions = False  # type: bool
        self.cert = None  # type: Optional[str]
        self.columns = None  # type: Optional[List[Tuple[str, str]]]
        self.no_headers = False
        self.table_format = 'plain'
        self.sort_by = None

    def get_token(self, user: str = '', password: str = ''):
        self.api_token = super(Configuration, self).get_token(user, password)
        return self.api_token

    def update_endpoints(self, endpoint: str = ''):
        """ Rebuilds API endpoints"""
        self.api_endpoint = f'{endpoint}/v2'
        self.base_endpoint = endpoint
        self.token_endpoint = f'{endpoint}/auth/request-token'

    def echo(self, msg: str, *args: Optional[Any]) -> None:
        """Put content message to stdout."""
        self.log(msg, *args)

    def log(  # pylint: disable=no-self-use
        self, msg: str, *args: Optional[str]
    ) -> None:  # pylint: disable=no-self-use
        """Log a message to stdout."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stdout)

    def vlog(self, msg: str, *args: Optional[str]) -> None:
        """Log a message only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

    def __repr__(self) -> str:
        """Return the representation of the Configuration."""
        view = {
            "server": self.server,
            "access-token": 'yes' if self.token is not None else 'no',
            "user": 'yes' if self.username is not None else 'no',
            "user-password": 'yes' if self.password is not None else 'no',
            "output": self.output,
            "verbose": self.verbose,
        }

        return "<Configuration({})".format(view)

    def auto_output(self, auto_output: str) -> str:
        """Configure output format."""
        if self.output == "auto":
            if auto_output == 'data':
                auto_output = const.DEFAULT_DATAOUTPUT
            _LOGGING.debug("Setting auto-output to: %s", auto_output)
            self.output = auto_output
        return self.output

    @staticmethod
    def _default_user_agent(name: str = const.PACKAGE_NAME,
                            version: str = const.__version__,
                            extensions: str = ''):
        environment = {'product': name,
                       'product_version': version,
                       'python_version': platform.python_version(),
                       'system': platform.system(),
                       'system_version': platform.release(),
                       'platform_details': platform.platform(),
                       'extensions': extensions
                       }
        # User-Agent:
        # <product>/<version> (<system-information>)
        # <platform> (<platform-details>) <extensions>
        user_agent = '{product}/{product_version}' \
                     ' ({system}/{system_version}) ' \
                     'Python/{python_version} ({platform_details}) ' \
                     '{extensions}'.format(**environment)
        return user_agent

    def load_profile_from_config(self, endpoint):
        username, password, token = None, None, None
        profiles = self.load_raw_config_file()
        profile = profiles.get(endpoint)
        if profile:
            # get auth attr
            auth = profile.get('auth')
            # get token attr
            token = profile.get('token')
            if not auth or not token:
                raise Exception('Invalid configuration file')
            auth_enc = auth.encode()
            credentials_decoded = b64decode(auth_enc)
            # get user/pass
            username, password = \
                credentials_decoded.split(b':')
        return username, password, token

    def load_raw_config_file(self):
        try:
            with open(self.config, 'r') as f:
                profiles = json.load(f)
                return profiles
        except ValueError as ex:
            raise Exception('Invalid configuration file.')

    def load_config(self):
        try:
            if self.server:
                self.update_endpoints(self.server)
            # check for environment variables
            if self.token or \
                    (self.username and
                     self.password):
                # don't load config file
                if self.token:
                    # set api token
                    self.api_token = self.token
                    return self.username, self.password, self.api_token
                elif self.username and self.password:
                    # generate a new token - won't save
                    self.get_token()
                    return self.username, self.password, self.api_token
                else:
                    raise VssCliError(
                        'Environment variables error. Please, verify '
                        'VSS_TOKEN or VSS_USER and VSS_USER_PASS')
            else:
                self.vlog(f'Loading configuration file: {self.config}')
                if os.path.isfile(self.config):
                    # read config and look for profile
                    self.username, self.password, self.api_token = \
                        self.load_profile_from_config(self.base_endpoint)
                    self.vlog(f'Loaded from file {self.base_endpoint}:'
                              f' {self.username}')
                    creds = self.username and self.password
                    if not (creds or self.api_token):
                        raise VssCliError(
                            "Invalid endpoint {} configuration. \n "
                            "Please, run 'vss configure' to add "
                            "endpoint to "
                            "configuration.".format(self.base_endpoint))
                    try:
                        self.whoami()
                    except VssCliError as ex:
                        if self.debug:
                            self.log(str(ex))
                            self.echo('Generating a new token')
                        self.api_token = self.get_token(self.username,
                                                        self.password)
                        if self.debug:
                            self.echo('Token generated successfully')
                        self.write_config_file(new_token=self.api_token)
                        # check for updates
                        # self.check_for_updates()
                        # check for unread messages
                        # self.check_unread_messages()
                    return self.username, self.password, self.api_token
            raise VssCliError("Invalid configuration. "
                              "Please, run "
                              "'vss configure' to initialize configuration.")
        except Exception as ex:
            raise VssCliError(str(ex))

    def write_config_file(self, new_token=None):
        """
        Creates or updates configuration file with different
        endpoints.

        :param new_token: new api token to store
        :return:
        """
        token = new_token or self.get_token(self.username,
                                            self.password)
        username = self.username if isinstance(self.username, bytes) \
            else self.username.encode()
        password = self.password if isinstance(self.password, bytes) \
            else self.password.encode()
        credentials = b':'.join([username,
                                 password])
        config_dict = {self.base_endpoint: {
            'auth': b64encode(credentials).strip().decode('utf-8'),
            'token': token}
        }
        try:
            self.vlog(f'Writing configuration file:'
                      f' {self.config}')
            # validate if file exists
            if os.path.isfile(self.config):
                with open(self.config, 'r+') as fp:
                    try:
                        _conf_dict = json.load(fp)
                    except ValueError:
                        _conf_dict = {}
                    _conf_dict.update(config_dict)
                    fp.seek(0)
                    json.dump(_conf_dict, fp,
                              sort_keys=True,
                              indent=4)
                    fp.truncate()
            else:
                with open(self.config, 'w') as fp:
                    _conf_dict = config_dict
                    json.dump(_conf_dict, fp,
                              sort_keys=True,
                              indent=4)
        except IOError as e:
            raise VssCliError('An error occurred writing '
                              'configuration file: {}'.format(e))
        if self.debug:
            self.echo(f'Successfully written'
                      f' configuration file {self.config}')

    def configure(self, username, password, endpoint, replace=False):
        self.username = username
        self.password = password
        # update instance endpoints if provided
        self.update_endpoints(endpoint)
        # directory available
        if not os.path.isdir(os.path.dirname(self.config)):
            os.mkdir(os.path.dirname(self.config))
        # config file
        if os.path.isfile(self.config):
            try:
                # load credentials by endpoint
                e_username, e_password, e_api_token = \
                    self.load_profile_from_config(self.base_endpoint)
                if not (e_username and e_password and e_api_token):
                    self.echo('Profile not found.')
                    self.write_config_file()

                if e_username and e_password and e_api_token:
                    confirm = replace or click.confirm(
                        'Would you like to replace existing configuration?')
                    if confirm:
                        self.write_config_file()
                else:
                    self.echo(
                        'Successfully configured credentials for {}. '
                        'You are ready to use '
                        'VSS CLI.'.format(self.base_endpoint))
            except VssCliError as ex:
                self.echo(str(ex))
                confirm = click.confirm(
                    'Would you like to replace existing configuration?')
                if confirm:
                    self.write_config_file()
        else:
            self.write_config_file()
