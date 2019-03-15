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
    validate_phone_number, validate_email,
    validate_json_type
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
    if not ctx.get_vm(uuid):
        raise click.BadArgumentUsage(
            'uuid should be an existing Virtual Machine'
        )
    ctx.uuid = uuid
    ctx.payload_options = dict()
    ctx.user_meta = dict(to_tuples(user_meta))
    ctx.schedule = schedule
    if user_meta:
        ctx.payload_options['user_meta'] = ctx.user_meta
    if schedule:
        ctx.payload_options['schedule'] = ctx.schedule
    if click.get_current_context().invoked_subcommand is None:
        raise click.UsageError(
            'Sub command is required'
        )


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
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'alarm',
    short_help='Acknowledge or clear alarms'
)
@click.argument(
    'alarm_moref', type=click.STRING, required=True
)
@click.option(
    '-a', '--action', type=click.Choice(['ack', 'cl']),
    help='Action to perform', required=True
)
@pass_context
def compute_vm_set_alarm(
        ctx: Configuration, action, alarm_moref
):
    """Acknowledge or clear a given alarm. Obtain alarm moref by:

        vss compute vm get <uuid> alarm

        vss compute vm set <uuid> alarm <moref> --action ack

    """
    payload = dict(
        uuid=ctx.uuid,
        moref=alarm_moref
    )
    # add common options
    payload.update(ctx.payload_options)
    # action
    if action == 'ack':
        obj = ctx.ack_vm_alarm(**payload)
    else:
        obj = ctx.clear_vm_alarm(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'boot-bios',
    short_help='Enable or disable Boot to BIOS'
)
@click.option(
    '--on/--off',
    is_flag=True,
    help='Enable/Disable boot to BIOS',
    default=False)
