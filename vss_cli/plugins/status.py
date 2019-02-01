"""Status plugin for VSS CLI (vss-cli)."""
import click
from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.helper import format_output
from vss_cli.sstatus import check_status


@click.group(
    invoke_without_command=True,
    short_help='Check VSS Status.'
)
@pass_context
def cli(ctx: Configuration):
    """Check VSS Status from https://www.systemstatus.utoronto.ca/"""
    obj = check_status()
    columns = [
        ('NAME', 'component.name'),
        ('DESCRIPTION', 'component.description'),
        ('STATUS', 'component.status'),
        ('UPDATED', 'component.updated_at'),
        ('MAINTENANCES', 'upcoming_maintenances[*]')
    ]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )

