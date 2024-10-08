"""AI assistant."""
import logging
import random

import click

from vss_cli.cli import pass_context
from vss_cli.config import Configuration
from vss_cli.utils.emoji import EMOJI_UNICODE

_LOGGING = logging.getLogger(__name__)

ej_ai = EMOJI_UNICODE.get(':robot_face:')
ej_rk = EMOJI_UNICODE.get(':rocket:')

we_msg = f"""Hi, I’m UTORcloudy {ej_ai}, the ITS Private Cloud virtual agent.
I can help with account, virtual machine management, billing questions
and more. {ej_rk}
"""

suggestions = [
    "How to deploy an Ubuntu virtual machine?",
    "How do I get started?",
    "What are the VSS Guidelines?",
    "How can I reset my account password?",
    "How to enable Ubuntu Pro on your VM?",
    "How to activate Windows Server in the ITS Private Cloud?",
    "Do you provide public IP addresses?",
    "How Can I change CPU, Memory,Network, HDD specs after a VM is created?",
    "How to request an SSL certificate?",
    "What additional services are included in my ITS Private Cloud bill?",
    "What factors determine the cost of my ITS Private Cloud usage?",
    'How can I install sentinelOne on my VM?',
]

final_msg = """
Responses are generated by artificial intelligence and may contain errors.
Always check sources and refer to actual policies for reliable information."""


@click.command('assist', short_help='VSS AI Assistant')
@click.option(
    '--no-load', is_flag=True, default=False, help='do not load config'
)
@click.argument(
    "message",
    required=False,
)
@pass_context
def cli(ctx: Configuration, no_load: bool, message: str):
    """Manage your VSS account."""
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        if no_load:
            ctx.set_defaults()
        else:
            ctx.load_config(spinner_cls=spinner_cls)
            _LOGGING.debug(
                f'GPT settings: {ctx.gpt_persona=}, '
                f'{ctx.gpt_token=}, {ctx.gpt_server}'
            )
        if not message:
            spinner_cls.stop()
            ctx.secho(we_msg)
            default = random.choice(suggestions)
            message = click.prompt(
                "How may I assist you?",
                type=str,
                prompt_suffix=" ",
                show_default=True,
                default=f"{default}",
            )
            ctx.echo("")
            spinner_cls.start()
        ctx.ask_assistant(
            spinner_cls=spinner_cls, message=message, final_message=final_msg
        )