@pass_context
def compute_vm_set_boot_bios(
        ctx: Configuration,
        on
):
    """Update virtual machine boot configuration to
    boot directly to BIOS.

    vss compute vm set <uuid> boot-bios --on
    vss compute vm set <uuid> boot-bios --off
    """
    payload = dict(
        uuid=ctx.uuid,
        boot_bios=on
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_boot_bios(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'boot-delay',
    short_help='Boot delay in milliseconds'
)
@click.argument(
    'delay-in-ms', type=click.INT,
    required=True
)
@pass_context
def compute_vm_set_boot_delay(
        ctx: Configuration,
        delay_in_ms
):
    """Update virtual machine boot delay time (ms).

    vss compute vm set <uuid> boot-delay 5000
    """
    payload = dict(
        uuid=ctx.uuid,
        boot_delay_ms=delay_in_ms
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_boot_delay(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'cd',
    short_help='CD/DVD backing'
)
@click.argument(
    'unit', type=click.INT,
    required=True
)
@click.option(
    '-i', '--iso', type=click.STRING,
    required=True,
    help='Update CD/DVD backing device '
         'to given ISO path or Client device.'
)
@pass_context
def compute_vm_set_cd(
        ctx: Configuration, unit, iso
):
    """Update virtual machine CD/DVD backend to ISO or client.

    vss compute vm set <uuid> cd <unit> --iso "<name-or-path-or-id>"

    vss compute vm set <uuid> cd <unit> --iso client
    """
    iso_ref = {}
    user_isos = ctx.get_user_isos()
    try:
        iso_id = int(iso)
        # public or user
        iso_ref = ctx.get_isos(filter=f'id,eq,{iso_id}') \
            or list(filter(lambda i: i['id'] == iso_id, user_isos))
    except ValueError as ex:
        # not an integer
        _LOGGING.debug(f'iso is not an id {iso_ref}')
        # checking name or path
        # check in public and user isos
        iso_ref = ctx.get_isos(filter=f'name,like,%{iso}%') \
            or ctx.get_isos(filter=f'path,like,%{iso}%') \
            or list(filter(lambda i: i['name'] == iso, user_isos)) \
            or list(filter(lambda i: i['path'] == iso, user_isos))

    # no iso ref
    if not iso_ref:
        raise click.BadParameter(
            '--iso/-i should be a valid name, path or id'
        )
    _LOGGING.debug(f'Will mount {iso_ref}')
    # generate payload
    payload = dict(
        uuid=ctx.uuid,
        unit=unit,
        iso=iso_ref[0].get('path')
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_cd(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'client',
    short_help='Client (Metadata)'
)
@click.argument(
    'client', type=click.STRING,
    required=True
)
@pass_context
def compute_vm_set_client(
        ctx: Configuration,
        client
):
    """Update virtual machine client/billing department.

    vss compute vm set <uuid> client <New-Client>
    """
    # generate payload
    payload = dict(
        uuid=ctx.uuid,
        value=client
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_vss_client(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'client-note',
    short_help='Client note (Metadata)'
)
@click.argument(
    'notes',
    required=True
)
@click.option(
    '--replace', '-r', is_flag=True,
    required=False,
    help="Whether to replace existing value."
)
@pass_context
def compute_vm_set_client_note(
        ctx: Configuration, notes, replace
):
    """Set or update virtual machine client notes
     in metadata.

     vss compute vm set <uuid> client-note "New note"
     """
    if not replace:
        _old_notes = ctx.get_vm_notes(
            ctx.uuid
        )
        old_notes = _old_notes.get('value') or ""
        notes = "{}\n{}".format(old_notes, notes)
    # generate payload
    payload = dict(
        uuid=ctx.uuid,
        notes=notes
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_notes(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'consolidate',
    short_help='Disk consolidation'
)
@pass_context
def compute_vm_set_consolidate(
        ctx: Configuration
):
    """Perform virtual machine disk consolidation

    vss compute vm set --schedule <timestamp> <uuid> consolidate
    """
    # generate payload
    payload = dict(
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.consolidate_vm_disks(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'cpu'
)
@pass_context
def compute_vm_set_cpu(
        ctx: Configuration
):
    """Update virtual machine CPU count and settings
    """
    pass


@compute_vm_set_cpu.command(
    'count',
    short_help='Update CPU count'
)
@click.argument(
    'cpu_count', type=click.INT,
    required=True
)
@click.pass_context
def compute_vm_set_cpu_count(
        ctx: Configuration,
        cpu_count
):
    # generate payload
    payload = dict(
        uuid=ctx.uuid,
        number=cpu_count
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.set_vm_cpu(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_cpu.command(
    'hot-add',
    short_help='Enable/disable CPU hot add'
)
@click.argument(
    'status', type=click.Choice(['on', 'off']),
    required=True
)
@pass_context
def compute_vm_set_cpu_hot_add(
        ctx: Configuration, status
):
    lookup = {'on': True, 'off': False}
    payload = dict(
        uuid=ctx.uuid,
        hot_add=lookup[status]
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_cpu_hot_add(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'custom-spec',
    short_help='Custom specification'
)
@click.option(
    '--hostname', '-h', type=click.STRING,
    required=True, help='OS hostname.'
)
@click.option(
    '--domain', '-m', type=click.STRING,
    required=True, help='OS domain.'
)
@click.option(
    '--dns', '-n', type=click.STRING,
    multiple=True,
    required=False, help='DNS list.'
)
@click.option(
    '--interface', '-i', type=click.STRING,
    required=False, multiple=True,
    help='Interfaces to customize in json format.'
)
@pass_context
def compute_vm_set_custom_spec(
        ctx: Configuration,
        hostname, domain,
        dns, interface
):
    """Set up Guest OS customization specification.
    Virtual machine power state require is powered off."""
    if ctx.is_powered_on_vm(
        ctx.uuid
    ):
        raise Exception(
            'Cannot perform operation '
            'on VM with current power state'
        )
    # temp custom_spec
    _custom_spec = dict(
        hostname=hostname,
        domain=domain
    )
    if dns:
        _custom_spec['dns'] = dns
    interfaces = list()
    # interfaces
    if interface:
        import json
        for iface in interface:
            validate_json_type(ctx, '', iface)
            _if = json.loads(iface)
            interfaces.append(
                ctx.get_custom_spec_interface(**_if)
            )
    else:
        _LOGGING.warning('No interfaces were received from input')
    # update custom spec with interfaces
    _custom_spec.update(
        {'interfaces': interfaces}
    )
    # create custom_spec
    custom_spec = ctx.get_custom_spec(**_custom_spec)
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        custom_spec=custom_spec
    )
    # add common options
    payload.update(ctx.payload_options)
    # process request
    # submit custom_spec
    obj = ctx.create_vm_custom_spec(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'description',
    short_help='Description (Metadata)'
)
@click.argument(
    'description',
    required=True
)
@pass_context
def compute_vm_set_description(
        ctx: Configuration, description
):
    """Set or update virtual machine description in metadata.

    vss compute vm set <uuid> description "This is a new description"
    """
    payload = dict(
        uuid=ctx.uuid,
        description=description
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_vss_description(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'disk',
    short_help='Disk management'
)
@pass_context
def compute_vm_set_disk(
        ctx: Configuration
):
    """Manage virtual machine disks.
     Add, expand and remove virtual disks."""
    pass


@compute_vm_set_disk.command(
    'mk',
    short_help='Create new disk(s)'
)
@click.option(
    '-c', '--capacity', type=click.INT,
    required=True, multiple=True,
    help='Create given disk(s) capacity in GB.'
)
@pass_context
def compute_vm_set_disk_mk(
        ctx: Configuration, capacity
):
    """Create virtual machine disk:

        vss compute vm set <uuid> disk mk -c 10 -c 40
    """
    payload = dict(
        uuid=ctx.uuid,
        values_in_gb=capacity
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.create_vm_disk(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_disk.command(
    'up',
    short_help='Update disk capacity'
)
@click.argument(
    'unit', type=click.INT, required=True
)
@click.option(
    '-c', '--capacity', type=int,
    required=True,
    help='Update given disk capacity in GB.'
)
@pass_context
def compute_vm_set_disk_up(
        ctx: Configuration,
        unit, capacity
):
    """Update virtual machine disk capacity:

        vss compute vm set <uuid> disk up --capacity 30 <unit>
    """
    payload = dict(
        uuid=ctx.uuid,
        disk=unit,
        valueGB=capacity
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_disk_capacity(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_disk.command(
    'rm',
    short_help='Remove disk from vm'
)
@click.argument(
    'unit', type=click.INT,
    required=True, nargs=-1
)
@click.option(
    '-r', '--rm',
    is_flag=True, default=False,
    help='Confirm disk removal'
)
@pass_context
def compute_vm_set_disk_rm(
        ctx: Configuration, unit, rm
):
    """Remove virtual machine disks. Warning: data will be lost:

        vss compute vm set <uuid> disk rm <unit> <unit> ...
    """
    payload = dict(
        uuid=ctx.uuid,
        units=list(unit)
    )
    # add common options
    payload.update(ctx.payload_options)
    # confirm
    confirm = rm or click.confirm(
        f'Are you sure you want to delete disk unit {unit}?'
    )
    if confirm:
        obj = ctx.delete_vm_disks(**payload)
    else:
        raise click.ClickException('Cancelled by user.')
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'domain',
    short_help='Domain migration'
)
@click.argument(
    'domain_moref', type=click.STRING,
    required=True
)
@click.option(
    '-f', '--force', is_flag=True,
    help='Shut down or power off before migration.'
)
@click.option(
    '-o', '--on', is_flag=True,
    help='Power of after migrating'
)
@pass_context
def compute_vm_set_domain(
        ctx: Configuration,
        domain_moref, force, on
):
    """Migrate a virtual machine to another fault domain.
    In order to proceed with the virtual machine relocation,
    it's required to be in a powered off state. The `force` flag
    will send a shutdown signal anf if times out, will perform a
    power off task. After migration completes, the `on` flag
    indicates to power on the virtual machine.

    vss compute vm set <uuid> domain <domain-moref> --force --on
    """
    payload = dict(
        uuid=ctx.uuid,
        moref=domain_moref,
        poweron=on, force=force
    )
    if not ctx.get_domain(domain_moref):
        raise click.BadArgumentUsage(
            f'Domain {domain_moref} does not exist'
        )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_domain(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'export',
    short_help='Export to OVF'
)
@pass_context
def compute_vm_set_export(
        ctx: Configuration
):
    """Export current virtual machine to OVF.

    vss compute vm set <uuid> export
    """
    payload = dict(
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.export_vm(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'floppy',
    short_help='Floppy backing'
)
@click.argument(
    'unit', type=click.INT,
    required=True
)
@click.option(
    '-i', '--image', type=click.STRING,
    required=True,
    help='Update floppy backing device to'
         ' given flp image path.'
)
@pass_context
def compute_vm_set_floppy(
        ctx: Configuration, unit, image
):
    """Update virtual machine floppy backend to Image or client"""
    img_ref = {}
    user_imgs = ctx.get_user_floppies()
    try:
        img_id = int(image)
        # public or personal
        img_ref = ctx.get_floppies(filter=f'id,eq,{img_id}') \
            or list(filter(lambda i: i['id'] == img_id, user_imgs))
    except ValueError as ex:
        # not an integer
        _LOGGING.debug(f'iso is not an id {img_ref}')
        # checking name or path
        # check in public and user images
        img_ref = ctx.get_floppies(filter=f'name,like,%{image}%') \
            or ctx.get_floppies(filter=f'path,like,%{image}%') \
            or list(filter(lambda i: i['name'] == image, user_imgs)) \
            or list(filter(lambda i: i['path'] == image, user_imgs))
    # no iso ref
    if not img_ref:
        raise click.BadParameter(
            '--image/-i should be a valid name, path or id'
        )
    _LOGGING.debug(f'Will mount {img_ref}')
    # generate payload
    payload = dict(
        uuid=ctx.uuid,
        floppy=unit,
        image=img_ref[0].get('path')
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_floppy(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'folder',
    short_help='Logical folder'
)
@click.argument(
    'moref', type=click.STRING,
    required=True
)
@pass_context
def compute_vm_set_folder(
        ctx: Configuration, moref
):
    """Move vm from logical folder. Get folder moref from:

        vss compute folder ls

    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        folder_moId=moref
    )
    if not ctx.get_folder(moref):
        raise click.BadArgumentUsage(
            f'Folder {moref} does not exist'
        )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_folder(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'guest-cmd',
    short_help='Execute command on OS host'
)
@click.option(
    '-u', '--username',
    help='Guest Operating System username or via '
         'environment variable VSS_CMD_USER',
    envvar='VSS_CMD_USER'
)
@click.option(
    '-p', '--password',
    help='Guest Operating System username password or via '
         'environment variable VSS_CMD_USER_PASS',
    envvar='VSS_CMD_USER_PASS'
)
@click.option(
    '-e', '--env',  multiple=True,
    help='Environment variables in KEY=value format.'
)
@click.argument(
    'cmd', type=click.STRING,
    required=True
)
@click.argument(
    'cmd-args', type=click.STRING,
    required=True
)
@pass_context
def compute_vm_set_guest_cmd(
        ctx, cmd, cmd_args,
        env, username, password
):
    """
    Execute a command in the Guest Operating system.

    vss compute vm set <uuid> guest-cmd "/bin/echo"
    "Hello > /tmp/hello.txt"

    Note: VMware Tools must be installed and running.
    """
    username = username or click.prompt('Username')
    password = password or click.prompt(
        'Password',
        show_default=False, hide_input=True,
        confirmation_prompt=True
    )
    # check vmware tools status
    vmt = ctx.get_vm_tools(ctx.uuid)
    if not vmt:
        raise click.BadParameter(
            f'VMware Tools status could '
            f'not be checked on {ctx.uuid} '
        )
    if vmt.get('runningStatus') not in ["guestToolsRunning"]:
        raise click.BadParameter(
            f'VMware Tools must be running '
            f'on {ctx.uuid} to execute cmd.'
        )
    # creating payload
    payload = dict(
        uuid=ctx.uuid, user=username,
        pwd=password, cmd=cmd,
        arg=cmd_args, env=env
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.run_cmd_guest_vm(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'guest-os',
    short_help='Update guest operating system'
)
@click.argument(
    'guest-id', type=click.STRING,
    required=True
)
@click.pass_context
def compute_vm_set_guest_os(
        ctx: Configuration, guest_id
):
    """Update guest operating system configuration:

        vss compute os ls -f guestId,like,cent%

        or

        vss compute os ls -f guestFullName,like,Cent%

    """
    if not ctx.get_os(filter=f'guestId,eq,{guest_id}'):
        raise click.BadParameter(
            'OS not found. Please try: "vss compute os ls"'
        )
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        os=guest_id
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_os(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'ha-group',
    short_help='HA Group (Metadata)'
)
@click.argument(
    'uuid', type=click.UUID, nargs=-1,
    required=True
)
@click.option(
    '-r', '--replace', is_flag=True,
    required=False,
    help='Replace existing value.'
)
@pass_context
def compute_vm_set_ha_group(
        ctx: Configuration, uuid, replace
):
    """Create HA group by tagging virtual machines with given
    virtual machine UUIDs.

    Checks will run every 3 hours to validate virtual machine
    association and domain separation.

    vss compute vm set <uuid> ha-group --replace <uuid-1> <uuid-n>
    """
    for vm in uuid:
        _vm = ctx.get_vm(vm)
        if not vm:
            raise click.BadArgumentUsage(
                f'{vm} could not be found'
            )
    # create payload
    payload = dict(
        append=not replace,
        vms=list(map(str, uuid)),
        uuid=str(ctx.uuid)
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_vss_ha_group(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'inform',
    short_help='Informational contacts (Metadata)'
)
@click.argument(
    'email', type=click.STRING,
    nargs=-1, required=True
)
@click.option(
    '-r', '--replace', is_flag=True,
    required=False,
    help='Replace existing value.'
)
@pass_context
def compute_vm_set_inform(
        ctx: Configuration, email, replace
):
    """Update or set informational contacts emails in
    metadata.

    vss compute vm set <uuid> inform <email-1> <email-n>
    """
    for e in email:
        validate_email(ctx, '', e)
    # create payload
    payload = dict(
        append=not replace,
        emails=list(email),
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_vss_inform(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'memory'
)
@pass_context
def compute_vm_set_memory(ctx: Configuration):
    """Update virtual machine Memory count and settings
    """
    pass


@compute_vm_set_memory.command(
    'size', short_help='Update memory size in GB'
)
@click.argument(
    'memory_gb', type=click.INT,
    required=True
)
@pass_context
def compute_vm_set_memory_size(
        ctx: Configuration, memory_gb
):
    """Update virtual machine memory size in GB.

    vss compute vm set <uuid> memory size <memory_gb>

    """
    # create payload
    payload = dict(
        sizeGB=memory_gb,
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.set_vm_memory(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_memory.command(
    'hot-add',
    short_help='Enable/disable Memory hot add'
)
@click.argument(
    'status', type=click.Choice(['on', 'off']),
    required=True
)
@pass_context
def compute_vm_set_memory_hot_add(
        ctx: Configuration, status
):
    """Enable or disable virtual machine memory hot-add setting

    vss compute vm set <uuid> memory hot-add on|off

    """
    lookup = {'on': True, 'off': False}
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        hot_add=lookup[status]
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_memory_hot_add(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'name',
    short_help='Logical name'
)
@click.argument(
    'name', type=click.STRING,
    required=True
)
@pass_context
def compute_vm_set_name(
        ctx: Configuration, name
):
    """Update virtual machine name only. It does not update
    VSS prefix YYMM{P|D|Q|T}.

    vss compute vm set <uuid> name <new-name>

    """
    payload = dict(
        name=name,
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.rename_vm(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'nic',
    short_help='Network adapter management'
)
@pass_context
def compute_vm_set_nic(ctx: Configuration):
    """Add, remove or update virtual machine network adapters

        vss compute vm set <uuid> nic mk --network <net-moref>

    """
    pass


@compute_vm_set_nic.command(
    'up',
    short_help='Update NIC unit'
)
@click.argument(
    'unit', type=click.INT,
    required=True
)
@click.option(
    '-n', '--network', type=click.STRING,
    help='Virtual network moref'
)
@click.option(
    '-s', '--state',
    type=click.Choice(['connect',
                       'disconnect']),
    help='Updates nic state'
)
@click.option(
    '-a', '--adapter',
    type=click.Choice(['VMXNET2', 'VMXNET3',
                       'E1000', 'E1000e']),
    help='Updates nic adapter type'
)
@pass_context
def compute_vm_set_nic_up(
        ctx: Configuration,
        unit, network, state, adapter
):
    """Update network adapter backing network, type or state

        vss compute vm set <uuid> nic up --adapter VMXNET3 <unit>
        vss compute vm set <uuid> nic up --network <name-or-moref> <unit>
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        nic=unit
    )
    # add common options
    payload.update(ctx.payload_options)
    # process request
    lookup = {
        'network': ctx.update_vm_nic_network,
        'state': ctx.update_vm_nic_state,
        'type': ctx.update_vm_nic_type
    }
    # select attr
    if network:
        networks = ctx.get_networks(summary=1)
        # search by name or moref
        net = list(filter(lambda i: network in i['name'], networks)) \
            or list(filter(lambda i: network in i['moref'], networks))
        net_count = len(net)
        if not net:
            raise click.BadParameter(
                f'{network} could not be found'
            )
        if len(net) > 1:
            raise click.BadParameter(
                f'{network} returned {net_count} results. '
                f'Narrow down by using specific name or moref.'
            )
        attr = 'network'
        value = net[0]['moref']
        _LOGGING.debug(f'Update NIC {unit} to {net}')
    elif state:
        attr = 'state'
        value = state
    elif adapter:
        attr = 'type'
        value = adapter
    else:
        raise click.UsageError(
            'Select at least one setting to change'
        )
    # lookup function to call
    f = lookup[attr]
    payload[attr] = value
    # request
    obj = f(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_nic.command(
    'mk',
    short_help='Create NIC unit'
)
@click.option(
    '-n', '--network', type=click.STRING,
    multiple=True,
    help='Virtual network moref'
)
@pass_context
def compute_vm_set_nic_mk(
        ctx: Configuration, network
):
    """Add network adapter specifying backing network.

        vss compute vm set <uuid> nic mk -n <moref-or-name>
        -n <moref-or-name>
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid
    )
    # add common options
    payload.update(ctx.payload_options)
    # pull networks
    networks = ctx.get_networks()
    _LOGGING.debug(networks)
    networks_payload = []
    for net_name_or_moref in network:
        # search by name or moref
        net = list(filter(lambda i: net_name_or_moref in i['name'], networks)) \
            or list(filter(lambda i: net_name_or_moref in i['moref'], networks))
        if not net:
            _LOGGING.warning(
                f'{net_name_or_moref} could not be found. '
                f'Ignoring.'
            )
        net_count = len(net)
        if len(net) > 1:
            _LOGGING.warning(
                f'{net_name_or_moref} returned {net_count} results. '
                f'Narrow down by using specific name or moref.'
            )
        # adding to payload
        networks_payload.append(net[0]['moref'])
    # payload
    payload['networks'] = networks_payload
    # request
    obj = ctx.create_vm_nic(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_nic.command(
    'rm',
    short_help='Remove NIC unit'
)
@click.argument(
    'unit', type=click.INT,
    required=True, nargs=-1
)
@click.option(
    '-c', '--confirm', is_flag=True,
    default=False,
    help='Confirm nic removal'
)
@pass_context
def compute_vm_set_nic_rm(
        ctx: Configuration,
        unit, confirm
):
    """Remove given network adapters

        vss compute vm set <uuid> nic rm <unit> <unit> ...
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
    )
    units_payload = []
    # add common options
    payload.update(ctx.payload_options)
    confirm_message = list()
    # validate adapters
    for n in unit:
        _nic = ctx.get_vm_nic(
            uuid=ctx.uuid, nic=n
        )
        if _nic:
            _nic = _nic.pop()
            _message = const.DEFAULT_NIC_DEL_MSG.format(
                **_nic
            )
            confirm_message.append(_message)
            units_payload.append(n)
        else:
            _LOGGING.warning(
                f'Adapter {n} could not be found. Ignoring.'
            )
    if not units_payload:
        raise click.BadArgumentUsage(
            'No valid adapters could be found.'
        )
    else:
        payload['units'] = units_payload
    confirm_message.append(
        'Are you sure you want to delete the following NICs'
    )
    confirm_message_str = '\n'.join(confirm_message)
    # confirm message
    confirm = confirm or click.confirm(confirm_message_str)
    # request
    if confirm:
        obj = ctx.delete_vm_nics(**payload)
    else:
        raise click.ClickException('Cancelled by user.')
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'snapshot',
    short_help='Snapshot management'
)
@pass_context
def compute_vm_set_snapshot(
        ctx: Configuration
):
    """Manage virtual machine snapshots. Create, delete and revert
    virtual machine snapshot on a given date and time."""
    if ctx.payload_options.get('schedule'):
        _LOGGING.warning(
            'schedule is ignored for snapshots. Removing.'
        )
        del ctx.payload_options['schedule']


@compute_vm_set_snapshot.command(
    'mk',
    short_help='Create snapshot'
)
@click.option(
    '-d', '--description',
    type=click.STRING, required=True,
    help='A brief description of the snapshot.'
)
@click.option(
    '-t', '--timestamp',
    type=click.DateTime(formats=[const.DEFAULT_DATETIME_FMT]),
    required=True,
    help='Timestamp to create the snapshot from.'
)
@click.option(
    '-l', '--lifetime',
    type=click.IntRange(1, 72), required=True,
    help='Number of hours the snapshot will live.')
@pass_context
def compute_vm_set_snapshot_mk(
        ctx: Configuration,
        description, timestamp, lifetime
):
    """Create virtual machine snapshot:

       vss compute vm set <uuid> snapshot mk -d 'Short description'
       -t '2018-02-22 00:00' -l 72
    """
    import datetime
    payload = dict(
        uuid=ctx.uuid,
        desc=description,
        date_time=datetime.datetime.strftime(
            timestamp, const.DEFAULT_DATETIME_FMT
        ),
        valid=lifetime
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.create_vm_snapshot(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_snapshot.command(
    'rm',
    short_help='Remove snapshot'
)
@click.argument(
    'snapshot_id', type=click.INT, required=True
)
@pass_context
def compute_vm_set_snapshot_rm(
        ctx: Configuration, snapshot_id
):
    """Remove virtual machine snapshot:

        vss compute vm set <uuid> snapshot rm <snapshot-id>
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        snapshot=snapshot_id
    )
    if not ctx.get_vm_snapshot(
            uuid=ctx.uuid, snapshot=snapshot_id
    ):
        raise click.BadArgumentUsage(
            f'Snapshot ID {snapshot_id} could not be found.'
        )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.delete_vm_snapshot(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_snapshot.command(
    're',
    short_help='Revert snapshot'
)
@click.argument(
    'snapshot_id', type=click.INT, required=True
)
@pass_context
def compute_vm_set_snapshot_re(
        ctx: Configuration, snapshot_id
):
    """Revert virtual machine snapshot:

        vss compute vm set <uuid> snapshot re <snapshot-id>
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        snapshot=snapshot_id
    )
    if not ctx.get_vm_snapshot(
            uuid=ctx.uuid, snapshot=snapshot_id
    ):
        raise click.BadArgumentUsage(
            f'Snapshot ID {snapshot_id} could not be found.'
        )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.revert_vm_snapshot(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'state',
    short_help='Power state'
)
@click.argument(
    'state',
    type=click.Choice(
        ['on', 'off', 'reboot',
         'reset', 'shutdown']
    ),
    required=True
)
@click.option(
    '-c', '--confirm',
    is_flag=True, default=False,
    help='Confirm state change'
)
@pass_context
def compute_vm_set_state(
        ctx: Configuration,
        state, confirm
):
    """ Set given virtual machine power state.

    vss compute vm set <uuid> state on|off|reset|reboot|shutdown -c

    Reboot and shutdown send a guest OS restart signal
    (VMware Tools required).

    """
    # lookup dict for state
    lookup = {
        'on': 'poweredOn',
        'off': 'poweredOff',
        'reset': 'reset',
        'reboot': 'reboot',
        'shutdown': 'shutdown'
    }
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        state=lookup[state]
    )
    # add common options
    payload.update(ctx.payload_options)
    # validate VMware tools if shutdown/reboot
    if state in ['reboot', 'shutdown']:
        vmt = ctx.get_vm_tools(ctx.uuid)
        if not vmt:
            raise click.BadParameter(
                f'VMware Tools status could '
                f'not be checked on {ctx.uuid} '
            )
        if vmt.get('runningStatus') not in ["guestToolsRunning"]:
            raise click.BadParameter(
                f'VMware Tools must be running '
                f'on {ctx.uuid} send a reboot or shutdown '
                f'signal.'
            )
    # process request
    # show guest os info if no confirmation flag has been
    # included - just checking
    guest_info = ctx.get_vm_guest(ctx.uuid)
    ip_addresses = ', '.join(guest_info.get('ipAddress')) \
        if guest_info.get('ipAddress') else ''
    # confirmation string
    confirmation_str = const.DEFAULT_STATE_MSG.format(
        state=state, ip_addresses=ip_addresses,
        **guest_info
    )
    confirmation = confirm or click.confirm(confirmation_str)
    if not confirmation:
        raise click.ClickException('Cancelled by user.')
    # request
    obj = ctx.update_vm_state(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'template',
    short_help='Mark vm as template or vice versa.'
)
@click.option(
    '--on/--off', is_flag=True,
    help='Marks vm as template or template as vm',
    default=False
)
@pass_context
def compute_vm_set_template(
        ctx: Configuration, on
):
    """Marks virtual machine as template or template to virtual machine.

    vss compute vm set <uuid> template --on/--off
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        value=on
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.mark_template_as_vm(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'tools',
    short_help='Manage VMware Tools'
)
@click.argument(
    'action',
    type=click.Choice(['upgrade',
                       'mount',
                       'unmount']),
    required=True
)
@pass_context
def compute_vm_set_tools(
        ctx: Configuration, action
):
    """Upgrade, mount and unmount official VMware Tools package.
    This command does not apply for Open-VM-Tools.

    vss compute vm set <uuid> tools upgrade|mount|unmount
    """
    payload = dict(
        uuid=ctx.uuid,
        action=action
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_tools(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.command(
    'usage',
    short_help='Usage (Metadata)'
)
@click.argument(
    'usage',
    type=click.Choice(['Prod', 'Test',
                       'Dev', 'QA']),
    required=True
)
@pass_context
def compute_vm_set_usage(
        ctx: Configuration, usage
):
    """Update virtual machine usage in both name prefix
    and metadata.

    vss compute vm set <uuid> usage Prod|Test|Dev|QA
    """
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        usage=usage
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_vss_usage(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set.group(
    'version'
)
@pass_context
def compute_vm_set_version(ctx: Configuration):
    """Manage virtual machine virtual hardware version and policy."""


@compute_vm_set_version.command(
    'vmx',
    short_help='Update hardware (VMX) version'
)
@click.argument(
    'vmx', type=click.Choice(['vmx-11',
                              'vmx-12',
                              'vmx-13']),
    required=False, default='vmx-13'
)
@pass_context
def compute_vm_set_version_policy_vmx(
        ctx: Configuration, vmx
):
    """Update virtual hardware version."""
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        vmx=vmx
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_version(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm_set_version.command(
    'policy',
    short_help='Update hardware (VMX) version '
               'upgrade policy'
)
@click.argument(
    'policy',
    type=click.Choice(['never', 'onSoftPowerOff', 'always']),
    required=True
)
@pass_context
def compute_vm_set_version_policy(
        ctx: Configuration, policy
):
    """Update virtual hardware version upgrade policy."""
    # create payload
    payload = dict(
        uuid=ctx.uuid,
        policy=policy
    )
    # add common options
    payload.update(ctx.payload_options)
    # request
    obj = ctx.update_vm_version_policy(**payload)
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@compute_vm.group(
    'rm', help='Delete given virtual machines',
    invoke_without_command=True
)
@click.option(
    '-f', '--force',
    is_flag=True, default=False,
    help='Force deletion if power state is on'
)
@click.option(
    '-m', '--max-del', type=click.IntRange(1, 10),
    required=False, default=3
)
@click.option(
    '-s', '--show-info',
    is_flag=True, default=False,
    help='Show guest info and confirmation '
         'if -f/--force is not included.')
@click.argument(
    'uuid', type=click.UUID,
    required=True,
    nargs=-1
)
@pass_context
def compute_vm_rm(
        ctx: Configuration, uuid,
        force, max_del, show_info
):
    """ Delete a list of virtual machine uuids:

        vss compute vm rm <uuid> <uuid> --show-info

    """
    # result set
    objs = list()
    if len(uuid) > max_del:
        raise click.BadArgumentUsage(
            'Increase max instance removal with '
            '--max-del/-m option'
        )
    #
    for vm in uuid:
        skip = False
        _vm = ctx.get_vm(vm)
        if not _vm:
            _LOGGING.warning(
                f'Virtual machine {vm} could not be found. '
                f'Skipping.'
            )
            skip = True
        if _vm and show_info:
            folder_info = ctx.get_vm_folder(vm)
            name = ctx.get_vm_name(vm)
            guest_info = ctx.get_vm_guest(vm)
            ip_addresses = ', '.join(guest_info.get('ipAddress')) \
                if guest_info.get('ipAddress') else ''

            c_str = const.DEFAULT_VM_DEL_MSG.format(
                name=name, folder_info=folder_info,
                ip_addresses=ip_addresses,
                **guest_info
            )
            confirmation = force or click.confirm(c_str)
            if not confirmation:
                _LOGGING.warning(
                    f'Skipping {vm}...'
                )
                skip = True
        if not skip:
            # request
            payload = dict(uuid=vm, force=force)
            objs.append(ctx.delete_vm(**payload))
    # print
    columns = ctx.columns or const.COLUMNS_REQUEST_SUBMITTED
    for obj in objs:
        click.echo(
            format_output(
                ctx,
                [obj],
                columns=columns,
                single=True
            )
        )
