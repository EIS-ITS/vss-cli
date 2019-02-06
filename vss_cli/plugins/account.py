"""Account Management plugin for VSS CLI (vss-cli)."""
import click
from vss_cli.cli import pass_context
from vss_cli import const
from vss_cli.config import Configuration
from vss_cli.helper import format_output


@click.group(
    'account',
    short_help='Manage your VSS account'
)
@pass_context
def cli(ctx: Configuration):
    """Manage your VSS account."""
    ctx.load_config()


@cli.group('get',
           short_help='get account attribute')
@pass_context
def account_get(ctx: Configuration):
    """Obtain an account attribute"""
    pass


@account_get.group('digest')
@pass_context
def account_get_digest(ctx):
    """Get digest status"""
    pass


@account_get_digest.command('message')
@pass_context
def account_get_digest_message(ctx: Configuration):
    """Get message digest status"""
    _obj = ctx.get_user_digest_settings()
    obj = {'message': _obj.get('message')}
    columns = ctx.columns or const.COLUMNS_MESSAGE_DIGEST
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get.command('groups')
@pass_context
def account_get_groups(ctx: Configuration):
    """User group membership"""
    obj = dict(groups=ctx.get_user_groups())
    columns = ctx.columns or const.COLUMNS_GROUPS
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get.command('group')
@click.argument(
    'group_name', type=click.STRING, required=True)
@pass_context
def account_get_group(ctx: Configuration, group_name):
    """Get given group info or members.
    User must be part of the group."""
    obj = ctx.get_user_group(group_name, True)
    columns = ctx.columns or const.COLUMNS_GROUP
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get.command('access-role')
@pass_context
def account_get_access_role(ctx: Configuration):
    """Access role and entitlements"""
    obj = ctx.get_user_roles()
    columns = ctx.columns or const.COLUMNS_ROLE
    click.echo(
        format_output(
            ctx,
            [obj['access']],
            columns=columns,
            single=True
        )
    )


@account_get.command('request-role')
@pass_context
def account_get_request_role(ctx: Configuration):
    """Request role and entitlements"""
    obj = ctx.get_user_roles()
    columns = ctx.columns or const.COLUMNS_ROLE
    click.echo(
        format_output(
            ctx,
            [obj['request']],
            columns=columns,
            single=True
        )
    )


@account_get.command('personal')
@pass_context
def account_get_personal(ctx: Configuration):
    """User information"""
    obj = ctx.get_user_personal()
    obj.update(ctx.get_user_ldap())
    columns = ctx.columns or const.COLUMNS_USER_PERSONAL
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get.command('status')
@pass_context
def account_get_pstatus(ctx: Configuration):
    """Account status"""
    obj = ctx.get_user_status()
    columns = ctx.columns or const.COLUMNS_USER_STATUS
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get.group('notification')
@pass_context
def account_get_notification(ctx: Configuration):
    """Notification settings"""
    pass


@account_get_notification.command('request')
@pass_context
def account_get_notification_request(ctx: Configuration):
    """Get notification format"""
    obj = ctx.get_user_request_notification_settings()
    columns = ctx.columns or const.COLUMNS_NOT_REQUEST
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_get_notification.command('format')
@pass_context
def account_get_notification_format(ctx: Configuration):
    """Get notification format"""
    obj = ctx.get_user_notification_format()
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=ctx.columns,
            single=True
        )
    )


@account_get_notification.command('method')
@pass_context
def account_get_notification_method(ctx: Configuration):
    """Get notification format"""
    obj = ctx.get_user_notification_method()
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=ctx.columns,
            single=True
        )
    )


@cli.group(
    'set',
    short_help='set account attribute'
)
@pass_context
def account_set(ctx: Configuration):
    """Set account attribute"""
    pass


@account_set.group(
    'digest',
    short_help='set account weekly digest configuration'
)
@pass_context
def account_set_digest(ctx: Configuration):
    """update weekly digest configuration"""
    pass


@account_set_digest.command(
    'message'
)
@click.argument(
    'state',
    type=click.Choice(['in', 'out']),
    required=True
)
@pass_context
def account_set_digest_message(
        ctx: Configuration, state
):
    """Opt-in or opt-out of weekly message digest"""
    if state == 'in':
        ctx.enable_user_message_digest()
    else:
        ctx.disable_user_message_digest()
    _obj = ctx.get_user_digest_settings()
    obj = {'message': _obj.get('message')}
    columns = ctx.columns or const.COLUMNS_MESSAGE_DIGEST
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=columns,
            single=True
        )
    )


@account_set.group(
    'notification',
    short_help='set account notification settings'
)
@pass_context
def account_notification_set(ctx: Configuration):
    """Set account notification settings"""
    pass


@account_notification_set.command(
    'format'
)
@click.argument(
    'fmt',
    type=click.Choice(['html', 'text']),
    required=True)
@pass_context
def account_notification_set_format(
        ctx: Configuration,
        fmt
):
    """Update notification format where FMT can be html or text"""
    obj = ctx.update_user_notification_format(fmt)
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=ctx.columns,
            single=True
        )
    )


@account_notification_set.command(
    'method'
)
@click.argument(
    'method',
    type=click.Choice(['mail', 'message']),
    required=True
)
@pass_context
def account_notification_set_method(
        ctx: Configuration,
        method
):
    """Update notification method where METHOD can be mail or message"""
    obj = ctx.update_user_notification_method(method)
    click.echo(
        format_output(
            ctx,
            [obj],
            columns=ctx.columns,
            single=True
        )
    )
