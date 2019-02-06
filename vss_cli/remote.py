"""
Basic API to access remote instance of VSS.

If a connection error occurs while communicating with the API a
VssCliError will be raised.
"""
import collections
from datetime import datetime
import enum
import json
import logging
from typing import Any, Dict, List, Optional, cast
import urllib.parse
from urllib.parse import urlencode

from vss_cli.config import Configuration
from vss_cli.exceptions import VssCliError
import vss_cli.vssconst as vss
import requests

_LOGGER = logging.getLogger(__name__)

CONTENT_TYPE = 'Content-Type'
METH_DELETE = 'DELETE'
METH_GET = 'GET'
METH_POST = 'POST'
METH_PUT = 'PUT'
METH_PATCH = 'PATCH'


class APIStatus(enum.Enum):
    """Representation of an API status."""

    OK = "ok"
    INVALID_PASSWORD = "invalid_password"
    CANNOT_CONNECT = "cannot_connect"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        """Return the state."""
        return self.value  # type: ignore


def restapi(
    ctx: Configuration, method: str, path: str, data: Optional[Dict] = None
) -> requests.Response:
    """Make a call to the VSS REST API."""
    if data is None:
        data_str = None
    else:
        data_str = json.dumps(data, cls=JSONEncoder)

    headers = {CONTENT_TYPE: vss.CONTENT_TYPE_JSON}  # type: Dict[str, Any]

    if ctx.token:
        headers["Authorization"] = "Bearer {}".format(ctx.token)

    url = urllib.parse.urljoin(ctx.server + path, "")

    try:
        if method == METH_GET:
            return requests.get(url, params=data_str, headers=headers)

        return requests.request(method, url, data=data_str, headers=headers)

    except requests.exceptions.ConnectionError:
        raise VssCliError("Error connecting to {}".format(url))

    except requests.exceptions.Timeout:
        error = "Timeout when talking to {}".format(url)
        _LOGGER.exception(error)
        raise VssCliError(error)


class JSONEncoder(json.JSONEncoder):
    """JSONEncoder that supports VSS objects."""

    # pylint: disable=method-hidden
    def default(self, o: Any) -> Any:
        """Convert VSS objects.

        Hand other objects to the original method.
        """
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, set):
            return list(o)
        if hasattr(o, "as_dict"):
            return o.as_dict()

        return json.JSONEncoder.default(self, o)
