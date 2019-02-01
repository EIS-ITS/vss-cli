"""Shell plugin for VSS CLI (vss-cli)."""
import click
import os
from click_repl import repl
from prompt_toolkit.history import FileHistory
from vss_cli.cli import pass_context
from vss_cli import const
from vss_cli.config import Configuration
from vss_cli.helper import get_hostname_from_url


@click.group('shell',
             invoke_without_command=True)
@click.option('-i', '--history', type=click.STRING,
              help='File path to save history',
              default=const.DEFAULT_HISTORY,
              required=False)
@pass_context
def cli(ctx: Configuration, history):
    """REPL interactive shell."""
    endpoint = ctx.api_endpoint
    _message_pfix = 'vss'
    _message_sfix = '> '
    # obtain hostname
    _host = get_hostname_from_url(const.DEFAULT_HISTORY,
                                  endpoint)
    if _host:
        _message = [_message_pfix, '({})'.format(_host),
                    _message_sfix]
    else:
        _message = [_message_pfix, _message_sfix]
    _message = u' '.join(_message)
    welcome = r"""
    __   _____ ___
    \ \ / / __/ __|      API Endpoint: {endpoint}
     \ V /\__ \__ \      Tab-completion & suggestions
      \_/ |___/___/      Prefix external commands with "!"
       CLI v{version}        History is saved: {history}

    Exit shell with :exit, :q, :quit, ctrl+d
    """.format(version=const.__version__,
               history=history,
               endpoint=endpoint)
    click.secho(welcome, fg='blue')
    dir_name = os.path.dirname(ctx.history)
    # create dir for history
    if not os.path.exists(os.path.expanduser(dir_name)):
        os.mkdir(os.path.expanduser(dir_name))
    # run repl
    prompt_kwargs = {
        'history': FileHistory(history),
        'message': _message
    }
    repl(ctx, prompt_kwargs=prompt_kwargs,
         allow_internal_commands=True,
         allow_system_commands=True)

