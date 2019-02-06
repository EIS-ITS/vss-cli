"""Details for the auto-completion."""
import os
from typing import Any, Dict, List, Tuple  # NOQA

from vss_cli import const
from vss_cli.config import Configuration


def _init_ctx(ctx: Configuration) -> None:
    """Initialize ctx."""
    # ctx is incomplete thus need to 'hack' around it
    # see bug https://github.com/pallets/click/issues/942
    if not hasattr(ctx, 'server'):
        ctx.server = os.environ.get('VSS_ENDPOINT', const.DEFAULT_SERVER)

    if not hasattr(ctx, 'token'):
        ctx.token = os.environ.get('VSS_TOKEN', None)

    if not hasattr(ctx, 'username'):
        ctx.password = os.environ.get('VSS_USER', None)

    if not hasattr(ctx, 'password'):
        ctx.password = os.environ.get('VSS_USER_PASS', None)

    if not hasattr(ctx, 'timeout'):
        ctx.timeout = int(
            os.environ.get('VSS_TIMEOUT', str(const.DEFAULT_TIMEOUT))
        )


def table_formats(
    ctx: Configuration, args: List, incomplete: str
) -> List[Tuple[str, str]]:
    """Table Formats."""
    _init_ctx(ctx)

    completions = [
        ("plain", "Plain tables, no pseudo-graphics to draw lines"),
        ("simple", "Simple table with --- as header/footer (default)"),
        ("github", "Github flavored Markdown table"),
        ("grid", "Formatted as Emacs 'table.el' package"),
        ("fancy_grid", "Draws a fancy grid using box-drawing characters"),
        ("pipe", "PHP Markdown Extra"),
        ("orgtbl", "org-mode table"),
        ("jira", "Atlassian Jira Markup"),
        ("presto", "Formatted as PrestoDB cli"),
        ("psql", "Formatted as Postgres psql cli"),
        ("rst", "reStructuredText"),
        ("mediawiki", "Media Wiki as used in Wikpedia"),
        ("moinmoin", "MoinMain Wiki"),
        ("youtrack", "Youtrack format"),
        ("html", "HTML Markup"),
        ("latex", "LaTeX markup, replacing special characters"),
        ("latex_raw", "LaTeX markup, no replacing of special characters"),
        (
            "latex_booktabs",
            "LaTex markup using spacing and style from `booktabs",
        ),
        ("textile", "Textile"),
        ("tsv", "Tab Separated Values"),
    ]

    completions.sort()

    return [c for c in completions if incomplete in c[0]]

