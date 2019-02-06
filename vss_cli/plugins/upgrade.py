"""Status plugin for VSS CLI (vss-cli)."""
import click
from subprocess import call


@click.group(
    'upgrade',
    invoke_without_command=True,
    short_help='Upgrade VSS CLI and dependencies.')
def cli():
    """Upgrade existing install of VSS CLI to the latest version
    (experimental)."""
    try:
        import pip
        exit_code = call("pip install --upgrade vss-cli", shell=True)
        if exit_code > 0:
            raise click.ClickException(
                'Could not perform upgrade, please try: '
                '\n\tpip install --upgrade vsscli')
    except ImportError as ex:
        raise click.UsageError('Pip is required to upgrade VSS CLI')
