=========
Changelog
=========

v0.1.4
======

**Improvements:**
- `#82`_: ``core``: setup.cfg improvements: by `jm.lopez`_
- `#85`_: ``core``: upgrade to py-vss v0.9.30: by `jm.lopez`_
- `#86`_: ``token``: ls/get columns: by `jm.lopez`_
- `#88`_: ``token``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``service``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``message``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``key``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``compute floppy``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``compute image``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``compute iso``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``compute os``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request change``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request new``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request export``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request folder``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request image``: ls standardizing relational options: by `jm.lopez`_
- `#88`_: ``request inventory``: ls standardizing relational options: by `jm.lopez`_

**Bug Fixes:**
- `#83`_: ``ci``: CI/Docker Job Failed #17142: by `jm.lopez`_
- `#87`_: ``compute``: vm st snapshot rm - Unable to delete snapshot: by `jm.lopez`_

v0.1.3
======

**Improvements:**

- `#69`_: ``core``: Implement ruamel.yaml for yaml mgmt: by `jm.lopez`_
- `#72`_: ``core``: spinner improvements: by `jm.lopez`_
- `#78`_: ``core``: emoji handling/rendering improvements: by `jm.lopez`_
- `#79`_: ``stor``: general improvements : by `jm.lopez`_

**Bug Fixes:**

- `#68`_: ``core``: options are overridden by configuration file: by `jm.lopez`_
- `#71`_: ``upgrade``: stable does not occur due to a missing argument: by `jm.lopez`_
- `#73`_: ``service``: missing column name in table format: by `jm.lopez`_
- `#74`_: ``core``: config.py aka ctx does not match services available: by `jm.lopez`_
- `#75`_: ``configure mk``: missing default endpoint: by `jm.lopez`_
- `#76`_: ``configure migrate``: unhandled exception with invalid configuration file: by `jm.lopez`_
- `#77`_: ``configure set``: cannot change default_endpoint_name when invalid endpoint is found: by `jm.lopez`_
- `#80`_: ``status``: command fails when there's no input format selected. : by `jm.lopez`_

v0.1.2
======

**Improvements:**

- `#67`_: ``core``: Provide user feedback while CLI processing: by `jm.lopez`_

**Bug Fixes:**

- `#65`_: ``configure``: command mismatch from auto-completion: by `jm.lopez`_
- `#66`_: ``configure``: upgrade missing description: by `jm.lopez`_

v0.1.1
======

**Improvements:**

- `#54`_: ``docs``: Windows installation steps: by `jm.lopez`_
- `#55`_: ``core``: Handle advanced configuration editable by users and via CLI : by `jm.lopez`_
- `#57`_: ``docs``: docs/Add man page build and deploy stage to pipeline: by `jm.lopez`_

**Bug Fixes:**

- `#63`_: ``compute floppy|folder|net``: invalid context in compute, floppy, folder and network commands: by `jm.lopez`_
- `#61`_: ``core``: pyvss/AttributeError: 'Configuration' object has no attribute 'get_vss_services': by `jm.lopez`_
- `#59`_: ``account set notification request``: missing command account/set/notification/request: by `jm.lopez`_
- `#58`_: ``message get``: message/get does not provide auto-completion: by `jm.lopez`_
- `#56`_: ``upgrade``: vss-cli upgrade fails when there's no pip: by `jm.lopez`_

**New Features:**

- `#62`_: ``request change set scheduled``: request/change/set scheduled and scheduled_datetime: by `jm.lopez`_

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


.. _`#88`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88
.. _`#87`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/87
.. _`#86`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/86
.. _`#85`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/85
.. _`#83`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/83
.. _`#82`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/82
.. _`#80`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/80
.. _`#79`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/79
.. _`#78`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/78
.. _`#77`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/77
.. _`#76`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/76
.. _`#75`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/75
.. _`#74`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/74
.. _`#73`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/73
.. _`#72`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/72
.. _`#71`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/71
.. _`#70`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/70
.. _`#69`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/69
.. _`#68`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/68
.. _`#67`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/67
.. _`#66`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/66
.. _`#65`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/65
.. _`#63`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/63
.. _`#62`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/62
.. _`#61`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/61
.. _`#60`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/60
.. _`#59`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/59
.. _`#58`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/58
.. _`#57`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/57
.. _`#56`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/56
.. _`#55`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55
.. _`#54`: https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54
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