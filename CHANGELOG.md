# Changelog 📝

## [v0.1.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.1) (2019-04-05)

**Improvements:**

- [#54](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54): ``docs``: Windows installation steps: by [jm.lopez]
- [#55](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55): ``core``: Handle advanced configuration editable by users and via CLI : by [jm.lopez]
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