=========
Changelog
=========

`v0.2.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.0>`_ (2019-07-26)
==================================================================================

**Improvements:**

- `#125 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/125>`_: ``core``: pyvss upgrade from 0.9.36 -> 0.9.38: by `jm.lopez`_
- `#124 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/124>`_: ``compute vm ls``: add options to filter and sort: by `jm.lopez`_
- `#126 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/126>`_: ``compute template ls``: add options to filter and sort: by `jm.lopez`_
- `#127 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/127>`_: ``compute vm set disk up --backing-mode``: updates scsi controller used by disk: by `jm.lopez`_


`v0.1.9 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.9>`_ (2019-07-19)
==================================================================================

**Improvements:**

- `#122 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/122>`_: ``core``: removing config.update_vm_floppy in favour of pyvss: by `jm.lopez`_
- `#121 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/121>`_: ``core``:` pyvss upgrade from 0.9.35 -> 0.9.36: by `jm.lopez`_
- `#119 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/119>`_: ``compute vm get controller scsi``: command update: by `jm.lopez`_
- `#118 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/118>`_: ``compute vm get disk scsi``: provides scsi controller used by disk: by `jm.lopez`_
- `#117 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/117>`_: ``compute vm set disk up --scsi``: updates scsi controller used by disk: by `jm.lopez`_
- `#116 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/116>`_: ``compute folder get children``: gets children folder of a given folder: by `jm.lopez`_
- `#115 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/115>`_: ``compute folder get vm``: command update: by `jm.lopez`_
- `#114 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/114>`_: ``compute folder ls``: add options to filter and sort  `jm.lopez`_

**New Features:**

- `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_: ``compute vm set controller scsi mk``: create vm scsi controllers: by `jm.lopez`_
- `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_: ``compute vm set controller scsi up``: update vm scsi controllers: by `jm.lopez`_
- `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_: ``compute vm set controller scsi rm``: remove vm scsi controllers: by `jm.lopez`_


`v0.1.8 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.8>`_ (2019-07-10)
==================================================================================

**Improvements:**

- `#109 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/109>`_: ``core``: pyvss upgrade from 0.9.34 -> 0.9.35: by `jm.lopez`_
- `#107 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/107>`_: ``compute net ls``: add new options to filter and sort: by `jm.lopez`_
- `#108 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/108>`_: ``compute net get``: update vms command backend: by `jm.lopez`_
- `#111 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/111>`_: ``compute vm set floppy``: improve image lookup and handling: by `jm.lopez`_

**Bug Fixes:**

- `#106 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/106>`_: ``docs``: project links > documentation typo in project docs url: by `jm.lopez`_
- `#110 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/110>`_: ``compute vm set nic mk``: error when creating cards: by `jm.lopez`_
- `#112 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/112>`_: ``compute vm set client``: update_vm_vss_client missing positional argument: by `jm.lopez`_


`v0.1.7 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.7>`_ (2019-06-27)
==================================================================================

**Improvements:**

- `#103 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/103>`_: ``core``: update pyvss to 0.9.34: by `jm.lopez`_
- `#102 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/102>`_: ``compute vm get``: provide floppy attribute: by `jm.lopez`_
- `#104 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104>`_: ``compute vm set cd mk``: create cd/dvd devices: by `jm.lopez`_
- `#104 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104>`_: ``compute vm set cd up``: update cd/dvd devices: by `jm.lopez`_

**Bug Fixes:**

- `#101 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/101>`_: ``compute floppy personal sync``: fails to sync floppy images: by `jm.lopez`_

`v0.1.6 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.6>`_ (2019-05-24)
==================================================================================

**Improvements:**

- `#99 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/99>`_: update pyvss to 0.9.33: by `jm.lopez`_

**Bug Fixes:**

- `#98 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/98>`_: ``compute vm get nic``: command missing network moref using table format: by `jm.lopez`_


`v0.1.5 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.5>`_ (2019-05-14)
==================================================================================

**Improvements:**

- `#90 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/90>`_: ``compute vm get spec``: generates a VSS-CLI specification: by `jm.lopez`_
- `#91 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/91>`_: ``compute vm mk from-file``: checks for VSS CLI specification: by `jm.lopez`_
- `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_: ``compute vm set extra-cfg mk``: create ``guestinfo`` option: by `jm.lopez`_
- `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_: ``compute vm set extra-cfg up``: update ``guestinfo`` option: by `jm.lopez`_
- `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_: ``compute vm set extra-cfg rm``: remove ``guestinfo`` option: by `jm.lopez`_
- `#95 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/95>`_: ``compute vm get console``: option to generate link for a given client (html5, flash, vmrc): by `jm.lopez`_
- `#96 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/96>`_: ``core``: ruamel.yaml upgrade from 0.15.92 -> 0.15.94: by `jm.lopez`_
- `#97 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/97>`_: ``core``: pyvss upgrade from 0.9.30 -> 0.9.32: by `jm.lopez`_

**Bug Fixes:**

- `#93 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/93>`_: ``core``: autocompletion is not working properly with multi-endpoint configuration: by `jm.lopez`_

`v0.1.4 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.4>`_ (2019-05-06)
==================================================================================

**Improvements:**

- `#82 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/82>`_: ``core``: setup.cfg improvements: by `jm.lopez`_
- `#85 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/85>`_: ``core``: upgrade to py-vss v0.9.30: by `jm.lopez`_
- `#86 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/86>`_: ``token``: ls/get columns: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``token``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``service``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``message``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``key``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``compute floppy``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``compute image``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``compute iso``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``compute os``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request change``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request new``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request export``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request folder``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request image``: ls standardizing relational options: by `jm.lopez`_
- `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_: ``request inventory``: ls standardizing relational options: by `jm.lopez`_

**Bug Fixes:**

- `#83 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/83>`_: ``ci``: CI/Docker Job Failed #17142: by `jm.lopez`_
- `#87 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/87>`_: ``compute``: vm st snapshot rm - Unable to delete snapshot: by `jm.lopez`_

`v0.1.3 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.3>`_ (2019-04-18)
==================================================================================

**Improvements:**

- `#69 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/69>`_: ``core``: Implement ruamel.yaml for yaml mgmt: by `jm.lopez`_
- `#72 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/72>`_: ``core``: spinner improvements: by `jm.lopez`_
- `#78 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/78>`_: ``core``: emoji handling/rendering improvements: by `jm.lopez`_
- `#79 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/79>`_: ``stor``: general improvements : by `jm.lopez`_

**Bug Fixes:**

- `#68 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/68>`_: ``core``: options are overridden by configuration file: by `jm.lopez`_
- `#71 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/71>`_: ``upgrade``: stable does not occur due to a missing argument: by `jm.lopez`_
- `#73 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/73>`_: ``service``: missing column name in table format: by `jm.lopez`_
- `#74 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/74>`_: ``core``: config.py aka ctx does not match services available: by `jm.lopez`_
- `#75 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/75>`_: ``configure mk``: missing default endpoint: by `jm.lopez`_
- `#76 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/76>`_: ``configure migrate``: unhandled exception with invalid configuration file: by `jm.lopez`_
- `#77 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/77>`_: ``configure set``: cannot change default_endpoint_name when invalid endpoint is found: by `jm.lopez`_
- `#80 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/80>`_: ``status``: command fails when there's no input format selected. : by `jm.lopez`_

`v0.1.2 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.2>`_ (2019-04-12)
==================================================================================

**Improvements:**

- `#67 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/67>`_: ``core``: Provide user feedback while CLI processing: by `jm.lopez`_

**Bug Fixes:**

- `#65 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/65>`_: ``configure``: command mismatch from auto-completion: by `jm.lopez`_
- `#66 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/66>`_: ``configure``: upgrade missing description: by `jm.lopez`_

`v0.1.1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.1>`_ (2019-04-05)
==================================================================================

**Improvements:**

- `#54 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54>`_: ``docs``: Windows installation steps: by `jm.lopez`_
- `#55 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55>`_: ``core``: Handle advanced configuration editable by users and via CLI : by `jm.lopez`_
- `#57 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/57>`_: ``docs``: docs/Add man page build and deploy stage to pipeline: by `jm.lopez`_

**Bug Fixes:**

- `#63 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/63>`_: ``compute floppy|folder|net``: invalid context in compute, floppy, folder and network commands: by `jm.lopez`_
- `#61 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/61>`_: ``core``: pyvss/AttributeError: 'Configuration' object has no attribute 'get_vss_services': by `jm.lopez`_
- `#59 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/59>`_: ``account set notification request``: missing command account/set/notification/request: by `jm.lopez`_
- `#58 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/58>`_: ``message get``: message/get does not provide auto-completion: by `jm.lopez`_
- `#56 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/56>`_: ``upgrade``: vss-cli upgrade fails when there's no pip: by `jm.lopez`_

**New Features:**

- `#62 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/62>`_: ``request change set scheduled``: request/change/set scheduled and scheduled_datetime: by `jm.lopez`_

