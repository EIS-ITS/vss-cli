"""Request Management plugin for VSS CLI (vss-cli)."""
import click
from vss_cli.cli import pass_context
from vss_cli import const
from vss_cli.config import Configuration
from vss_cli.helper import format_output


@click.group('request')
@pass_context
def cli(ctx: Configuration):
    """Manage various requests.
    Useful to track request status and details."""
    ctx.load_config()


@cli.group('image-sync')
@pass_context
def request_mgmt_image_sync(ctx: Configuration):
    """Manage user-image synchronization requests.

    Synchronizing your personal store files with the VSS API produces a
    image-sync request"""


@request_mgmt_image_sync.command(
    'ls',
    short_help='list image-sync requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_image_sync_ls(
        ctx: Configuration, filter, page,
        sort, show_all, count):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request image-sync ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request image-sync ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.append(('TYPE', 'type'))
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort
    # make request
    _requests = ctx.get_image_sync_requests(
        show_all=show_all,
        per_page=count, **params)
    # format output
    output = format_output(
        ctx,
        _requests,
        columns=columns,
    )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_image_sync.command(
    'get',
    help='Image sync request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_image_sync_get(ctx, rid):
    obj = ctx.get_image_sync_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            [('TYPE', 'type'),
             ('DELETED', 'deleted'),
             ('ADDED', 'added'),
             ('ERRORS', 'message.errors'),
             ('WARNINGS', 'message.warnings'),
             ('TASK', 'task_id'),
             ('USER', 'user.username')]
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group('snapshot')
@pass_context
def request_mgmt_snapshot(ctx: Configuration):
    """Manage virtual machine snapshot requests.

    Creating, deleting and reverting virtual machine snapshots will produce
    a virtual machine snapshot request."""


@request_mgmt_snapshot.command(
    'ls',
    short_help='list snapshot requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_snapshot_mgmt_ls(ctx: Configuration, filter, page,
        sort, show_all, count):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request snapshot ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request snapshot ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('VM_NAME', 'vm_name'),
            ('VM_UUID', 'vm_uuid'),
            ('ACTION', 'action')
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_snapshot_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
            ctx,
            _requests,
            columns=columns,
        )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_snapshot.command(
    'get',
    help='Snapshot request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_snapshot_mgmt_get(ctx, rid):
    obj = ctx.get_snapshot_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_SNAP
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@request_mgmt_snapshot.group(
    'set',
    help='Update snapshot request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_snapshot_mgmt_set(ctx: Configuration, rid):
    ctx.rid = rid
    pass


@request_snapshot_mgmt_set.command('duration')
@click.option('-l', '--lifetime', type=click.IntRange(1, 72),
              help='Number of hours the snapshot will live.',
              required=True)
@pass_context
def request_snapshot_mgmt_set_duration(ctx: Configuration, lifetime):
    """Extend snapshot lifetime"""
    _, obj = ctx.extend_snapshot_request(ctx.rid, lifetime)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_SNAP
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group('new')
@pass_context
def request_mgmt_new(ctx: Configuration):
    """Manage your new virtual machine deployment requests."""
    pass


@request_mgmt_new.command(
    'ls', short_help='list vm new requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_new_ls(
        ctx: Configuration, filter, page, sort,
        show_all, count
):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request new ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request new ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('APPROVED', 'approval.approved'),
            ('VM_NAME', 'vm_name'),
            ('VM_UUID', 'vm_uuid'),
            ('BUILT', 'built_from')
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_new_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
            ctx,
            _requests,
            columns=columns,
        )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_new.command(
    'get',
    short_help='New vm request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_new_get(
    ctx: Configuration,
    rid
):
    obj = ctx.get_new_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_NEW
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@request_mgmt_new.command(
    'retry',
    short_help='Retry vm new request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_new_retry(ctx: Configuration, rid):
    """Retries given virtual machine new request with status
    'Error Processed'.
    """
    obj = ctx.retry_new_request(rid)
    columns = ctx.columns or []
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_SUBMITTED
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group('change')
@pass_context
def request_mgmt_change(ctx: Configuration):
    """Manage virtual machine change requests.

    Updating any virtual machine attribute will produce a virtual machine
    change request."""
    pass


@request_mgmt_change.command(
    'ls',
    short_help='list vm change requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_change_ls(
        ctx: Configuration, filter, page, sort,
        show_all, count
):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request change ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request change ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('APPROVED', 'approval.approved'),
            ('VM_NAME', 'vm_name'),
            ('VM_UUID', 'vm_uuid'),
            ('ATTRIBUTE', 'attribute'),
            ('VALUE', 'value[*]')
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_change_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
            ctx,
            _requests,
            columns=columns,
        )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_change.command(
    'get',
    short_help='Change request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_change_get(ctx: Configuration, rid):
    obj = ctx.get_change_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_CHANGE
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@request_mgmt_change.command(
    'retry',
    short_help='Retry vm change request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_change_retry(ctx: Configuration, rid):
    """Retries given virtual machine change request with status
    'Error Processed'.
    """
    obj = ctx.retry_change_request(rid)
    columns = ctx.columns or []
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_SUBMITTED
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group('export')
@pass_context
def request_mgmt_export(ctx: Configuration):
    """Manage virtual machine export requests."""
    pass


@request_mgmt_export.command(
    'ls',
    short_help='list vm export requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_export_ls(ctx: Configuration, filter, page, sort,
                           show_all, count):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request export ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request export ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('VM_NAME', 'vm_name'),
            ('VM_UUID', 'vm_uuid'),
            ('TRANSFERRED', 'transferred'),
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_export_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
            ctx,
            _requests,
            columns=columns,
        )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_export.command(
    'get',
    short_help='Export request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_export_get(ctx: Configuration, rid):
    obj = ctx.get_export_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_EXPORT
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group(
    'folder',
    help='Manage logical folder requests.'
)
@click.pass_context
def request_mgmt_folder(ctx: Configuration):
    """Manage logical folder requests.

    Logical Folders are containers for storing and organizing
    inventory objects, in this case virtual machines."""
    pass


@request_mgmt_folder.command(
    'ls',
    short_help='list logical folder requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_folder_ls(
        ctx, filter, page, sort,
        show_all, count
):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request folder ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request folder ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('ACTION', 'action'),
            ('MOREF', 'moref'),
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_folder_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
            ctx,
            _requests,
            columns=columns,
        )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_folder.command(
    'get',
    short_help='Folder request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_folder_get(ctx, rid):
    obj = ctx.get_folder_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_FOLDER
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@cli.group('inventory')
@pass_context
def request_mgmt_inventory(ctx: Configuration):
    """Manage virtual machine inventory requests."""


@request_mgmt_inventory.command(
    'ls',
    short_help='list inventory requests'
)
@click.option('-f', '--filter', type=click.STRING,
              help='apply filter')
@click.option('-s', '--sort', type=click.STRING,
              help='apply sorting ')
@click.option('-a', '--show-all', is_flag=True,
              help='show all results')
@click.option('-c', '--count', type=int,
              help='size of results')
@click.option('-p', '--page', is_flag=True,
              help='page results in a less-like format')
@pass_context
def request_mgmt_inventory_ls(
        ctx: Configuration, filter, page, sort,
        show_all, count
):
    """List requests based on:

        Filter list in the following format <field_name>,<operator>,<value>
        where operator is eq, ne, lt, le, gt, ge, like, in.
        For example: status,eq,Processed

            vss request inventory ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss request inventory ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend([
            ('NAME', 'name'),
            ('FORMAT', 'format')
        ])
    params = dict()
    if filter:
        params['filter'] = filter
    if sort:
        params['sort'] = sort

    _requests = ctx.get_inventory_requests(
        show_all=show_all,
        per_page=count, **params)

    output = format_output(
        ctx,
        _requests,
        columns=columns,
    )
    # page results
    if page:
        click.echo_via_pager(output)
    else:
        click.echo(output)


@request_mgmt_inventory.command(
    'get',
    short_help='Inventory request'
)
@click.argument('rid', type=int, required=True)
@pass_context
def request_mgmt_inventory_get(ctx: Configuration, rid):
    obj = ctx.get_inventory_request(rid)
    columns = ctx.columns or const.COLUMNS_REQUEST
    if not ctx.columns:
        columns.extend(
            const.COLUMNS_REQUEST_INVENTORY
        )
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )
