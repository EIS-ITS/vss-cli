"""Compute plugin for VSS CLI (vss-cli)."""
import click
from vss_cli.cli import pass_context
from vss_cli.config import Configuration


@click.group(
    'compute',
    short_help='Manage VMs, networks, folders, etc.'
)
@pass_context
def cli(ctx: Configuration):
    """Compute related resources such as virtual machines, networks
       supported operating systems, logical folders, OVA/OVF images,
       floppy images, ISO images and more."""
    ctx.load_config()


from vss_cli.plugins.compute_plugins import (
    domain, inventory, net, os as compute_os
)  # pylint: disable=unused-import

