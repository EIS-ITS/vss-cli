"""Folder Request Management plugin for VSS CLI (vss-cli)."""
import click
import logging

from vss_cli import const
from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.helper import format_output
from vss_cli.plugins.request import cli


_LOGGING = logging.getLogger(__name__)


@cli.group(
    'folder',
    short_help='Manage logical folder requests.'
)
@click.pass_context
def request_mgmt_folder(ctx: Configuration):
    """ Logical Folders are containers for storing and organizing
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

            vss-cli request folder ls -f status,eq,Processed

        Sort list in the following format <field_name>,<asc|desc>. For example:

            vss-cli request folder ls -s created_on,desc

    """
    columns = ctx.columns or const.COLUMNS_REQUEST_FOLDER_MIN
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
        columns=columns
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
    columns = ctx.columns or const.COLUMNS_REQUEST_FOLDER
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )
