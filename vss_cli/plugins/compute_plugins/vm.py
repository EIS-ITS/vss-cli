import click
import logging
import os

from vss_cli import const
from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.helper import (
    format_output, to_tuples,
)
from vss_cli.validators import (
    validate_phone_number, validate_email
)
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
        obj = obj or []
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
        obj = obj or []
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
    obj = obj or {}
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
        if obj:
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
            logging.error('Unit does not exist')
    else:
        devs = ctx.get_vm_cds(ctx.uuid)
        obj = [d.get('data') for d in devs] if devs else []
        columns = ctx.columns or const.COLUMNS_VM_CD_MIN
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
    obj = obj or {}
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
    obj = obj or {}
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
        obj = obj or {}
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
        if obj:
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
            logging.error('Unit does not exist')
    else:
        obj = ctx.get_vm_disks(ctx.uuid)
        obj = [d.get('data') for d in obj] if obj else []
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
        if obj:
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
            logging.error('Unit does not exist')
    else:
        devs = ctx.get_vm_floppies(ctx.uuid)
        obj = [d.get('data') for d in devs] if devs else []
        columns = ctx.columns or const.COLUMNS_VM_CD_MIN
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )


@compute_vm_get.command(
    'folder',
    short_help='Logical folder'
)
@pass_context
def compute_vm_get_folder(ctx: Configuration):
    """Virtual machine logical folder."""
    obj = ctx.get_vm_folder(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_FOLDER
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.group(
    'guest',
    short_help='Guest summary',
    invoke_without_command=True
)
@pass_context
def compute_vm_get_guest(ctx: Configuration):
    """Get virtual machine guest info via VMware Tools."""
    obj = ctx.get_vm_guest(ctx.uuid)
    if click.get_current_context().invoked_subcommand is None:
        columns = ctx.columns or const.COLUMNS_VM_GUEST
        click.echo(
            format_output(
                ctx,
                [obj],
                columns=columns,
                single=True
            )
        )


@compute_vm_get_guest.command(
    'os',
    short_help='Guest OS configuration'
)
@pass_context
def compute_vm_get_guest_os(ctx: Configuration):
    """Get virtual machine guest OS."""
    obj = ctx.get_vm_guest_os(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_VM_GUEST_OS
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get_guest.command(
    'ip',
    short_help='Guest IP Address configuration'
)
@pass_context
def compute_vm_get_guest_ip(ctx: Configuration):
    """Get virtual machine ip addresses via VMware Tools."""
    obj = ctx.get_vm_guest_ip(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_VM_GUEST_IP
    click.echo(
        format_output(
            ctx,
            obj,
            columns=columns
        )
    )


@compute_vm_get.command(
    'ha-group',
    short_help='HA Group (Metadata)'
)
@pass_context
def compute_vm_get_ha_group(ctx: Configuration):
    obj = ctx.get_vm_vss_ha_group(ctx.uuid)
    if obj:
        obj = obj.get('vms', [])
    else:
        obj = []
    columns = ctx.columns or const.COLUMNS_VM_HAGROUP
    click.echo(
        format_output(
            ctx,
            obj,
            columns=columns
        )
    )


@compute_vm_get.command(
    'inform',
    short_help='Informational contacts (Metadata)'
)
@pass_context
def compute_vm_get_inform(ctx: Configuration):
    """Virtual machine informational contacts. Part of the
    VSS metadata."""
    obj = ctx.get_vm_vss_inform(ctx.uuid)
    if obj:
        obj = dict(inform=obj)
    columns = ctx.columns or [('INFORM', 'inform.[*]')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'memory',
    short_help='Memory configuration'
)
@pass_context
def compute_vm_get_memory(ctx: Configuration):
    """Virtual machine memory configuration."""
    obj = ctx.get_vm_memory(str(ctx.uuid))
    columns = ctx.columns or const.COLUMNS_VM_MEMORY
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'name',
    short_help='Logical name'
)
@pass_context
def compute_vm_get_name(ctx: Configuration):
    """Virtual machine human readable name."""
    obj = ctx.get_vm_name(ctx.uuid)
    columns = ctx.columns or [('NAME', 'name')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'nic',
    short_help='NIC configuration'
)
@click.argument(
    'unit', type=int, required=False
)
@pass_context
def compute_vm_get_nics(
        ctx: Configuration, unit
):
    """Virtual machine network interface adapters configuration."""

    if unit:
        obj = ctx.get_vm_nic(ctx.uuid, unit)
        if obj:
            columns = ctx.columns or const.COLUMNS_VM_NIC
            click.echo(
                format_output(
                    ctx,
                    obj,
                    columns=columns,
                    single=True
                )
            )
        else:
            logging.error('Unit does not exist')
    else:
        obj = ctx.get_vm_nics(ctx.uuid)
        obj = [d.get('data') for d in obj] if obj else []
        columns = ctx.columns or const.COLUMNS_VM_NIC_MIN
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )


@compute_vm_get.command(
    'perm',
    short_help='Permissions'
)
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def compute_vm_get_perms(ctx: Configuration, page):
    """Obtain virtual machine group or user permissions."""
    obj = ctx.get_vm_permission(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_OBJ_PERMISSION
    click.echo(
        format_output(
            ctx,
            obj,
            columns=columns
        )
    )


@compute_vm_get.command(
    'snapshot',
    short_help='Snapshots'
)
@click.argument(
    'snapshot_id', type=int,
    required=False
)
@pass_context
def compute_vm_get_snapshot(
        ctx: Configuration, snapshot_id
):
    """Virtual Machine snapshots"""
    if snapshot_id:
        obj = ctx.get_vm_snapshot(ctx.uuid, snapshot_id)
        columns = ctx.columns or const.COLUMNS_VM_SNAP
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns,
                single=True
            )
        )
    else:
        obj = ctx.get_vm_snapshots(ctx.uuid)
        columns = ctx.columns or const.COLUMNS_VM_SNAP_MIN
        click.echo(
            format_output(
                ctx,
                obj,
                columns=columns
            )
        )


@compute_vm_get.command(
    'spec',
    short_help='Configuration specification',
    context_settings={"ignore_unknown_options": True}
)
@click.argument(
    'spec_file', type=click.Path(),
    required=False,
)
@pass_context
def compute_vm_get_spec(
        ctx: Configuration,
        spec_file
):
    """Virtual machine configuration specification."""
    import json
    obj = ctx.get_vm_spec(ctx.uuid)
    f_name = spec_file or f'{ctx.uuid}.json'
    with open(f_name, 'w') as fp:
        json.dump(obj, fp=fp)
    click.echo(f'Written to {f_name}')


@compute_vm_get.command(
    'state',
    short_help='Power state'
)
@pass_context
def compute_vm_get_state(ctx: Configuration):
    """Virtual machine running and power state."""
    obj = ctx.get_vm_state(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_VM_STATE
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'stats',
    short_help='Performance statistics'
)
@click.argument(
    'kind',
    type=click.Choice(
        ['memory', 'io',
         'cpu', 'net']
    )
)
@pass_context
def compute_vm_get_stats(ctx: Configuration, kind):
    """Get virtual machine memory, io, cpu and network
     performance statistics. Choose between: io, memory,
     cpu or net. For example:

    vss compute vm get <uuid> stats memory
    """
    lookup = {'cpu': ctx.get_vm_performance_cpu,
              'memory': ctx.get_vm_performance_memory,
              'io': ctx.get_vm_performance_io,
              'net': ctx.get_vm_performance_net}

    if not ctx.is_powered_on_vm(ctx.uuid):
        raise VssCliError(
            'Cannot perform operation in '
            'current power state'
        )
    obj = lookup[kind](ctx.uuid)
    columns = ctx.columns or [
        (i.upper(), i) for i in obj.keys()
    ]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'template',
    short_help='Template configuration'
)
@pass_context
def compute_vm_get_template(ctx: Configuration):
    """Virtual machine template state."""
    obj = ctx.is_vm_template(ctx.uuid)
    columns = ctx.columns or [
        ('ISTEMPLATE', 'isTemplate')
    ]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'tools',
    short_help='VMware Tools Status'
)
@pass_context
def compute_vm_get_tools(ctx: Configuration):
    """Virtual machine VMware Tools status."""
    obj = ctx.get_vm_tools(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_VM_TOOLS
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'usage',
    short_help='Usage (Metadata)'
)
@pass_context
def compute_vm_get_usage(ctx: Configuration):
    """Get current virtual machine usage.

    Part of the VSS metadata and the name prefix (YYMMP-) is composed
    by the virtual machine usage, which is intended to specify
    whether it will be hosting a Production, Development,
    QA, or Testing system."""
    obj = ctx.get_vm_vss_usage(ctx.uuid)
    columns = ctx.columns or [('USAGE', 'value')]
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_get.command(
    'version',
    short_help='Hardware (VMX) version'
)
@pass_context
def compute_vm_get_version(ctx: Configuration):
    """Get VMX hardware version"""
    obj = ctx.get_vm_version(ctx.uuid)
    columns = ctx.columns or const.COLUMNS_VM_HW
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm.group(
    'set',
    short_help='Set virtual machine attribute',
    invoke_without_command=True
)
@click.argument(
    'uuid',
    type=click.UUID,
    required=True)
@click.option(
    '-s', '--schedule',
    type=click.DateTime(formats=[const.DEFAULT_DATETIME_FMT]),
    required=False, default=None,
    help='Schedule change in a given point in time based'
         ' on format YYYY-MM-DD HH:MM.'
)
@click.option(
    '-u', '--user-meta',
    help='User metadata in key=value format. '
         'These tags are stored in the request.',
    required=False, default=None
)
@pass_context
def compute_vm_set(
        ctx: Configuration,
        uuid, schedule, user_meta: str
):
    """Set given virtual machine attribute such as cpu,
    memory, disk, network backing, cd, etc.."""
    ctx.uuid = uuid
    ctx.payload_options = dict()
    ctx.user_meta = dict(to_tuples(user_meta))
    ctx.schedule = schedule
    if user_meta:
        ctx.payload_options['user_meta'] = ctx.user_meta
    if schedule:
        ctx.payload_options['schedule'] = ctx.schedule


@compute_vm_set.command(
    'admin',
    short_help='Administrator'
)
@click.argument(
    'name', type=click.STRING, required=True
)
@click.argument(
    'email', type=click.STRING, required=True,
    callback=validate_email
)
@click.argument(
    'phone', type=click.STRING, required=True,
    callback=validate_phone_number
)
@pass_context
def compute_vm_set_admin(
        ctx: Configuration, name, email, phone
):
    """Set or update virtual machine administrator in metadata.

    vss compute vm set <uuid> admin "Admin Name"
    admin.email@utoronto.ca 416-666-6666
    """
    payload = dict(
        name=name,
        phone=phone,
        email=email,
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # process request
    obj = ctx.update_vm_vss_admin(**payload)
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )
