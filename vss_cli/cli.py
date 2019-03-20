"""VSS CLI (vss-cli)."""
import logging
import os
import sys
from typing import List, Optional, Union, cast
import pyvss

import click
from click.core import Command, Context, Group
import click_log
import vss_cli.autocompletion as autocompletion
from vss_cli.config import Configuration
import vss_cli.const as const
from vss_cli.helper import debug_requests_on, to_tuples

click_log.basic_config()

_LOGGER = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(auto_envvar_prefix='VSS')

pass_context = click.make_pass_decorator(  # pylint: disable=invalid-name
    Configuration, ensure=True
)


def run() -> None:
    """Run entry point.

    Wraps click for full control over exception handling in Click.
    """
    # A hack to see if exception details should be printed.
    exceptionflags = ['-x']
    verbose = [c for c in exceptionflags if c in sys.argv]

    try:
        # Could use cli.invoke here to use the just created context
        # but then shell completion will not work. Thus calling
        # standalone mode to keep that working.
        result = cli.main(standalone_mode=False)
        if isinstance(result, int):
            sys.exit(result)

    # Exception handling below is done to use logger
    # and mimic as close as possible what click would
    # do normally in its main()
    except click.ClickException as ex:
        ex.show()  # let Click handle its own errors
        sys.exit(ex.exit_code)
    except click.Abort:
        _LOGGER.critical("Aborted!")
        sys.exit(1)
    except Exception as ex:  # pylint: disable=broad-except
        if verbose:
            _LOGGER.exception(ex)
        else:
            _LOGGER.error("%s: %s", type(ex).__name__, ex)
            _LOGGER.info(
                "Run with %s to see full exception infomation.",
                " or ".join(exceptionflags),
            )
        sys.exit(1)


class VssCli(click.Group):
    """The ITS Private Cloud Command-line."""

    def list_commands(self, ctx: Context) -> List[str]:
        """List all command available as plugin."""
        cmd_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'plugins')
        )

        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and not filename.startswith('__'):
                commands.append(filename[:-3])
        commands.sort()
        _LOGGER.debug(f'Loading {commands}')
        return commands

    def get_command(
        self, ctx: Context, cmd_name: str
    ) -> Optional[Union[Group, Command]]:
        """Import the commands of the plugins."""
        try:
            mod = __import__(
                '{}.plugins.{}'.format(const.PACKAGE_NAME, cmd_name),
                {},
                {},
                ['cli'],
            )
            _LOGGER.debug(f'Loading {mod}')
        except ImportError as ex:
            _LOGGER.warning(
                f'Error loading plugin'
                f' {cmd_name} {type(ex).__name__}: {ex}'
            )
            return None
        return cast(Union[Group, Command], mod.cli)


def _default_token() -> Optional[str]:
    return os.environ.get('VSS_TOKEN', os.environ.get('VSS_API_TOKEN', None))


@click.command(cls=VssCli, context_settings=CONTEXT_SETTINGS)
@click_log.simple_verbosity_option(logging.getLogger(), "--loglevel", "-l")
@click.option(
    '--server',
    '-s',
    help='The server URL',
    default=const.DEFAULT_SERVER,
    show_default=True,
    envvar='VSS_ENDPOINT',
)
@click.option(
    '--config',
    default=const.DEFAULT_CONFIG,
    help='Configuration file',
    envvar='VSS_CONFIG'
)
@click.option(
    '--token',
    default=_default_token,
    help='The Bearer token for the VSS API.',
    envvar='VSS_TOKEN',
)
@click.option(
    '--username',
    default=None,  # type: ignore
    help='The API username for VSS API.',
    envvar='VSS_USER',
)
@click.option(
    '--password',
    default=None,  # type: ignore
    help='The API password for VSS API.',
    envvar='VSS_USER_PASSWORD',
)
@click.option(
    '--timeout',
    help='Timeout for network operations.',
    default=const.DEFAULT_TIMEOUT,
    show_default=True,
)
@click.option(
    '--output',
    '-o',
    help="Output format.",
    type=click.Choice(['json', 'yaml', 'table', 'auto']),
    envvar='VSS_OUTPUT',
    default='auto',
    show_default=True,
)
@click.option(
    '-v',
    '--verbose',
    is_flag=True,
    default=False,
    help='Enables verbose mode.',
)
@click.option(
    '-x',
    'showexceptions',
    default=False,
    is_flag=True,
    help="Print back traces when exception occurs.",
)
@click.option(
    '--debug',
    is_flag=True,
    default=False,
    help='Enables debug mode.'
)
@click.option(
    '--columns',
    default=None,
    help=(
        'Custom columns key=value list.'
        ' Example: VM=uuid,PROVISIONED=storage.provisionedGB'
    ),
)
@click.option(
    '--no-headers',
    default=False,
    is_flag=True,
    help="When printing tables don\'t use headers (default: print headers)",
)
@click.option(
    '--table-format',
    default='simple',
    envvar='VSS_TABLE',
    help="Which table format to use (default: simple)",
    autocompletion=autocompletion.table_formats,
)
@click.option(
    '--sort-by',
    default=None,
    help='Sort table by the jsonpath expression. Example: updated_on',
)
@click.version_option(
    version=f'{const.__version__}; pyvss v{pyvss.__version__}',
    message='%(prog)s v%(version)s'
)
@pass_context
def cli(
    ctx: Configuration,
    verbose: bool,
    server: str,
    token: Optional[str],
    username: Optional[str],
    password: Optional[str],
    config: str,
    output: str,
    timeout: int,
    debug: bool,
    showexceptions: bool,
    columns: str,
    no_headers: bool,
    table_format: str,
    sort_by: Optional[str],
):
    """Command line interface for the ITS Private Cloud."""
    ctx.verbose = verbose
    ctx.server = server
    ctx.token = token
    ctx.config = config
    ctx.username = username
    ctx.password = password
    ctx.timeout = timeout
    ctx.output = output
    ctx.debug = debug
    ctx.showexceptions = showexceptions
    ctx.columns = to_tuples(columns)
    ctx.no_headers = no_headers
    ctx.table_format = table_format
    ctx.sort_by = sort_by  # type: ignore

    if debug:
        debug_requests_on()

    _LOGGER.debug("Using settings: %s", ctx)

    if ctx.server:
        _LOGGER.debug(f"Updating endpoint from {ctx.api_endpoint} to {server}")
        ctx.update_endpoints(ctx.server)
        _LOGGER.debug(f"Using {ctx.api_endpoint}")
