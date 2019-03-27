=========
Changelog
=========

v0.1.0
======

**Improvements:**

- `#43`_: ``compute vm get spec`` download spec and save to file (yaml or json): by `jm.lopez`_
- `#50`_: ``upgrade`` command to support multiple code branches: by `jm.lopez`_
- `#41`_: ``completion bash|zsh``: Auto-completion for managed objects: by `jm.lopez`_
- `#32`_: ``docs``: Migrate documentation to new vss-cli command structure: by `jm.lopez`_
- `#48`_: ``plugins``: Support externally-installable plugins: by `jm.lopez`_
- `#40`_: ``tests``: Migrate Unit Testing from legacy VSSCLI: by `jm.lopez`_
- `#37`_: ``ci``: Add bump2version to project to manage versioning: by `jm.lopez`_
- `#36`_: ``ci``: Add GitLab Templates: by `jm.lopez`_
- `#51`_: ``ci``: Implement ``isort`` and ``flake8`` in configuration file ``setup.cfg``: by `jm.lopez`_
- `#42`_: ``compute vm mk from-file``:  improve vm creation with VSS-CLI specification files: by `jm.lopez`_, `alex.tremblay`_
- `#53`_: ``vss-cli``: support externally-installable plugins scope improvement: by `alex.tremblay`_


**Bug Fixes:**

- `#49`_: ``compute vm set --schedule`` not working properly: by `jm.lopez`_
- `#44`_: ``vss-cli`` Auto-completion does not prioritize env var over files: by `jm.lopez`_
- `#45`_: ``vss-cli --timeout``: Configuration.timeout not implemented: by `jm.lopez`_

**New Features:**

- `#13`_: ``vss-cli``: Migrate VSSCLI to VSSCLI-NG: by `jm.lopez`_
- `#4`_ : ``configure``: Configure VSS CLI options: by `jm.lopez`_
- `#20`_: ``compute``: Manage VMs, networks, folders, etc: by `jm.lopez`_
- `#22`_: ``compute domain``: List domains availabl: by `jm.lopez`_
- `#28`_: ``compute floppy``: Manage floppy images: by `jm.lopez`_
- `#30`_: ``compute folder``: Manage logical folders: by `jm.lopez`_
- `#27`_: ``compute image`` : Manage your OVA/OVF images: by `jm.lopez`_
- `#24`_: ``compute inventory``: Manage inventory report: by `jm.lopez`_
- `#29`_: ``compute iso``: Manage ISO images: by `jm.lopez`_
- `#25`_: ``compute net``: List available virtual networks: by `jm.lopez`_
- `#26`_: ``compute os``: Supported OS: by `jm.lopez`_
- `#31`_: ``compute template``: List virtual machine template: by `jm.lopez`_
- `#33`_: ``compute vm``: Manage virtual machines: by `jm.lopez`_
- `#46`_: ``compute vm set|get vss-option``: Manage VSS option: by `jm.lopez`_
- `#47`_: ``compute vm get|set vss-service``: Manage VSS Service: by `jm.lopez`_
- `#23`_: ``shell``: REPL interactive shell: by `jm.lopez`_
- `#18`_: ``stor``: Manage your personal storage space: by `jm.lopez`_
- `#12`_: ``status``: Check VSS Status: by `jm.lopez`_
- `#14`_: ``upgrade``: Upgrade VSS CLI and dependencies (experimental): by `jm.lopez`_
- `#1`_ : ``request``: Manage your different requests history: by `jm.lopez`_
- `#15`_: ``token``: Manage your API tokens: by `jm.lopez`_
- `#17`_: ``account``: Manage your VSS account: by `jm.lopez`_
- `#16`_: ``message``: Manage user messages: by `jm.lopez`_
- `#19`_: ``key``: Manage your SSH Public Keys: by `jm.lopez`_


.. Links to issues section

.. _`#53`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/53
.. _`#51`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/51
.. _`#50`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/50
.. _`#49`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/49
.. _`#48`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/48
.. _`#47`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/47
.. _`#46`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/46
.. _`#45`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/45
.. _`#44`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/44
.. _`#43`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/43
.. _`#42`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/42
.. _`#41`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/41
.. _`#40`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/40
.. _`#39`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/39
.. _`#38`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/38
.. _`#37`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/37
.. _`#36`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/36
.. _`#35`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/35
.. _`#34`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/34
.. _`#33`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/33
.. _`#32`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/32
.. _`#31`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/31
.. _`#30`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/30
.. _`#20`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/20
.. _`#21`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/21
.. _`#22`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/22
.. _`#23`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/23
.. _`#24`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/24
.. _`#25`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/25
.. _`#26`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/26
.. _`#27`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/27
.. _`#28`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/28
.. _`#29`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/29
.. _`#10`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/10
.. _`#11`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/11
.. _`#12`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/12
.. _`#13`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/13
.. _`#14`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/14
.. _`#15`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/15
.. _`#16`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/16
.. _`#17`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/17
.. _`#18`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/18
.. _`#19`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/19
.. _`#1`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/1
.. _`#4`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/4

.. Contributors

.. _`jm.lopez`: https://gitlab-ee.eis.utoronto.ca/jm.lopez
.. _`alex.tremblay`: https://gitlab-ee.eis.utoronto.ca/alex.tremblay