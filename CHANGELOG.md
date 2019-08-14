# Changelog 📝

## [v0.2.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.1) (2019-08-14)

**Improvements:**
- [#129](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/129): `core`: pyvss upgrade from 0.9.38 -> 0.9.39: by [jm.lopez]
- [#131](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/131): `docs`: vmware paravirtual scsi migration how-to: by [jm.lopez]
- [#133](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/133): `core`: `vss` command as an alias of `vss-cli`: by [jm.lopez]

**Bug Fixes:**
- [#130](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/130): `core`: `config.get_vm_by_uuid_or_name` cannot find templates: by [jm.lopez]
- [#132](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/132): `core`: `config.get_vm_by_uuid_or_name` cannot find vms: by [jm.lopez]

## [v0.2.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.0) (2019-07-26)

**Improvements:**
- [#125](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/125): `core`: pyvss upgrade from 0.9.36 -> 0.9.38: by [jm.lopez]
- [#124](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/124): `compute vm ls`: add options to filter and sort  [jm.lopez]
- [#126](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/126): `compute template ls`: add options to filter and sort  [jm.lopez]
- [#127](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/127): `compute vm set disk up --backing-mode`: updates scsi controller used by disk: by [jm.lopez]

## [v0.1.9](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.9) (2019-07-19)

**Improvements:**
- [#122](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/122): `core`: removing config.update_vm_floppy in favour of pyvss: by [jm.lopez]
- [#121](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/121): `core`: pyvss upgrade from 0.9.35 -> 0.9.36: by [jm.lopez]
- [#119](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/119): `compute vm get controller scsi`: command update: by [jm.lopez]
- [#118](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/118): `compute vm get disk scsi`: provides scsi controller used by disk: by [jm.lopez]
- [#117](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/117): `compute vm set disk up --scsi`: updates scsi controller used by disk: by [jm.lopez]
- [#116](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/116): `compute folder get children`: gets children folder of a given folder: by [jm.lopez]
- [#115](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/115): `compute folder get vm`: command update: by [jm.lopez]
- [#114](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/114): `compute folder ls`: add options to filter and sort  [jm.lopez]

**New Features:**
- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): `compute vm set controller scsi mk`: create vm scsi controllers: by [jm.lopez]
- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): `compute vm set controller scsi up`: update vm scsi controllers: by [jm.lopez]
- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): `compute vm set controller scsi rm`: remove vm scsi controllers: by [jm.lopez]


## [v0.1.8](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.8) (2019-07-10)

**Improvements:**
- [#109](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/109): `core`: pyvss upgrade from 0.9.34 -> 0.9.35: by [jm.lopez]
- [#107](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/107): `compute net ls`: add new options to filter and sort: by [jm.lopez]
- [#108](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/108): `compute net get`: update vms command backend: by [jm.lopez]
- [#111](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/111): `compute vm set floppy`: improve image lookup and handling: by [jm.lopez]

**Bug Fixes:**
- [#106](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/106): `docs`: project links > documentation typo in project docs url: by [jm.lopez]
- [#110](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/110): `compute vm set nic mk`: error when creating cards: by [jm.lopez]
- [#112](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/112): `compute vm set client`: update_vm_vss_client missing positional argument: by [jm.lopez]


## [v0.1.7](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.7) (2019-06-27)

**Improvements:**
- [#103](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/103): `core`: update pyvss to 0.9.34: by [jm.lopez]
- [#102](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/102): `compute vm get`: provide floppy attribute: by [jm.lopez]
- [#104](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104): `compute vm set cd mk`: create cd/dvd devices: by [jm.lopez]
- [#104](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104): `compute vm set cd up`: update cd/dvd devices: by [jm.lopez]

**Bug Fixes:**
- [#101](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/101): `compute floppy personal sync`: fails to sync floppy images: by [jm.lopez]

## [v0.1.6](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.6) (2019-05-24)

**Improvements:**
- [#99](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/99): `core`: update pyvss to 0.9.33: by [jm.lopez]

**Bug Fixes:**
- [#98](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/98): ``compute vm get nic``: command missing network moref using table format: by [jm.lopez]

## [v0.1.5](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.5) (2019-05-14)

**Improvements:**

- [#90](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/90): `compute vm get spec`: generates a VSS-CLI specification: by [jm.lopez]
- [#91](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/91): `compute vm mk from-file`: checks for VSS CLI specification: by [jm.lopez]
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): `compute vm set extra-cfg mk`: create `guestinfo` option: by [jm.lopez]
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): `compute vm set extra-cfg up`: update `guestinfo` option: by [jm.lopez]
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): `compute vm set extra-cfg rm`: remove `guestinfo` option: by [jm.lopez]
- [#95](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/95): `compute vm get console`: option to generate link for a given client (html5, flash, vmrc): by [jm.lopez]
- [#96](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/96): `core`: ruamel.yaml upgrade from 0.15.92 -> 0.15.94: by [jm.lopez]
- [#97](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/97): `core`: pyvss upgrade from 0.9.30 -> 0.9.32: by [jm.lopez]

**Bug Fixes:**

- [#93](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/93): `core`: autocompletion is not working properly with multi-endpoint configuration: by [jm.lopez]

## [v0.1.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.4) (2019-05-06)

**Improvements:**

- [#82](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/82): `core`: setup.cfg improvements: by [jm.lopez]
- [#85](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/85): `core`: upgrade to py-vss v0.9.30: by [jm.lopez]
- [#86](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/86): `token`: ls/get columns: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `token`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `service`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `message`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `key`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `compute floppy`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `compute image`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `compute iso`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `compute os`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request change`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request new`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request export`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request folder`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request image`: ls standardizing relational options: by [jm.lopez]
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): `request inventory`: ls standardizing relational options: by [jm.lopez]

**Bug Fixes:**

- [#83](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/83): `ci`: CI/Docker Job Failed #17142: by [jm.lopez]
- [#87](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/87): `compute`: vm st snapshot rm - Unable to delete snapshot: by [jm.lopez]

## [v0.1.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.3) (2019-04-18)

**Improvements:**

- [#69](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/69): `core`: Implement ruamel.yaml for yaml mgmt: by [jm.lopez]
- [#72](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/72): `core`: spinner improvements: by [jm.lopez]
- [#78](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/78): `core`: emoji handling/rendering improvements: by [jm.lopez]
- [#79](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/79): `stor`: general improvements: by [jm.lopez]

**Bug Fixes:**

- [#68](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/68): `core`: options are overridden by configuration file: by [jm.lopez]
- [#71](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/71): `upgrade`: stable does not occur due to a missing argument: by [jm.lopez]
- [#73](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/73): `service`: missing column name in table format: by [jm.lopez]
- [#74](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/74): `core`: config.py aka ctx does not match services available: by [jm.lopez]
- [#75](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/75): `configure mk`: missing default endpoint: by [jm.lopez]
- [#76](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/76): `configure migrate`: unhandled exception with invalid configuration file: by [jm.lopez]
- [#77](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/77): `configure set`: cannot change default_endpoint_name when invalid endpoint is found: by [jm.lopez]
- [#80](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/80): `status`: command fails when there's no input format selected.: by [jm.lopez]

## [v0.1.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.2) (2019-04-12)

**Improvements:**

- [#67](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/67): ``core``: Provide user feedback while CLI processing [jm.lopez]

**Bug Fixes:**

- [#65](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/65): ``core``: configure command mismatch from autocompletion [jm.lopez]
- [#66](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/66): ``core``: configure upgrade missing description [jm.lopez]


## [v0.1.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.1) (2019-04-05)

**Improvements:**

- [#54](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54): ``docs``: Windows installation steps: by [jm.lopez]
- [#55](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55): ``core``: Handle advanced configuration editable by users and via CLI: by [jm.lopez]
- [#57](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/57): ``docs``: docs/Add man page build and deploy stage to pipeline: by [jm.lopez]

**Bug Fixes:**

- [#63](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/63): ``compute floppy|folder|net``: invalid context in compute, floppy, folder and network commands: by [jm.lopez]
- [#61](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/61): ``core``: pyvss/AttributeError: 'Configuration' object has no attribute 'get_vss_services': by [jm.lopez]
- [#59](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/59): ``account set notification request``: missing command account/set/notification/request: by [jm.lopez]
- [#58](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/58): ``message get``: message/get does not provide auto-completion: by [jm.lopez]
- [#56](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/56): ``upgrade``: vss-cli upgrade fails when there's no pip: by [jm.lopez]

**New Features:**

- [#62](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/62): ``request change set scheduled``: request/change/set scheduled and scheduled_datetime: by [jm.lopez]


## [v0.1.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.0) (2019-03-29)

**Improvements:**

- [#43](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/43): ``compute vm get spec``: download spec and save to file (yaml or json): by [jm.lopez]
- [#50](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/50): ``upgrade``: command to support multiple code branches: by [jm.lopez]
- [#41](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/41): ``completion bash|zsh``: Auto-completion for managed objects: by [jm.lopez]
- [#32](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/32): ``docs``: Migrate documentation to new vss-cli command structure: by [jm.lopez]
- [#48](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/48): ``plugins``: Support externally-installable plugins: by [jm.lopez]
- [#40](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/40): ``tests``: Migrate Unit Testing from legacy VSSCLI: by [jm.lopez]
- [#37](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/37): ``ci``: Add bump2version to project to manage versioning: by [jm.lopez]
- [#36](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/36): ``ci``: Add GitLab Templates: by [jm.lopez]
- [#51](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/51): ``ci``: Implement ``isort`` and ``flake8`` in configuration file ``setup.cfg``: by [jm.lopez]
- [#42](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/42): ``compute vm mk from-file``:  improve vm creation with VSS-CLI specification file: by [jm.lopez], [alex.tremblay]
- [#53](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/53): ``vss-cli``: support externally-installable plugins scope improvement: by [alex.tremblay]

**Bug Fixes:**

- [#49](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/49): ``compute vm set --schedule``: not working properly: by [jm.lopez]
- [#44](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/44): ``vss-cli``: Auto-completion does not prioritize env var over files: by [jm.lopez]
- [#45](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/45): ``vss-cli --timeout``: Configuration.timeout not implemented: by [jm.lopez]

**New Features:**

- [#13](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/13): ``vss-cli``: Migrate VSSCLI to VSSCLI-NG: by [jm.lopez]
- [#4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/4): ``configure``: Configure VSS CLI options: by [jm.lopez]
- [#20](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/20): ``compute``: Manage VMs, networks, folders, etc: by [jm.lopez]
- [#22](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/22): ``compute domain``: List domains available: by [jm.lopez]
- [#28](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/28): ``compute floppy``: Manage floppy images: by [jm.lopez]
- [#30](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/30): ``compute folder``: Manage logical folders: by [jm.lopez]
- [#27](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/27): ``compute image`` : Manage your OVA/OVF images: by [jm.lopez]
- [#24](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/24): ``compute inventory``: Manage inventory reports: by [jm.lopez]
- [#29](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/29): ``compute iso``: Manage ISO images: by [jm.lopez]
- [#25](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/25): ``compute net``: List available virtual networks: by [jm.lopez]
- [#26](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/26): ``compute os``: Supported OS: by [jm.lopez]
- [#31](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/31): ``compute template``: List virtual machine templates: by [jm.lopez]
- [#33](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/33): ``compute vm``: Manage virtual machines: by [jm.lopez]
- [#46](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/46): ``compute vm set|get vss-option``: Manage VSS options: by [jm.lopez]
- [#47](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/47): ``compute vm get|set vss-service``: Manage VSS Services: by [jm.lopez]
- [#23](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/23): ``shell``: REPL interactive shell: by [jm.lopez]
- [#18](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/18): ``stor``: Manage your personal storage space: by [jm.lopez]
- [#12](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/12): ``status``: Check VSS Status: by [jm.lopez]
- [#14](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/14): ``upgrade``: Upgrade VSS CLI and dependencies (experimental): by [jm.lopez]
- [#1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/): `` equest``: Manage your different requests history: by [jm.lopez]
- [#15](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/15): ``token``: Manage your API tokens: by [jm.lopez]
- [#17](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/17): ``account``: Manage your VSS account: by [jm.lopez]
- [#16](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/16): ``message``: Manage user messages: by [jm.lopez]
- [#19](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/19): ``key``: Manage your SSH Public Keys: by [jm.lopez]
- [#34](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/34): ``raw``: Raw calls to API: by [jm.lopez]


[jm.lopez]: https://gitlab-ee.eis.utoronto.ca/jm.lopez
[alex.tremblay]: https://gitlab-ee.eis.utoronto.ca/alex.tremblay