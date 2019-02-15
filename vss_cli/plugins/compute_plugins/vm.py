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


@compute_vm_get.command(
    'boot',
    short_help='Boot configuration'
)
@pass_context
def compute_vm_get_boot(
        ctx: Configuration,
):
    """Virtual machine boot settings.
       Including boot delay and whether or not
       to boot and enter directly to BIOS."""
    columns = ctx.columns or const.COLUMNS_VM_BOOT
    obj = ctx.get_vm_boot(ctx.uuid)
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
    'cd',
    short_help='CD/DVD configuration'
)
@click.argument(
    'unit', type=int, required=False
)
@pass_context
def compute_vm_get_cds(
        ctx: Configuration, unit
):
    """Virtual machine CD/DVD configuration."""
    if unit:
        obj = ctx.get_vm_cd(ctx.uuid, unit)
        if not obj:
            raise VssCliError('CD/DVD could not be found')
        columns = ctx.columns or const.COLUMNS_VM_CD
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns,
                single=True
            )
        )
    else:
        devs = ctx.get_vm_cds(ctx.uuid)
        obj = [d.get('data') for d in devs]
        columns = ctx.columns or const.COLUMNS_VM_CD_MIN
        if not obj:
            raise VssCliError('Virtual Machine CD not found')
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )


@compute_vm_get.command(
    'client',
    short_help='Client (Metadata)'
)
@pass_context
def compute_vm_get_client(ctx: Configuration):
    """Get current virtual machine client/billing department.
    Part of the VSS metadata.
    """
    obj = ctx.get_vm_vss_client(ctx.uuid)
    columns = ctx.columns or [('VALUE', 'value')]
    if not obj:
        raise VssCliError('Virtual Machine Client not found')
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'client-note',
    short_help='Client note (Metadata)'
)
@pass_context
def compute_vm_get_client_notes(ctx):
    """Virtual machine client notes. Part of the
    VM metadata."""
    obj = ctx.get_vm_notes(ctx.uuid)
    columns = ctx.columns or [('VALUE', 'value')]
    if not obj:
        raise VssCliError('Virtual Machine Note not found')
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'console',
    short_help='HTML console link'
)
@click.option(
    '-l', '--launch', is_flag=True,
    help='Launch link in default browser'
)
@pass_context
def compute_vm_get_console(
        ctx: Configuration,
        launch
):
    """'Get one-time HTML link to access console"""
    username = ctx.username or click.prompt(
        'Username',
        default=os.environ.get('VSS_USER', '')
    )
    password = ctx.password or click.prompt(
        'Password',
        default=os.environ.get('VSS_USER_PASSWORD', ''),
        show_default=False, hide_input=True,
        confirmation_prompt=True
    )
    auth = (username.decode(), password.decode())
    obj = ctx.get_vm_console(
        ctx.uuid,
        auth=auth
    )
    link = obj.get('value')
    # print
    columns = ctx.columns or [('VALUE', 'value')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )
    # launch
    if launch:
        click.launch(link)


@compute_vm_get.command(
    'consolidate',
    short_help='Consolidation requirement'
)
@pass_context
def compute_vm_get_consolidate(ctx):
    """Virtual Machine disk consolidation status."""
    obj = ctx.get_vm_consolidation(ctx.uuid)
    columns = ctx.columns or [('REQUIRE', 'requireDiskConsolidation')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.group(
    'controller',
    invoke_without_command=True
)
@pass_context
def compute_vm_get_controllers(
        ctx: Configuration
):
    """Controllers (IDE, SCSI, etc.)"""
    if click.get_current_context().invoked_subcommand is None:
        obj = ctx.get_vm_controllers(ctx.uuid)
        if not obj:
            raise VssCliError('No Controllers found')
        columns = ctx.columns or [('SCSI', 'scsi.count')]
        click.echo(
            format_output(
                ctx,
                [obj],
                columns=columns,
                single=True
            )
        )


@compute_vm_get_controllers.command(
    'scsi',
    short_help='SCSI adapters'
)
@click.argument(
    'bus', type=int, required=False
)
@click.option(
    '--disks', '-d',
    help='include disks attached',
    is_flag=True
)
@pass_context
def compute_vm_get_controller_scsi(
        ctx: Configuration, bus, disks
):
    """Virtual machine SCSI controllers and attached disks"""
    if bus is None:
        obj = ctx.get_vm_controllers_scsi(ctx.uuid)
        columns = ctx.columns or const.COLUMNS_VM_CTRL_MIN
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )
    else:
        obj = ctx.get_vm_controller_scsi(
            ctx.uuid, bus, disks
        )
        if disks:
            obj = obj.get('devices', [])
            columns = ctx.columns or const.COLUMNS_VM_CTRL_DISK
            click.echo(
                format_output(
                    ctx,
                    obj,
                    columns=columns
                )
            )
        else:
            columns = ctx.columns or const.COLUMNS_VM_CTRL
            click.echo(
                format_output(
                    ctx,
                    [obj],
                    columns=columns,
                    single=True
                )
            )


