"""Validators module for the VSS-CLI."""
import json
import logging
import re
from uuid import UUID

import click

from vss_cli.helper import to_tuples

_LOGGING = logging.getLogger(__name__)


def process_options(ctx, param, key_value):
    """Process options."""
    try:
        _options = to_tuples(','.join(key_value))
        options = [{opt[0]: opt[1]} for opt in _options]
        _LOGGING.debug(f'_options={_options} -> options={options}')
        return options
    except Exception as ex:
        _LOGGING.error(ex)
        raise click.BadArgumentUsage('Argument must be key=value strings')


def validate_phone_number(ctx, param, phone):
    """Validate phone number."""
    phone_regex = (
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|'
        r'\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d'
        r'{3}[-\.\s]??\d{4})+'
    )
    if not re.match(phone_regex, phone):
        raise click.BadParameter(
            'Value must be in the ' 'following format 416-166-6666'
        )
    return phone


def validate_email(ctx, param, email):
    """Validate email callback method."""
    email_regex = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+' r'\.[a-zA-Z0-9-.]+$)'
    if not re.match(email_regex, email):
        raise click.BadParameter(
            'Value must be in the ' 'following format user@utoronto.ca'
        )
    return email


def validate_json_type(ctx, param, value):
    """Validate json callback method."""
    try:
        if value is not None:
            return json.loads(value)
    except ValueError as ex:
        _LOGGING.error(f'{ex}')
        raise click.BadParameter(
            f'{param.name} should be a JSON parameter input.'
        )


def validate_admin(ctx, param, value):
    """Validate admin callback method."""
    if value:
        _value = value.split(':')
        if not value or len(_value) < 2:
            raise click.BadParameter(
                'Admin should be in the '
                'following format: '
                'FullName:Phone:email'
            )
        validate_email(ctx, param, _value[2])
        validate_phone_number(ctx, param, _value[1])
        return value


def validate_inform(ctx, param, value):
    """Validate inform callback method."""
    if value:
        _value = value.split(',')
        if not value:
            raise click.BadParameter(
                'Informational contacts format:'
                'email@utoronto.ca,email2@utoronto.ca'
            )
        for email in _value:
            validate_email(ctx, param, email)
        return value


def validate_uuid(ctx, param, value):
    """Validate uuid callback method."""
    if value:
        try:
            _ = UUID(value)
            return value
        except ValueError:
            return False


def validate_vm_moref(ctx, param, value):
    """Validate moref callback method."""
    if value:
        if re.match(r'vm-[0-9]+', value):
            return value
    return False