`v0.1.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.0>`_ (2019-03-29)
==================================================================================

**Improvements:**

- `#43 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/43>`_: ``compute vm get spec`` download spec and save to file (yaml or json): by `jm.lopez`_
- `#50 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/50>`_: ``upgrade`` command to support multiple code branches: by `jm.lopez`_
- `#41 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/41>`_: ``completion bash|zsh``: Auto-completion for managed objects: by `jm.lopez`_
- `#32 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/32>`_: ``docs``: Migrate documentation to new vss-cli command structure: by `jm.lopez`_
- `#48 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/48>`_: ``plugins``: Support externally-installable plugins: by `jm.lopez`_
- `#40 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/40>`_: ``tests``: Migrate Unit Testing from legacy VSSCLI: by `jm.lopez`_
- `#37 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/37>`_: ``ci``: Add bump2version to project to manage versioning: by `jm.lopez`_
- `#36 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/36>`_: ``ci``: Add GitLab Templates: by `jm.lopez`_
- `#51 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/51>`_: ``ci``: Implement ``isort`` and ``flake8`` in configuration file ``setup.cfg``: by `jm.lopez`_
- `#42 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/42>`_: ``compute vm mk from-file``:  improve vm creation with VSS-CLI specification files: by `jm.lopez`_, `alex.tremblay`_
- `#53 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/53>`_: ``vss-cli``: support externally-installable plugins scope improvement: by `alex.tremblay`_


**Bug Fixes:**

- `#49 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/49>`_: ``compute vm set --schedule`` not working properly: by `jm.lopez`_
- `#44 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/44>`_: ``vss-cli`` Auto-completion does not prioritize env var over files: by `jm.lopez`_
- `#45 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/45>`_: ``vss-cli --timeout``: Configuration.timeout not implemented: by `jm.lopez`_

**New Features:**

- `#13 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/13>`_: ``vss-cli``: Migrate VSSCLI to VSSCLI-NG: by `jm.lopez`_
- `#4 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/4>`_ : ``configure``: Configure VSS CLI options: by `jm.lopez`_
- `#20 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/20>`_: ``compute``: Manage VMs, networks, folders, etc: by `jm.lopez`_
- `#22 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/22>`_: ``compute domain``: List domains availabl: by `jm.lopez`_
- `#28 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/28>`_: ``compute floppy``: Manage floppy images: by `jm.lopez`_
- `#30 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/30>`_: ``compute folder``: Manage logical folders: by `jm.lopez`_
- `#27 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/27>`_: ``compute image`` : Manage your OVA/OVF images: by `jm.lopez`_
- `#24 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/24>`_: ``compute inventory``: Manage inventory report: by `jm.lopez`_
- `#29 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/29>`_: ``compute iso``: Manage ISO images: by `jm.lopez`_
- `#25 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/25>`_: ``compute net``: List available virtual networks: by `jm.lopez`_
- `#26 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/26>`_: ``compute os``: Supported OS: by `jm.lopez`_
- `#31 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/31>`_: ``compute template``: List virtual machine template: by `jm.lopez`_
- `#33 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/33>`_: ``compute vm``: Manage virtual machines: by `jm.lopez`_
- `#46 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/46>`_: ``compute vm set|get vss-option``: Manage VSS option: by `jm.lopez`_
- `#47 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/47>`_: ``compute vm get|set vss-service``: Manage VSS Service: by `jm.lopez`_
- `#23 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/23>`_: ``shell``: REPL interactive shell: by `jm.lopez`_
- `#18 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/18>`_: ``stor``: Manage your personal storage space: by `jm.lopez`_
- `#12 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/12>`_: ``status``: Check VSS Status: by `jm.lopez`_
- `#14 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/14>`_: ``upgrade``: Upgrade VSS CLI and dependencies (experimental): by `jm.lopez`_
- `#1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/1>`_ : ``request``: Manage your different requests history: by `jm.lopez`_
- `#15 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/15>`_: ``token``: Manage your API tokens: by `jm.lopez`_
- `#17 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/17>`_: ``account``: Manage your VSS account: by `jm.lopez`_
- `#16 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/16>`_: ``message``: Manage user messages: by `jm.lopez`_
- `#19 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/19>`_: ``key``: Manage your SSH Public Keys: by `jm.lopez`_


.. Contributors

.. _`jm.lopez`: https://gitlab-ee.eis.utoronto.ca/jm.lopez
.. _`alex.tremblay`: https://gitlab-ee.eis.utoronto.ca/alex.tremblay