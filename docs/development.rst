.. _Development:

Development
===========

First time setup
----------------

1. Download and install the `Latest version of git`_.
2. Configure git with your ``username`` and ``email`` matching your GitLab account:

.. code-block:: bash

    git config --global user.name 'your name'
    git config --global user.email 'your email'

3. Fork the ``vss-cli`` repository by clicking the `Fork`_ button.
4. Clone your fork locally:

.. code-block:: bash

    git clone git@gitlab-ee.eis.utoronto.ca:{username}/vss-cli.git
    cd vss-cli

5. Add the main repository as a remote to update later:

.. code-block:: bash

    git remote add vss git@gitlab-ee.eis.utoronto.ca:vss/vss-cli.git
    git fetch vss

6. Create virtual environment:

.. code-block:: bash

    python3 -m venv vss-cli
    source vss-cli/bin/activate

Start Coding
------------
1. Create a branch to identify the issue you would like to work on (e.g. ``issue-999``):

.. code-block:: bash

    cd vss-cli
    git checkout -b issue-999

2. Using your favorite editor, make your changes, `committing as you go`_.
3. Follow `PEP8`_.

.. code-block:: bash

    pip install .[test]
    flake8 --ignore F401,E402, vss_cli

4. Push your commits to GitLab and `create a merge request`_.

.. code-block:: bash

    git push origin issue-999

5. Celebrate 🎉

Build docs
----------
1. Install requirements:

.. code-block:: bash

    pip install .[dev]

2. Go to the `docs` folder and run `make` to start the build:

.. code-block:: bash

    cd docs
    make html


Developing Plugins
------------------
Plugin developers need to register their sub-commands or sub-groups to either of the following entry-points
in their `setup.py` that is loaded by the `vss-cli` core package:

- ``vss_cli.contrib.plugins``: scope at ``vss-cli plugins`` command group.
- ``vss_cli.contrib.compute.plugins``: scope at ``vss-cli compute`` command group.
- ``vss_cli.contrib.compute.vm.plugins``: scope at ``vss-cli compute vm`` command group.

For example, if someone wanted to make a plugin package called ``new_plugin`` which adds a sub-command at
``vss-cli compute report`` and another one at ``vss-cli compute vm report``, they would create their
custom python package with the ``vss-cli`` as a dependency, and add the following to their package's setuptools
entry-points in ``setup.py``:

.. code-block:: python

    #!/usr/bin/env python


    """
    Setup script for `new-plugin`
    """


    from setuptools import setup


    setup(
        name='new-plugin',
        version='0.1dev0',
        packages=['new_plugin'],
        install_requires=['vss-cli>=0.1.0']
        entry_points='''

        [vss_cli.contrib.compute.plugins]
        report=new_plugin.core:report

        [vss_cli.contrib.compute.vm.plugins]
        report=new_plugin.core:report
        '''
    )

Now, the plugin package ``new_plugin`` contains ``__init__.py`` and ``core.py``:

.. code-block:: python

    """
    Add custom report to `vss-cli`
    """

    import click
    import logging
    from vss_cli.helper import format_output
    from vss_cli.cli import pass_context

    _LOGGING = logging.getLogger(__name__)


    @click.command(
        'report'
    )
    @pass_context
    def report(ctx):
        """+Custom report plugin"""
        _LOGGING.debug(f'Running report')
        vms = ctx.get_vms(summary=1)
        click.echo(
            format_output(
                ctx,
                vms,
                columns=[
                   ('UUID', 'uuid'), ('NAME', 'name'),
                   ('IP', 'ipAddress')
                ],
            )
        )

After installing the plugin, the ``vss-cli`` will load the plugin in the defined scope:

.. code-block:: bash

    vss-cli compute --help

    Usage: vss-cli compute [OPTIONS] COMMAND [ARGS]...

      Compute related resources such as virtual machines, networks supported
      operating systems, logical folders, OVA/OVF images, floppy images, ISO
      images and more.

    Options:
      --help  Show this message and exit.

    Commands:
      domain     List compute domains.
      floppy     Manage floppy images.
      folder     Manage logical folders
      image      Manage personal and list public VM images.
      inventory  Manage inventory reports
      iso        Manage ISO images.
      net        List available virtual networks
      os         Supported OS.
      report     +Custom report plugin
      template   List virtual machine templates
      vm         Manage virtual machines


    vss-cli compute vm report --help

    Usage: vss-cli compute vm report [OPTIONS]

      +Custom report plugin

    Options:
      --help  Show this message and exit.


.. _`Latest version of git`: https://git-scm.com/downloads
.. _`PEP8`: https://pep8.org/
.. _`committing as you go`: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
.. _`create a merge request`: https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html
.. _`Fork`: https://gitlab-ee.eis.utoronto.ca/help/gitlab-basics/fork-project.md