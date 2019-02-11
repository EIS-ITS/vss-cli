import click
import logging
import os
from vss_cli import const
from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.helper import format_output
from vss_cli.plugins.compute import cli
from vss_cli.exceptions import VssCliError


_LOGGING = logging.getLogger(__name__)


@cli.group(
    'vm',
    short_help='Manage virtual machines'
)
@pass_context
def compute_vm(ctx: Configuration):
    """List, update, deploy and delete instances."""
    pass


@compute_vm.command(
    'ls',
    short_help='List virtual machine'
)
@click.option(
    '-f', '--filter',
    multiple=True,
    type=(click.STRING, click.STRING),
    help='Filter list by name, ip, dns or path.'
)
@click.option(
    '-o', '--sort',
    type=click.STRING,
    help='sort by name or uuid. If summary is enabled, '
         'sort by more attributes.'
)
@click.option(
    '-s', '--summary', is_flag=True,
    help='Display summary'
)
@click.option(
    '-p', '--page', is_flag=True,
    help='Page results in a less-like format'
)
@pass_context
def compute_vm_ls(
        ctx: Configuration,
        filter, summary, page, sort
):
    """List virtual machine instances.

        Filter and sort list by name, ip address dns or path. For example:

        vss compute vm ls -f name VM -s -o name

    """
    query = dict()
    if summary:
        query['summary'] = 1
    if filter:
        for f in filter:
            query[f[0]] = f[1]
    if sort:
        query['sort'] = sort
    # get templates
    obj = ctx.get_vms(**query)
    # including additional attributes?
    if summary:
        columns = ctx.columns or const.COLUMNS_VM
        for t in obj:
            t['folder'] = '{parent} > {name}'.format(
                **t['folder']
            )
    else:
        columns = ctx.columns or const.COLUMNS_VM_MIN
    # format output
    output = format_output(
        ctx,
        obj,
        columns=columns
    )
    # page
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@compute_vm.group(
    'get',
    short_help='Given virtual machine info.',
    invoke_without_command=True
)
@click.argument(
    'uuid',
    type=click.UUID,
    required=True)
@pass_context
def compute_vm_get(
        ctx: Configuration,
        uuid
):
    """Obtain virtual machine summary and other attributes."""
    ctx.uuid = uuid
    if click.get_current_context().invoked_subcommand is None:
        columns = ctx.columns or const.COLUMNS_VM_INFO
        obj = ctx.get_vm(uuid)
        if not obj:
            raise VssCliError('Virtual Machine not found')
        click.echo(
            format_output(
                ctx,
                [obj],
                columns=columns,
                single=True
            )
        )


@compute_vm_get.command(
    'admin',
    short_help='Admin (metadata)'
)
@pass_context
def compute_vm_get_admin(
        ctx: Configuration,
        ):
    """Virtual machine administrator. Part of the
    VSS metadata."""
    columns = ctx.columns or const.COLUMNS_VM_ADMIN
    obj = ctx.get_vm_vss_admin(ctx.uuid)
    if not obj:
        raise VssCliError('Virtual Machine Admin not found')
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'alarm',
    short_help='Triggered alarms'
)
@click.argument(
    'moref',
    type=click.STRING,
    required=False
)
@pass_context
def compute_vm_get_alarms(
        ctx: Configuration, moref
):
    """Virtual machine triggered alarms"""
    if moref:
        columns = ctx.columns or const.COLUMNS_VM_ALARM
        obj = ctx.get_vm_alarm(
            ctx.uuid, moref)
        if not obj:
            raise VssCliError('Virtual Machine Alarm not found')
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns,
                single=True
            )
        )
    else:
        columns = ctx.columns or const.COLUMNS_VM_ALARM
        obj = ctx.get_vm_alarms(ctx.uuid)
        if not obj:
            raise VssCliError('Virtual Machine Alarms not found')
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )

