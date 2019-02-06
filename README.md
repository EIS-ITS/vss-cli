# ITS Private Cloud Command Line Interface

[![CI][build-img]](https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/commits/master)
[![Coverage][coverage-img]](https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/commits/master)
[![PyPI][pypi-img]](https://pypi.python.org/pypi/vsscli-ng)
[![PyPI version][pyver-img]](https://pypi.python.org/pypi/vsscli-ng)
[![Docker Image Pulls][docker-pulls-img]][docker-image]
[![Docker Image Layers][docker-layer-img]][docker-image]
[![Docker Image Version][docker-version-img]][docker-image]

This package provides a unified command line interface to the ITS Private Cloud.

## Documentation

Package documentation is now available at [docs][docs].

## Installation

> Windows users, download and install [Python Releases for Windows][Python Releases for Windows] prior running [pip][pip].

The fastest way to install VSS CLI is to use [pip][pip]:

```bash
pip install vsscli-ng
```

If you have the VSS CLI installed and want to upgrade to the latest version
you can run:

```bash
pip install --upgrade vsscli-ng
```

This will install VSS CLI as well as all dependencies. You can also just [download the tarball][download the tarball].
Once you have the `vss-cli` directory structure on your workstation, you can just run:

```bash
cd path_to_vsscli
python setup.py install
```


## CLI Releases

The release notes for the VSS CLI can be found [CHANGELOG](CHANGELOG.md) in the gitlab repo.

## Getting Started

Before using VSS CLI, you need setup your VSS credentials. You can do this in a couple of ways:

* Environment variables
* Configuration file

The quickest way to get started is to run the `vss-cli configure mk`` command:

```bash
vss-cli configure mk

Endpoint [https://cloud-api.eis.utoronto.ca]: 
Username: jm
Password: 
Repeat for confirmation: 

```

To use environment variables, set ``VSS_USER`` and ``VSS_USER_PASS`` or ``VSS_TOKEN``:

```bash
export VSS_USER=USER
export VSS_USER_PASS=superstrongpassword
# or
export VSS_TOKEN=JWT_TOKEN
```

To use a config file, create a configuration as follows:

```javascript
    {
    "https://vss-api.eis.utoronto.ca": {
        "auth": "<encoded_creds>",
        "token": "<access_token"
        }
    }
```

Place it in ``~/.vss-cli/config.json`` (or in ``%UserProfile%\.vss-cli\config.json`` on Windows).
If you place the config file in a different location than ``~/.vss-cli/config.json``
you need to inform VSS CLI the full path. Do this by setting
the appropriate environment variable:

```bash
export VSS_CONFIG=/path/to/config_file.json
```

Or use the ``-c/--config`` option in the ``vss-cli`` command as follows:

```bash
vss -c ~/.secret/vss-config.json
```

By default VSS CLI output is text, and this can be configured either by ``-o/--output``
option or the ``VSS_OUTPUT`` environment variable as follows:

```bash
$ export VSS_OUTPUT=json
# or
$ export VSS_OUTPUT=text
```

Options are `json`, `yaml`, `table`, `auto`.

The VSS CLI supports the following table formats supported by [python-tabulate](https://pypi.org/project/tabulate/): 
`plain`, `simple`, `github`, `grid`, `fancy_grid`, `pipe`, `orgtbl`, `rst`, `mediawiki`, `html`, `latex`, `latex_raw`, 
`latex_booktabs` or `tsv`. Default is `simple`.

This option is configurable by using ``--table-format`` or `VSS_TABLE` environment variable as follows:

```bash
$ export VSS_TABLE=simple
```

You can also control the data shown with ``--columns`` providing a name and a `jsonpath`. For instance 
``--columns=ID=id,VMNAME=vm_name,WARNINGS=message.warnings[*] request snapshot ls``

```text
  ID  VMNAME           WARNINGS
----  ---------------  -----------------------
   1  1502P-wiki-vss   Snapshot 3 deleted
   6  1000P-Med-ASP02  Snapshot 1 deleted
   2  1606T-coreos0    Snapshot 1 deleted
```

## JSON Parameter Input (WIP)

VSS CLI options vary from simple string, boolean or numeric values to
JSON data structures as input parameters on the command line.

For example, consider the following command to deploy a new virtual
machine from a given template and provide a guest operating system
specification to reconfigure hostname, domain, dns, ip, subnet
and gateway:

```bash
vss compute vm mk from-template --source c5916abb-def3-4d4d-8abe-2240b0a6c265 \
      --description 'New virtual machine' \
      --custom-spec '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": [{"dhcp": true}]}'
```

## Auto-completion (WIP)

As described above you can use source <(hass-cli completion zsh) to quickly and easy enable auto completion. 
If you do it from your .bashrc or .zshrc its recommend to use the form below as that does not trigger a run of hass-cli itself.

For zsh:

```bash
eval "$(_VSS_CLI_COMPLETE=source_zsh vss-cli)"
```

For bash:

```bash
eval "$(_VSS_COMPLETE=source vss-cli)"
```

Activating `bash` or `zsh` completion can be done by executing the following command:

```bash
source <(vss-cli completion bash)
```

or

```bash
source <(vss-cli completion zsh)
```

## VSS Shell

The VSS CLI provides a REPL interactive shell with tab-completion, suggestions and
command history.

```bash
Usage: vss shell [OPTIONS]

  REPL interactive shell.

Options:
  -i, --history TEXT  File path to save history
  --help              Show this message and exit.

```
To enter the shell just execute vss shell and you will get the following welcome message:

```bash
    __   _____ ___
    \ \ / / __/ __|      API Endpoint: https://cloud-api.eis.utoronto.ca/v2
     \ V /\__ \__ \      Tab-completion & suggestions
      \_/ |___/___/      Prefix external commands with "!"
       CLI v0.0.0        History is saved: /Users/user/.vss-cli/history

    Exit shell with :exit, :q, :quit, ctrl+d

```

## Getting Help

We use GitLab issues for tracking bugs, enhancements and feature requests.
If it turns out that you may have found a bug, please [open a new issue][open a new issue].

## Versioning

The API versions are tagged based on [Semantic Versioning](https://semver.org/). Versions available in the 
[tags section](https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/tags).

## Contributing

Refer to the [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process of 
submitting code to the repository.


[docs]: https://eis.utoronto.ca/~vss/vsscli-ng/
[download the tarball]: https://pypi.python.org/pypi/vsscli-ng
[Click]: http://click.pocoo.org/6/
[Python Releases for Windows]: https://www.python.org/downloads/windows/
[pip]: http://www.pip-installer.org/en/latest/
[open a new issue]: https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/issues/new>
[build-img]: https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/badges/master/build.svg
[coverage-img]: https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng/badges/master/coverage.svg
[pypi-img]: https://img.shields.io/pypi/v/vsscli-ng.svg
[pyver-img]: https://img.shields.io/pypi/pyversions/vsscli-ng.svg
[docker-pulls-img]:  https://img.shields.io/docker/pulls/uofteis/vsscli-ng.svg
[docker-layer-img]: https://images.microbadger.com/badges/image/uofteis/vsscli-ng.svg
[docker-version-img]: https://images.microbadger.com/badges/version/uofteis/vsscli-ng.svg
[docker-image]: https://hub.docker.com/r/uofteis/vsscli-ng/
