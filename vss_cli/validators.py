import re
import click


def validate_phone_number(ctx, param, phone):
    phone_regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|' \
                  r'\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})+'
    if not re.match(phone_regex, phone):
        raise click.BadParameter(
            'Value must be in the following format 416-166-6666')
    return phone


def validate_email(ctx, param, email):
    email_regex = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    if not re.match(email_regex, email):
        raise click.BadParameter('Value must be in the '
                                 'following format user@utoronto.ca')
    return email