@compute_vm_get.command(
    'cpu',
    short_help='CPU configuration'
)
@pass_context
def compute_vm_get_cpu(ctx: Configuration):
    """Virtual machine cpu configuration.
    Get CPU count and quick stats."""
    columns = ctx.columns or const.COLUMNS_VM_CPU
    obj = ctx.get_vm_cpu(ctx.uuid)
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'description',
    short_help='Description (Metadata)'
)
@pass_context
def compute_vm_get_description(ctx: Configuration):
    """Virtual machine description. Part of the
    VSS metadata."""
    obj = ctx.get_vm_vss_description(ctx.uuid)
    # print
    columns = ctx.columns or [('VALUE', 'value')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'disk',
    short_help='Disk configuration'
)
@click.argument(
    'unit', type=int, required=False
)
@click.option(
    '--backing', '-b',
    help='include backing info',
    is_flag=True
)
@pass_context
def compute_vm_get_disks(
        ctx: Configuration, unit, backing
):
    """Virtual machine Disk configuration."""
    if unit:
        obj = ctx.get_vm_disk(ctx.uuid, unit)
        if not obj:
            raise VssCliError('Disk not found')
        if backing:
            columns = ctx.columns or const.COLUMNS_VM_DISK_BACKING
            _obj = ctx.get_vm_disk_backing(ctx.uuid, unit)
            obj[0].update(_obj)
        else:
            columns = ctx.columns or const.COLUMNS_VM_DISK

        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns,
                single=True
            )
        )
    else:
        obj = ctx.get_vm_disks(ctx.uuid)
        if not obj:
            raise VssCliError('Disks not found')
        obj = [d.get('data') for d in obj]
        columns = ctx.columns or const.COLUMNS_VM_DISK_MIN
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )


@compute_vm_get.command(
    'domain',
    short_help='Running domain'
)
@pass_context
def compute_vm_get_domain(ctx: Configuration):
    """Virtual machine running domain"""
    obj = ctx.get_vm_domain(ctx.uuid)
    columns = ctx.columns or [('MOREF', 'domain.moref'),
                              ('NAME', 'domain.name')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'event',
    short_help='Events'
)
@click.option(
    '-w', '--window', type=int, default=1,
    help='Time window')
@pass_context
def compute_vm_get_events(ctx: Configuration, window):
    """Get virtual machine related events in given time window"""
    obj = ctx.request(f'/vm/{ctx.uuid}/event',
                      params=dict(hours=window))
    obj = obj.get('data')
    columns = ctx.columns or const.COLUMNS_VM_EVENT
    click.echo(
        format_output(
            ctx,
            obj,
            columns=columns
        )
    )


@compute_vm_get.command(
    'extra-config',
    short_help='GuestInfo extra configs'
)
@pass_context
def compute_vm_get_extra_config(ctx: Configuration):
    """Get virtual machine guest info via VMware Tools."""
    obj = ctx.get_vm_extra_config(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_DEFAULT
    click.echo(
        format_output(
            ctx,
            obj,
            columns=columns
        )
    )


@compute_vm_get.command(
    'floppy',
    short_help='Floppy configuration'
)
@click.argument(
    'unit', type=int, required=False
)
@pass_context
def compute_vm_get_floppies(
        ctx: Configuration, unit
):
    """Virtual machine Floppy configuration."""
    if unit:
        obj = ctx.get_vm_floppy(ctx.uuid, unit)
        if not obj:
            raise VssCliError('Floppy could not be found')
        columns = ctx.columns or const.COLUMNS_VM_CD
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns,
                single=True
            )
        )
    else:
        devs = ctx.get_vm_floppies(ctx.uuid)
        obj = [d.get('data') for d in devs]
        columns = ctx.columns or const.COLUMNS_VM_CD_MIN
        if not obj:
            raise VssCliError('Virtual Machine Floppy not found')
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )
