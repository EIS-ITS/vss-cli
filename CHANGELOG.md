# Changelog 📝

## [v2025.7.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2025.7.0) (2025-07-14)

**Bug Fixes:**

- [#773](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/773): ``compute vm mk from-file``: logging too high.
- [#774](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/774): ``mcp``: properly handle import error.
- [#777](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/777): ``compute template rm``: removes running vms.

**Improvements:**

- [#775](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/775): ``homebrew``: formula for vss-cli add mcp-vss.
- [#776](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/776): ``assist``: update retrieval format.

## [v2025.6.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2025.6.1) (2025-06-27)

**Bug Fixes:**

- [#766](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/766): ``docs``: confluence pipeline failed.
- [#768](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/768): ``compute vm mk from-file``: spec not properly parsed
- [#769](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/769): ``homebrew``: missing dependency mcp
- [#770](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/770): ``compute vm set domain``: docstring 

## [v2025.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2025.6.0) (2025-06-26)

**Improvements:**

- [#759](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/759): ``ci``: implement ``uv`` and ``pyproject.toml`` in favour of setup tools
- [#760](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/760): ``compute vm get metrics``: additional counters ``disk``.
- [#761](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/761): ``core``: Upgrade ``dataclasses-json`` to ``0.6.7``.
- [#763](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/763): ``docs``: docs/update install method.
- [#764](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/764): ``homebrew``: formula improvements: add mcp to install.


**New Features:**

- [#762](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/762): ``mcp``: command to run and install to the Model Context Protocol Server.

**Bug Fixes:**

- [#757](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/757): ``core``: autocompletion fix for networks and folders.
- [#758](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/758): ``request ls``: missing username attribute 


## [v2025.2.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2025.2.1) (2025-02-21)

**Improvements:**

- [#750](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/750): ``docs``: improving examples titles.
- [#751](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/751): ``core``: upgrade ``pyvss`` to ``v2025.2.1``.
- [#752](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/752): ``compute vm get encryption``: add command to obtain current vm encryption status.
- [#753](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/753): ``compute vm set encryption``: add command to set vm encryption status.
- [#754](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/754): ``ci``: upgrade pip before installing setup tools.

## [v2025.2.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2025.2.0) (2025-02-13)

**Improvements:**

- [#737](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/737): ``docs``: pvscsi example update.
- [#738](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/738): ``core``: upgrade ``clikc`` from 8.1.7 to 8.1.8.
- [#739](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/739): ``core``: upgrade ``sphinxcontrib-confluencebuilder`` to 2.10.1.
- [#740](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/740): ``core``: upgrade ``minio`` from 7.2.8 to 7.2.15.
- [#741](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/741): ``homebrew``: formula improvements: add stor to installation.
- [#742](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/742): ``core``: upgrade ``jsonpath-ng`` to v1.7.0.
- [#743](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/743): ``core``: upgrade ``dateparser`` from 1.2.0 to 1.2.1.
- [#744](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/744): ``core``: upgrade ``rich`` to 13.9.4.
- [#745](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/745): ``core``: upgrade ``validators`` to 0.34.0.
- [#746](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/746): ``core``: upgrade ``setuptools`` to 75.8.0.

## [v2024.10.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.10.0) (2024-10-31)

**Improvements:**

- [#731](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/731): ``assist``: increase retrieval results to 5.
- [#732](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/732): ``docs``: add ``cli`` specification documentation
- [#733](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/733): ``compute vm get spec``: add ``scsi`` controller reference to spec
- [#734](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/734): ``compute vm get spec``: add ``iso`` if mounted.
- [#734](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/734): ``compute vm get spec-api``: add ``iso`` if mounted.

## [v2024.9.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.9.0) (2024-09-25)

**Improvements:**

- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request change ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request export ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request folder ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request image ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request new ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request restore ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request retire ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request snapshot ls``: show group requests.
- [#727](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/727): ``request vmdk ls``: show group requests.
- [#728](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/728): ``assist``: add note about always checking for references.

## [v2024.8.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.8.1) (2024-08-30)

**Improvements:**

- [#722](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/722): ``compute vm set client-note``: improvements to set ``--action`` default to ``up``.
- [#723](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/723): ``core``: upgrade ``dateparser`` from 1.1.8 to 1.2.0.
- [#724](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/724): ``core``: upgrade ``validators`` from 0.2.0 to 0.33.0.

## [v2024.8.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.8.0) (2024-08-29)

**Improvements:**

- [#717](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/717): ``assist``: additional attributes in payload required.
- [#718](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/718): ``docs``: libs upgrade ``sphinxcontrib-confluencebuilder`` 2.7.1.
- [#719](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/719): ``core``: upgrade ``minio`` from 7.2.7 to 7.2.8.

## [v2024.7.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.7.2) (2024-07-17)

**Improvements:**

- [#709](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/709): ``assist``: minor improvements.
- [#713](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/713): ``homebrew``: update formula to python 3.11.
- [#714](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/714): ``core``: minimum ``python`` version 3.8.5.

**Bug Fixes:**

- [#708](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/708): ``core``: error with `importlib.resources`.
- [#712](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/712): ``importlib-resources`` and ``importlib-metadata`` version requirements

## [v2024.7.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.7.0) (2024-07-12)

**New Features:**

- [#702](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/702): ``assist``: command to provide access to the ITS Private cloud AI assistant

**Improvements:**

- [#703](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/703): ``core``:  replace ``pygments`` with ``rich`` to increase console printing functionality.
- [#704](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/704): ``docs``:  title improvements for answer engine optimization.
- [#705](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/705): ``plugins``:  implement ``importlib-resources`` and ``importlib-metadata`` to replace ``pkg_resources``.

**Bug Fixes:**

- [#701](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/701): ``docs``: client note doc outdated.

## [v2024.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.6.0) (2024-06-05)

**Improvements:**

- [#694](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/694): ``vpn``: commands to handle new VSS VPN MFA implementation.
- [#695](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/695): ``core``: handle mandatory multi-factor authentication.
- [#696](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/696): ``core``: upgrade ``pyvss`` to ``v2024.6.0``.
- [#697](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/697): ``core``: Homebrew formula for ``vss-cli`` version ``2024.6.0``.
- [#699](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/699): ``ci``: update gitlab templates.
- [#700](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/700): ``ci``: replace ``CI_BUILD_TAG`` with ``CI_COMMIT_TAG``.

## [v2024.5.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2024.5.0) (2024-05-24)

**Improvements:**

- [#684](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/684):  ``compute vm get controller``: add ``usb`` and ``usb-xhci`` counts.
- [#685](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/685): ``ci``: moving pipeline to use ``CI_REGISTRY_USER`` and ``CI_REGISTRY_PASSWORD``.
- [#686](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/686): ``core``: upgrade ``sphinxcontrib-confluencebuilder`` to ``7.2.7``.
- [#687](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/687): ``core``: upgrade ``minio`` to ``2.5.2``.
- [#688](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/688): ``core``: upgrade ``pyvss`` to ``v2024.5.0``.
- [#689](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/689): ``compute vm get controller usb``: get existing ``usb`` controllers.
- [#689](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/689): ``compute vm get controller usb-xhci``: get existing ``usb-xhci`` controllers.
- [#690](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/690): ``core``: implement ``importlib-resources`` and ``importlib-metadata`` to replace ``pkg_resources``.
- [#693](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/693): ``core``: Homebrew formula for ``vss-cli`` version ``2024.5.0``.


**Bug Fixes:**

- [#683](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/683): ``ovf get``: error when label is missing.
- [#691](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/691): ``core``: ``--totp`` option env variable should be ``VSS_USER_OTP``.

## [v2023.12.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.12.1) (2023-12-15)

**Improvements:**

- [#681](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/681): ``compute vm res``: add confirmation message.
- [#682](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/682): ``core``: Homebrew formula for ``vss-cli`` v2023.12.1.

## [v2023.12.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.12.0) (2023-12-13)

**Improvements:**

- [#676](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/676): ``core``: upgrade ``pyvss`` from ``2023.11.0`` to ``2023.12.0``.
- [#675](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/675): ``compute vm set gpu mk``: add vGPU to virtual machine.
- [#675](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/675): ``compute vm set gpu rm``: remove vGPU from virtual machine.
- [#675](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/675): ``compute vm set gpu update``: update vGPU profile.
- [#674](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/674): ``raw``: support ``--table-format`` and ``--output``.

## [v2023.11.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.11.1) (2023-11-20)

**Improvements:**

- [#671](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/671): ``compute vm set memory reservation``: set memory reservation.

## [v2023.11.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.11.0) (2023-11-16)

**Improvements:**

- [#664](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/664): ``compute vm set disk cp``: to copy virtual disks across VMs.
- [#665](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/665): ``core``: ``setuptools`` version ``68.2.2``.
- [#666](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/666): ``core``: ``filter_bojects_by_attrs`` match a set of named attributes.
- [#667](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/667): ``ci``: ``pre-commit`` hook updates.
- [#666](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/666): ``core``: upgrade ``pyvss`` from ``2023.10.0`` to ``2023.11.0``.

## [v2023.10.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.10.0) (2023-10-30)

**Improvements:**

- [#657](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/657): ``ovf get`` support for in Product section ``PropertyParams``.
- [#659](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/659): ``compute vm res`` to restore from available restore points.
- [#660](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/660): ``core``: upgrade ``pyvss`` from ``2023.9.0`` to ``2023.10.0``.
- [#661](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/661): ``request restore``: command to browse restore requests.


**Bug Fixes:**

- [#658](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/658): ``compute vm mk from-file`` spec ``metadata.inform`` help required.

## [v2023.9.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.9.0) (2023-09-29)

**Improvements:**

- [#644](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/644): ``compute vm mk from-file``: clone set source networking and ``machine.disks`` if not specified.
- [#647](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/647): ``core``: upgrade ``minio`` from ``7.1.13`` to ``7.1.17``.
- [#648](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/648): ``core``: upgrade ``dateparser`` from ``1.1.4`` to ``1.1.8``.
- [#649](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/649): ``compute domain get``: show ``gpu_profiles``.
- [#650](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/650): ``core``: upgrade ``pyvss`` from ``2023.6.0`` to ``2023.9.0``.
- [#652](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/652): ``compute vm set client-note``: allow deletion with ``--action del``.
- [#653](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/653): ``compute vm get gpu``: get gpu devices.
- [#654](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/654): ``compute vm get restore-point``: get restore points.

**Bug Fixes:**

- [#645](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/645): ``docs``: example pvscsi incorrect option.
- [#646](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/646): ``compute vm mk from-file``: ignores ``machine.memory`` in vss-cli configuration spec (``shell``).
- [#651](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/651): ``compute vm mk from-file``: ignores ``machine.scsi`` vss-cli configuration spec (``shell``).

## [v2023.8.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.8.0) (2023-08-22)

**Improvements:**

- [#635](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/635): ``docs``: publish docs to confluence cloud (VSS Public Documentation).
- [#636](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/636): ``ci``: rename branch master to main.
- [#637](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/637): ``docs``: update public mirror on github.com.
- [#638](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/638): ``core``: upgrade ``Pygments`` from ``2.13.0`` to ``>2.13.0``.
- [#639](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/639): ``docker``:  image move to sphinx-build
- [#640](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/640): ``core``: upgrade ``click`` from ``8.1.3`` to ``8.1.7``.

**Bug Fixes:**

- [#641](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/641): ``docs``: configuration.rst table not well formatted.

## [v2023.6.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.6.1) (2023-06-26)

**Improvements:**

- [#629](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/629): ``compute vm set ubuntu-pro``: attach/detach commands
- [#630](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/630): ``core``: upgrade ``pyvss`` from ``2023.2.1`` to ``2023.6.0``.
- [#631](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/631): ``core``: check motd via ``pyvss``.
- [#632](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/632): ``domain``: update help.

## [v2023.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.6.0) (2023-06-14)

**Improvements:**

- [#624](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/624): ``ci``: update pre-commit ``flake8`` endpoint.
- [#626](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/626): ``ci``: rename Gitlab CI variable ``CI_BUILD_REF_NAME`` -> ``CI_COMMIT_REF_NAME``.

**Bug Fixes:**

- [#625](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/625): ``docs``: search not working. Missing jquery.

## [v2023.3.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.3.1) (2023-03-29)

**Improvements:**

- [#620](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/620): ``compute vm mk from-file``: post process ``hostname`` in custom spec.
- [#621](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/621): ``compute vm mk from-file``: ``--save``/``--no-save`` to file improvements.
- [#623](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/623): ``cd``: Homebrew formula for `v2023.3.1`.

**Bug Fixes:**

- [#617](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/617): ``compute vm mk from-file``:  ignores ``memory`` in configuration spec.
- [#618](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/618): ``core``: shows empty message of the day.
- [#619](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/619): ``compute vm mk from-file``: ignores ``storage-type`` in configuration spec.

## [v2023.3.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.3.0) (2023-03-14)

**Improvements:**

- [#610](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/610): ``compute vm set disk up``: `--confirm` flag to prompt for confirmation.
- [#612](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/612): ``ovf get``: support for ``Strings/ovf:Strings`` reference.
- [#614](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/614): ``raw``: restrict calls only to ``utoronto.ca|edu`` domains

**Bug Fixes:**

- [#611](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/611): ``ovf get``: error when ``@ovf:fileRef`` is missing.
- [#613](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/613): ``compute vm mk from-file``: ``clib`` error when deploying.


## [v2023.2.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.2.1) (2023-02-24)

**Improvements:**

- [#602](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/602): ``compute vm mk from-file``: support ``clone`` and ``template`` build process.
- [#603](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/603): ``compute vm mk from-file``: ``clib`` and ``shell`` standardization.
- [#604](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/604): ``compute vm mk from-file``: default firmware set to ``efi``.
- [#605](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/605): ``compute vm set secure-boot``: enable ``--on`` or disable ``--off`` secure boot.
- [#606](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/606): ``core``: upgrade ``pyvss`` from ``2023.2.0`` to ``2023.2.1``.

**Bug Fixes:**

- [#607](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/607): ``compute vm set storage-type``: missing ``payload_options`` for scheduling.

## [v2023.2.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2023.2.0) (2023-02-16)

**Improvements:**

- [#597](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/597): ``compute vm set vss-preference``: ``--action`` ``add``/``del`` to manage vss preferences.
- [#597](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/597): ``compute vm get vss-preference``: get vss preferences.
- [#599](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/599): ``core``: upgrade ``minio`` from 7.1.12 to 7.1.13.
- [#596](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/596): ``core``: upgrade ``pyvss`` from ``2022.10.0`` to ``2023.2.0``.

**Bug Fixes:**

- [#595](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/595): ``compute vm mk from-file``: ``additional_params`` incorrectly parsed name and file
- [#598](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/598): ``compute vm mk from-file``: ``shell``/``clib`` template bad spec in disks.

## [v2022.12.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.12.0) (2022-12-08)

**Improvements:**

- [#586](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/586): ``core``: upgrade ``minio`` from 7.1.5 to 7.1.12.
- [#587](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/587): ``core``: upgrade ``Pygments`` from 2.11.2 to 2.13.0.
- [#588](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/588): ``core``: upgrade ``pick`` from 2.0.2 to 2.2.0.
- [#589](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/589): ``core``: upgrade ``dateparser`` from 1.1.1 to 1.1.4.
- [#590](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/590): ``core``: ``setup`` and requirements decoupling.
- [#591](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/591): ``core``:  ``gitignore`` and ``dockerignore`` improvements

**Bug Fixes:**

- [#592](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/592): ``compute vm mk shell``:  option ``--custom-spec`` error when using inline value.
- [#592](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/592): ``compute vm mk from-clone``: option ``--custom-spec`` error when using inline value.
- [#592](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/592): ``compute vm mk from-spec``: option ``--custom-spec`` error when using inline value.
- [#592](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/592): ``compute vm mk from-image``: option ``--custom-spec`` error when using inline value.
- [#592](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/592): ``compute vm mk from-clib``: option ``--custom-spec`` error when using inline value.

## [v2022.11.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.11.0) (2022-11-04)

**Improvements:**

- [#570](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/570): ``compute vm mk from-file``: support ``extra-config`` attribute.
- [#579](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/579): ``compute vm mk from-clib``: support ``config-file-name`` and ``idtoken-name`` attributes in ``day-zero`` section.
- [#580](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/580): ``compute vm mk from-file``: support ``config-file-name`` and ``idtoken-name`` attributes in ``day-zero`` section.
- [#581](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/581): ``compute vm mk from-file``: support ``firmware`` attributes in ``machine`` section.
- [#582](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/582): ``cd``: Homebrew formula for the vss-cli.
- [#583](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/583): ``core``: upgrade ``pyjwt`` from ``2.4.0`` to ``2.6.0``.
- [#584](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/584): ``core``: upgrade ``tabulate`` from ``0.8.10`` to ``0.9.0``.

## [v2022.10.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.10.1) (2022-10-22)

**New Features:**

- [#571](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/571):  ``ovf get``: to inspect and generate ``additional-params`` spec file from OVA or OVF.

**Improvements:**

- [#568](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/568): ``compute vm mk shell``:  option ``--custom-spec`` load from ``yaml``/``json`` file or input.
- [#568](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/568): ``compute vm mk from-clone``: option ``--custom-spec`` load from ``yaml``/``json`` file or input.
- [#568](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/568): ``compute vm mk from-spec``: option ``--custom-spec`` load from ``yaml``/``json`` file or input.
- [#568](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/568): ``compute vm mk from-image``: option ``--custom-spec`` load from ``yaml``/``json`` file or input.
- [#568](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/568): ``compute vm mk from-clib``: option ``--custom-spec`` load from ``yaml``/``json`` file or input.
- [#570](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/570): ``️compute vm mk from-file``: support ``extra-config`` attribute in the machine section.
- [#572](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/572): ``compute vm mk shell``:  option ``--vbs`` to enable Virtualization Based Security.
- [#572](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/572): ``compute vm mk from-clone``: option ``--vbs`` to enable Virtualization Based Security.
- [#572](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/572): ``compute vm mk from-spec``: option ``--vbs`` to enable Virtualization Based Security.
- [#572](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/572): ``compute vm mk from-image``: option ``--vbs`` to enable Virtualization Based Security.
- [#572](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/572): ``compute vm mk from-clib``:  option ``--vbs`` to enable Virtualization Based Security.
- [#573](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/573): ``compute vm mk from-file``: support ``vbs`` and ``tpm`` attribute in the machine section.
- [#574](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/574): ``misc b64d-gz``: process from input or file reference.
- [#574](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/574): ``misc gz-b64e``: process from input or file reference.
- [#574](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/574): ``hash-string``: process from input or file reference.
- [#575](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/575): ``docs``: example to deploy Photon OS from clib.
- [#576](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/576): ``docs``: update clib deployment user data.


## [v2022.10.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.10.0) (2022-10-07)

**Improvements:**

- [#563](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/563): ``compute vm set storage-type``: set to either ``ssd`` or ``hdd`` (approval required).
- [#564](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/564): ``compute vm get storage-type``: current virtual machine storage type.
- [#565](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/565): ``core``: upgrade ``pyvss`` from ``2022.9.0`` to ``2022.10.0``.

**Bug Fixes:**

- [#562](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/562): ``docs``: vm export example outdated.
- [#566](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/566): ``compute vm get ``: missing ``committed_gb`` attribute.

## [v2022.9.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.9.0) (2022-09-28)

**Improvements:**

- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk shell``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk from-clone``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk from-spec``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk from-image``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk from-template``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#553](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/553): ``compute vm mk from-clib``: option ``--storage-type`` to set either ``ssd`` or ``hdd``, defaults to ``hdd``.
- [#554](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/554): ``core``: upgrade ``pyvss`` from ``2022.8.1`` to ``2022.9.0``.
- [#555](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/555): ``core``: upgrade ``pick`` from ``1.2.0`` to ``1.4.0``.
- [#556](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/556): ``compute vm get spec``: to include `storage-type`.
- [#557](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/557): ``compute vm mk from-file``: support for ``storage-type``.
- [#558](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/558): ``docs``: updating deployment options.
- [#560](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/560): ``ci``: remove nose since it may be unmaintained.

## [v2022.8.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.8.1) (2022-08-25)

**Bug Fixes:**

- [#547](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/547): ``message``: showing spinner when prompting for TOTP.
- [#548](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/548): ``request``: showing spinner when prompting for TOTP.
- [#549](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/549): ``stor``: showing spinner when prompting for TOTP.
- [#550](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/550): ``service``: showing spinner when prompting for TOTP.

**Improvements:**

- [#546](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/546): ``core``: heck for message of the day.


## [v2022.8.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.8.0) (2022-08-16)

**Improvements:**

- [#538](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/538): ``compute vm set snapshot set mk``: set ``--no-memory`` as  default.
- [#539](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/539): ``core``: upgrade ``pyvss`` from ``2022.6.0`` to ``2022.8.1``.
- [#540](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/540): ``core``: upgrade ``pick`` from ``1.2.0`` to ``1.4.0``.
- [#541](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/541): ``compute vm set vbs on``: enable Virtualization Based Security (``vbs``).
- [#541](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/541): ``compute vm set vbs off``: disable Virtualization Based Security (``vbs``).
- [#542](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/542): ``compute vm get vbs``: get Virtualization Based Security (``vbs``) settings.
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk shell``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk from-clone``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk from-spec``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk from-image``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk from-template``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#543](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/543): ``compute vm mk from-clib``: option ``--tpm`` to add Trusted Platform Module (``tpm``).
- [#544](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/544): ``compute vm set floppy mk``: create floppy devices.
- [#544](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/544): ``compute vm set floppy up``: update floppy devices.
- [#544](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/544): ``compute vm set floppy rm``: remove floppy devices.

## [v2022.7.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.7.0) (2022-07-26)

**Improvements:**

- [#536](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/536): ``docs``: update vmx hardware version compatibility to ``vmx-19``.
 
**Bug Fixes:**

- [#535](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/535): ``stor ul``: error when uploading a file without ``--name``.


## [v2022.6.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.6.1) (2022-06-23)

**Improvements:**

- [#532](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/532): ``core``: upgrade ``tabulate`` from ``0.8.9`` to ``0.8.10``.
- [#533](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/533): ``core``: upgrade ``validators`` from ``0.18.2`` to ``0.20.0``.

**Bug Fixes:**

- [#530](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/530): ``compute vm mk from-clib``: ``--additional-params`` error even if not provided.
- [#531](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/531): ``compute vm mk from-file``: ignores ``admin`` in vss-cli configuration spec.

## [v2022.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.6.0) (2022-06-15)

**Improvements:**

- [#523](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/523): ``compute vm set tpm mk``: create ``vTPM`` device.
- [#523](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/523): ``compute vm set tpm rm``: delete ``vTPM`` device.
- [#524](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/524): ``compute vm get tpm``: get ``vTPM`` device.
- [#525](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/525): ``compute vm mk from-clib``: support ``--day-zero`` config and ``--id-token`` for Day0 configuration.
- [#526](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/526): ``️compute vm mk from-file``: support ``day-zero`` configuration via ``config`` and ``id-token`` in ``vss-cli spec``.
- [#527](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/527): ``core``: upgrade ``pyvss`` from ``2022.5.0`` to ``2022.6.0``.
- [#528](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/528): ``core``: upgrade ``pyjwt`` from ``2.3.0`` to ``2.4.0``.

## [v2022.5.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.5.0) (2022-05-30)

**Improvements:**

- [#520](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/520): ``core``: upgrade ``pyvss`` from ``2022.4.0`` to ``2022.5.0``.
- [#518](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/518): ``compute vm mk from-clib``: support ``--additional-params`` in ``yaml`` or ``json`` format for OVA/OVF ``PropertyParams`` and ``DeploymentOptionParams``.
- [#521](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/521): ``️compute vm mk from-file``: support ``clib`` deployments.

**Bug Fixes:**

- [#519](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/519): ``compute vm get console``: throws ``AttributeError``.

## [v2022.4.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.4.0) (2022-04-29)

**Improvements:**

- [#510](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/510): ``core``: upgrade ``pyvss`` from ``2022.3.1`` to ``2022.4.0``.
- [#511](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/511): ``core``: upgrade ``click`` from ``8.0`` to ``8.1.3``.
- [#512](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/512): ``ci``: upgrade ``pre-commit`` hook ``black`` version to ``22.3.0``.
- [#513](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/513): ``ci``: upgrade ``pre-commit`` hook ``flake8`` version to ``3.7.9``.

**Bug Fixes:**

- [#514](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/514): ``core``: autocompletion errors during option and argument completion.
- [#515](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/515): ``compute vm mk from-clone``: option ``--snapshot`` auto-completion throws exception.
- [#516](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/516): ``request retirement get``: auto-completion throws exception.


## [v2022.3.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.3.1) (2022-03-24)

**Improvements:**

- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor dl``: download object from your VSS personal store (s3 implementation).
- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor get``: get objects info stored in your VSS personal store (s3 implementation).
- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor la``: launch web interface to your VSS personal store (s3 implementation).
- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor ls``: list objects in VSS personal store (s3 implementation).
- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor sh``: generate a pre-signed link to share object stored in your VSS personal store (s3 implementation).
- [#504](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/504): ``stor ul``: upload object to your VSS personal store (s3 implementation).
- [#505](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/505): ``core``: upgrade ``pyvss`` from ``2022.3.0`` to ``2022.3.1``.
- [#506](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/506): ``core``: upgrade ``dataclasses-json`` from ``0.5.6`` to ``0.5.7``.
- [#508](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/508): ``docker``: remove from image ``libxml2-dev`` ``libxslt-dev`` and ``libffi-dev`` dependencies.
- [#509](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/509): ``docs``: update vskey-stor related configuration settings.

## [v2022.3.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.3.0) (2022-03-21)

**Improvements:**

- [#497](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/497): ``core``: update ``click`` from ``8.0.3`` to ``8.0.4``.
- [#498](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/498): ``core``: update ``click-log`` from ``0.3.2`` to ``0.4.0``.
- [#499](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/499): ``core``: update ``dateparser`` from ``1.1.0`` to ``1.1.1``.
- [#500](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/500): ``compute vm set disk up``: option ``--notes`` to set notes to disk.
- [#501](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/501): ``core``: upgrade ``pyvss`` from ``2022.2.0`` to ``2022.3.0``. 
- [#502](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/502): ``compute vm get disk``: include notes.

## [v2022.2.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2022.2.0) (2022-02-14)

**Improvements:**

- [#491](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/491): ``compute vm mk from-clib``: add yaml validation to ``--network-config`` and ``--user-data``.
- [#491](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/491): ``compute vm mk from-template``: add yaml validation to ``--network-config`` and ``--user-data``.
- [#492](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/492): ``compute vm rm``: add ``--prune`` option to completely remove instance.
- [#493](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/493): ``core``: upgrade ``pyvss`` from ``2021.12.0`` to ``2022.2.0``.
- [#494](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/494): ``core``: update ``ruamel.yaml`` from ``0.17.17`` to ``0.17.21``.
- [#495](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/495): ``core``: update ``Pygments`` from ``2.10.0`` to ``2.11.2``.
 
## [v2021.12.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.12.0) (2021-12-20)

**Improvements:**

- [#486](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/486): ``core``: minimum ``python`` version to `3.7`.
- [#487](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/487): ``core``: upgrade ``pick`` from ``1.0.0`` to ``1.2.0``..
- [#488](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/488): ``core``: upgrade ``pyvss`` from ``2021.11.2`` to ``2021.12.0``.
- [#489](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/489): ``compute vm set snapshot mk``: new option ``--memory/--no-memory`` to include or exclude memory.
 
## [v2021.11.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.11.2) (2021-11-29)

**Improvements:**

- [#479](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/479): ``core``: update ``pyvss`` from ``v2021.11.1`` to ``v2021.11.2``.
- [#484](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/484): ``core``: update ``ruamel.yaml`` to ``0.17.17``.

**Bug Fixes:**

- [#481](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/481): ``configure mk``: empty token in configuration file when creating new endpoint.
- [#483](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/483): ``core``: exception when api is unavailable.

## [v2021.11.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.11.1) (2021-11-08)

**Improvements:**

- [#476](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/476): ``account set mfa mk``: improve QR code compatibility.
- [#478](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/478): ``account set mfa rm``: prompt for token.
- [#479](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/479): ``core``: update ``pyvss`` from ``v2021.11.0`` to ``v2021.11.1``.

**Bug Fixes:**

- [#477](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/477): ``account set mfa mk``: ``recovery_codes.txt`` naming issue.

## [v2021.11.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.11.0) (2021-11-01)

**Improvements:**

- [#463](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/463): ``account set mfa mk``: enable mfa with totp.
- [#463](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/463): ``account set mfa rm``: disable mfa.
- [#463](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/463): ``account set mfa verify``: verify mfa totp setup.
- [#463](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/463): ``account set mfa get-token``: get totp.
- [#464](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/464): ``core``: update ``pyvss`` from ``v2021.8.0`` to ``v2021.11.0``.
- [#465](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/465): ``core``: support two-factor authentication.
- [#466](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/466): ``configure``: support two-factor authentication.
- [#467](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/467): ``account get mfa``: get account mfa status.
- [#468](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/468): ``core``: update ``click`` from ``8.0.1`` to ``8.0.3``.
- [#469](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/469): ``core``: update ``dateparser`` from ``1.0.0`` to ``1.1.0``.
- [#470](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/470): ``docker``: remove custom requirement branch for ``click-repl``.
- [#471](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/471): ``ci``: rollback #458 and use local images.
- [#472](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/472): ``core``: ``setup.py`` update ``stor``, ``dev`` and min ``python`` version to ``3.8``.
- [#473](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/473): ``docs``: remove ``microbadger`` backed images.

**Bug Fixes:**

- [#474](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/474): ``ci``: add missing ``rust`` dependency.

## [v2021.9.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.9.0) (2021-09-15)

**Improvements:**

- [#458](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/458): ``ci``: standardize Pipeline settings to ensure portability to GL SaaS.
- [#459](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/459): ``core``: update ``Pygments`` to ``2.10.0``.
- [#460](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/460): ``core``: update ``dataclasses-json`` to ``0.5.6``.
- [#461](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/461): ``core``: update ``ruamel.yaml`` to ``0.17.16``.

## [v2021.8.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.8.0) (2021-08-18)

**Improvements:**

- [#453](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/453): ``compute vm mk shell``: option ``--template`` to mark vm as template.
- [#453](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/453): ``compute vm mk from-clone``: option ``--template`` to mark vm as template.
- [#453](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/453): ``compute vm mk from-spec``: option ``--template`` to mark vm as template.
- [#453](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/453): ``compute vm mk from-image``: option ``--template`` to mark vm as template.
- [#453](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/453): ``compute vm mk from-template``: option ``--template`` to mark vm as template.
- [#454](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/454): ``compute vm mk shell``: option ``--cores-per-socket`` to set advanced cpu config.
- [#454](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/454): ``compute vm mk from-clone``: option ``--cores-per-socket`` to set advanced cpu config.
- [#454](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/454): ``compute vm mk from-spec``: option ``--cores-per-socket`` to set advanced cpu config.
- [#454](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/454): ``compute vm mk from-image``: option ``--cores-per-socket`` to set advanced cpu config.
- [#454](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/454): ``compute vm mk from-template``: option ``--cores-per-socket`` to set advanced cpu config.
- [#455](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/455): ``compute vm set cpu count`` : option ``--cores-per-socket`` for advanced settings.
- [#456](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/456): ``core``: update ``pyvss`` from ``v2021.6.0`` to ``v2021.8.0``.

**Bug Fixes:**

- [#452](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/452): ``compute vm set controller scsi rm``: Missing verb in removal confirmation.


## [v2021.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.6.0) (2021-06-14)

**Improvements:**

- [#447](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/447): ``compute vm mk shell``: deprecate ``--high-io`` **breaking**.
- [#447](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/447): ``compute vm mk from-clone``: deprecate ``--high-io`` **breaking**.
- [#447](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/447): ``compute vm mk from-spec``: deprecate ``--high-io`` **breaking**.
- [#447](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/447): ``compute vm mk from-image``: deprecate ``--high-io`` **breaking**.
- [#447](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/447): ``compute vm mk from-template``: deprecate ``--high-io`` **breaking**.
- [#448](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/448): ``compute vm mk shell``: option ``--scsi`` to define controllers with payload: ``{"type": "paravirtual", "bus": 0}``.
- [#448](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/448): ``compute vm mk from-clone``: option ``--scsi`` to define controllers with payload: ``{"type": "paravirtual", "bus": 0}``.
- [#448](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/448): ``compute vm mk from-spec``: option ``--scsi`` to define controllers with payload: ``{"type": "paravirtual", "bus": 0}``.
- [#448](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/448): ``compute vm mk from-image``: option ``--scsi`` to define controllers with payload: ``{"type": "paravirtual", "bus": 0}``.
- [#448](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/448): ``compute vm mk from-template``: option ``--scsi`` to define controllers with payload: ``{"type": "paravirtual", "bus": 0}``.
- [#449](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/449): ``core``: update ``pyvss`` from v2021.5.0 to v2021.6.0.

**Bug Fixes:**

- [#450](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/450): ``compute vm mk shell``: ``"scsi": 0`` ignored when provided in ``--disk`` option.
- [#450](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/450): ``compute vm mk from-clone``: ``"scsi": 0`` ignored when provided in ``--disk`` option.
- [#450](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/450): ``compute vm mk from-spec``: ``"scsi": 0`` ignored when provided in ``--disk`` option.
- [#450](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/450): ``compute vm mk from-image``: ``"scsi": 0`` ignored when provided in ``--disk`` option.
- [#450](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/450): ``compute vm mk from-template``: ``"scsi": 0`` ignored when provided in ``--disk`` option.


## [v2021.5.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.5.4) (2021-05-31)

**Improvements:**

- [#444](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/444): ``core``: update ``click-repl`` from v0.1.6 to v0.2.0.
- [#445](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/445): ``core``: update ``click-threading`` from v0.4.4 to v0.5.0.

## [v2021.5.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.5.3) (2021-05-26)

**Improvements:**

- [#439](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/439): ``core``: update ``click`` from v8.0.0 to v8.0.1.
- [#440](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/440): ``compute vm set controller scsi rm``: update to implement ``pyvss.manager.get_vm_scsi_device``. 
- [#442](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/442): ``core``: remove ``prompt-toolkit`` from dependencies.
- [#443](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/443): ``docs``: Update ``VSS Shell`` section in ``README.md`` and ``use.rst``. 

## [v2021.5.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.5.2) (2021-05-18)

**Improvements:**

- [#427](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/427): ``core``: update ``click`` from v7.1.1 to v8.0.0.
- [#428](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/428): ``completion``: update to support click 8 changes.
- [#429](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/429): ``shell``: formatting improvements.
- [#430](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/430): ``core``: update ``click-repl`` to custom repo/branch to support completion in click 8.
- [#431](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/431): ``core``: update ``dataclases-json`` from v0.5.2 to v0.5.3.
- [#432](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/432): ``core``: update ``Pygments`` from  v2.8.0 to v2.9.0
- [#433](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/433): ``core``: update ``ruamel.yaml`` from v0.16.13 to v0.17.4.
- [#434](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/434): ``docs``: update README with the latest info.
- [#436](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/436): ``docker``: Add ``git`` to base image.  

## [v2021.5.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v2021.5.1) (2021-05-05)

**New Features:**

- [#418](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/418): ``compute vm set retire mk``: manage retirement requests for vms.
- [#418](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/418): ``compute vm set retire confirm``: manage retirement requests for vms.
- [#418](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/418): ``compute vm set retire cancel``: manage retirement requests for vms.
- [#418](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/418): ``compute vm set retire send``: manage retirement requests for vms.
- [#419](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/419): ``compute vm get retire``: get retirement requests for vm.
- [#420](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/420): ``request retire ls``: list retirement requests.
- [#420](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/420): ``request retire get``: get retirement request info.
- [#420](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/420): ``request retire confirm``: confirm retirement request.
- [#420](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/420): ``request retire cancel``: cancel retirement request.
- [#420](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/420): ``request retire send``: send notification for a retirement request.

**Improvements:**

- [#417](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/417): ``core``: move from ``semver`` to ``calver``.
- [#423](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/423): ``compute vm set custom-spec``: allow multiple ``--dns-suffix`` options for dns search settings.
- [#424](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/424): ``compute vm mk shell``: create VM with retirement request ``--retire-type``, ``--retire-value``, ``--retire-warning``.
- [#424](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/424): ``compute vm mk from-clone``: create VM with retirement request ``--retire-type``, ``--retire-value``, ``--retire-warning``.
- [#424](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/424): ``compute vm mk from-spec``: create VM with retirement request ``--retire-type``, ``--retire-value``, ``--retire-warning``.
- [#424](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/424): ``compute vm mk from-image``: create VM with retirement request ``--retire-type``, ``--retire-value``, ``--retire-warning``.
- [#424](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/424): ``compute vm mk from-template``: create VM with retirement request ``--retire-type``, ``--retire-value``, ``--retire-warning``.
- [#426](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/426): ``core``: update ``pyvss`` from v0.18.1 to v2021.5.0.

**Bug Fixes:**

- [#421](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/421): ``request new retry``: ignores ``--wait`` option.
- [#422](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/422): ``request change retry``: ignores ``--wait`` option.

## [v0.12.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.12.1) (2021-04-15)

**Improvements:**

- [#409](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/409): ``account get groups``:  update default columns to recent api changes.
- [#410](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/410): ``account get group``: update default columns to recent api changes.
- [#411](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/411): ``request change get``: update default columns to recent api changes.
- [#412](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/412): ``request new get``: update default columns to recent api changes.
- [#413](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/413): ``request snapshot get``: update default columns to recent api changes.
- [#416](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/416): ``docker``: base image ``hub.eis.utoronto.ca/vss/docker/python:3.9-alpine``.
  
**Bug Fixes:**

- [#414](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/414): ``request vmdk``: missing command.

## [v0.12.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.12.0) (2021-04-09)

**New Features:**

- [#403](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/403): ``compute contentlib``: content library integration.
- [#405](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/405): ``copmute vm mk from-clib``: deploy vms from content library.

**Improvements:**

- [#402](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/402): ``core``: Add ``--webdav-server`` option to configuration file.
- [#406](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/406): ``compute vm mk from-clone``: ``--snapshot`` to clone from given snapshot
- [#404](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/404): ``core``: update ``pyvss`` from v0.17.2 to v0.18.1.

**Bug Fixes:**

- [#401](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/401): ``compute vm mk from-image``: throws exception when user-data is not provided even if it's optional. 
- [#407](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/407): ``core`` : ``--filter-by`` option ignored if operator is included.

## [v0.11.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.11.0) (2021-03-05)

**New Features:**

- [#390](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/390): ``compute vm get cr``:to get change requests by virtual machine.
- [#396](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/396): ``compute vm get cr``: Add support for ``--output ndjson``.

**Improvements:**

- [#389](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/389): ``compute vm set inform``: take single comma-separated emails or multiple emails.
- [#395](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/395): ``core``: minimum ``python`` version 3.7.0.
- [#391](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/391): ``core``: update ``pyvss`` from v0.17.1 to v0.17.2.
- [#392](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/392): ``core``: update ``tabulate`` from v0.8.7 to v0.8.9.
- [#393](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/393): ``core``: update ``dateparser`` from v0.7.6 to v1.0.0
- [#397](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/397): ``core``: update ``validators`` from v0.18.1 to v0.18.2.
- [#398](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/398): ``core``: update ``Pygments`` from v2.7.1 to v2.8.0.
- [#399](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/399): ``core``: update ``ruamel.yaml`` from v0.16.12 to v0.16.13.
- [#394](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/394): ``ci``: pipeline release-dist jobs missing dependencies: ``rust`` and ``cargo``.

## [v0.10.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.10.4) (2021-02-04)

**Improvements:**

- [#387](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/387): ``compute vm set disk mk``: support ``scsi`` in ``JSON`` format.

## [v0.10.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.10.3) (2021-01-22)

**Improvements:**

- [#385](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/385): ``compute vm mk from-image``: ``--network-config`` improvements to handle cloud config ``network-config`` file.


## [v0.10.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.10.2) (2021-01-07)

**Improvements:**

- [#383](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/383): ``compute vm mk from-image``: ``--user-data`` improvements to handle cloud config user data file.
- [#382](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/382): ``ci``: python package deployment on internal registry. 

## [v0.10.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.10.1) (2020-12-09)

**Improvements:**

- [#379](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/379): ``core``: direct status messages and user-interaction prompts to ``stderr`` instead of ``stdout``.
- [#380](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/380): ``core``: migrate from ``jsonpath-rw`` to ``jsonpath-ng``.

**Bug Fixes:**
 
- [#378](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/378):  ``compute vm mk from-file``: throws ``VssError`` exception.
 
## [v0.10.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.10.0) (2020-11-18)

**New Features:**

- [#371](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/371): ``compute vmdk``: command to mange user ``vmdk`` files.
- [#371](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/371): ``compute vmdk ls``: command to list user ``vmdk`` files.
- [#371](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/371): ``compute vmdk sync``: command to sync user ``vmdk``files from ``vskey-stor``.
- [#375](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/375): ``compute vm set firmware``: update vm firmware configuration.
- [#376](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/376): ``compute vm get firmware``: get vm firmware configuration.

**Improvements:**

- [#366](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/366): ``compute vm set extra-cfg``: update command to new payload.
- [#367](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/367): ``compute vm mk shell``: create VM with ``--extra-config`` takes multiple ``key=value``.
- [#367](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/367): ``compute vm mk from-clone``: create VM with ``--extra-config`` takes multiple ``key=value``.
- [#367](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/367): ``compute vm mk from-spec``: create VM with ``--extra-config`` takes multiple ``key=value``.
- [#367](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/367): ``compute vm mk from-image``: create VM with ``--extra-config`` takes multiple ``key=value``.
- [#367](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/367): ``compute vm mk from-template``: create VM with ``--extra-config`` takes multiple ``key=value``.
- [#368](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/368): ``core``: ``pyvss`` v0.16.0 -> v0.17.0.
- [#369](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/369): ``docker``: base image upgrade to ``hub.eis.utoronto.ca/vss/docker/python:3.8-alpine``.
- [#370](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/370): ``ci``: base docker services to use local repository.
- [#372](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/372): ``compute vm set disk mk``: support ``backing_vmdk`` in ``<capacity>=<backing_mode>=<backing_sharing>=<backing_vmdk>`` or ``JSON`` format.
- [#373](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/373): ``core``: ``pyvss`` v0.17.0 -> v0.17.1.
- [#374](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/374): ``compute vm mk shell``: create VM with ``--firmware/-w``.
- [#374](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/374): ``compute vm mk from-clone``: create VM with ``--firmware/-w``.
- [#374](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/374): ``compute vm mk from-spec``: create VM with ``--firmware/-w``.
- [#374](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/374): ``compute vm mk from-image``: create VM with ``--firmware/-w``.
- [#374](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/374): ``compute vm mk from-template``: create VM with ``--firmware/-w``.


## [v0.9.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.9.0) (2020-10-29)

**Improvements:**

- [#358](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/358): ``core``: ``pyvss`` v0.15.1 -> v0.16.0.
- [#359](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/359): ``compute vm set controller scsi up --sharing``: updates SCSI sharing mode.
- [#360](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/360): ``compute vm set disk up --sharing``: updates Disk sharing mod``<capacity>=<backing_mode>=<backing_sharing>``.e.
- [#361](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/361): ``compute vm set controller scsi mk --scsi``: create SCSI controller with new spec ``<type>=<sharing>``. 
- [#362](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/362): ``compute vm set disk mk --disk``: create Disk with new spec 
- [#363](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/363): ``compute vm mk shell``: create VM with Disks using new spec `` <capacity>=<backing_mode>=<backing_sharing>``. 
- [#363](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/363): ``compute vm mk from-clone``: create VM with Disks using new spec `` <capacity>=<backing_mode>=<backing_sharing>``.
- [#363](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/363): ``compute vm mk from-file``: create VM with Disks using new spec `` <capacity>=<backing_mode>=<backing_sharing>``.
- [#363](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/363): ``compute vm mk from-image``: create VM with Disks using new spec `` <capacity>=<backing_mode>=<backing_sharing>``.
- [#363](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/363): ``compute vm mk from-template``: create VM with Disks using new spec `` <capacity>=<backing_mode>=<backing_sharing>``.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``--wait/--no-wait``: add option to the main cli instead of per sub-command that submits requests. Also available with ``VSS_WAIT_FOR_REQUESTS``.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``config set``: add ``wait_for_requests`` option in general settings in configuration file. 
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute vm set``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute vm mk``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute vm rm``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute template rm``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute folder set``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute folder mk``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute folder rm``: remove ``--wait/--no-wait`` option.
- [#364](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/364): ``compute inventory mk``: remove ``--wait/--no-wait`` option.


## [v0.8.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.8.4) (2020-09-25)

**Improvements:**

- [#349](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/349): ``compute template rm``: command to allow decommissioning vm templates.
- [#350](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/350): ``core``: ``pyvss`` v0.15.0 -> v0.15.1.
- [#351](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/351): ``core``: ``pick`` v0.6.7 -> v1.0.0.
- [#352](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/352): ``core``: ``ruamel.yaml`` v0.16.10 -> v0.16.12.
- [#353](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/353): ``core``: ``dataclasses-json`` v0.2.2 -> v0.5.2.
- [#354](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/354): ``core``: ``validators`` v0.14.3 -> v0.18.1.
- [#355](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/355): ``core``: ``dateparser`` v0.7.4 -> 0.7.6.
- [#356](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/356): ``core``: ``Pygments`` v2.6.1 -> v2.7.1.


## [v0.8.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.8.3) (2020-08-17)

**Improvements:**

- [#347](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/347): ``compute vm set``: ``--no-wait`` option to override ``--wait``.

**Bug Fixes:**

- [#345](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/345): ``compute vm set``: output format always is ``json``.
- [#346](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/346): ``compute vm set``: ``--wait`` is always on.


## [v0.8.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.8.2) (2020-08-05)

**Improvements:**

- [#343](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/343): ``core``: ``pyvss``  v0.14.4 -> v0.15.0.
- [#342](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/342): ``core``: Add python ``3.8``.
- [#340](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/340): ``key``: docstring improvements.
- [#339](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/339): ``plugin``: docstring improvements.
- [#338](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/338): ``key``: docstring improvements.
- [#337](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/337): ``completion``: docstring improvements.
- [#336](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/336): ``account``: docstring improvements.
- [#335](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/335): ``request snapshot``: docstring improvements.
- [#334](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/334): ``request new``: docstring improvements.
- [#333](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/333): ``request inventory``: docstring improvements.
- [#332](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/332): ``request image``: docstring improvements.
- [#331](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/331): ``request folder``: docstring improvements.
- [#330](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/330): ``request export``: docstring improvements.
- [#329](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/329): ``request change``: docstring improvements.
- [#328](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/328): ``request template``: docstring improvements.
- [#327](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/327): ``compute os``: docstring improvements.
- [#326](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/326): ``compute net``: docstring improvements.
- [#325](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/325): ``compute iso``: docstring improvements.
- [#324](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/324): ``compute inventory``: docstring improvements.
- [#323](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/323): ``compute image``: docstring improvements.
- [#322](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/322): ``compute folder``: docstring improvements.
- [#321](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/321): ``compute floppy``: docstring improvements.
- [#320](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/320): ``compute domain``: docstring improvements.
- [#319](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/319): ``compute vm``: docstring improvements.
- [#318](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/318): ``core``: ``config`` general improvements.
- [#317](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/317): ``core``: ``helper`` general improvements.
- [#316](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/316): ``docs``: ``asciicast`` general improvements.
- [#214](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/214): ``compute vm set``: ``--dry-run`` option to simulate execution before submitting command.

**Bug Fixes:**

- [#341](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/341): ``upgrade``:  bandit warning HIGH. 

## [v0.8.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.8.1) (2020-06-22)

**Improvements:**

- [#314](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/314): ``tests``: Adding/Updating pre-commit hooks.

**Bug Fixes:**

- [#312](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/312): ``compute vm mk from-file``: throws TypeError exception.
- [#313](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/313): ``docs``: deploy-image outdated command options. 


## [v0.8.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.8.0) (2020-06-04)

**Improvements:**

- [#304](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/304): ``core``: ``pyvss``  v0.14.2 -> v0.14.4.
- [#306](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/306): ``️account get groups``: update to recent api changes: **breaking**.
- [#307](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/307): ``account get group``: update to recent api changes (``group_name_desc_or_id`` is now required): **breaking**.
- [#308](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/308): ``account get group member``: new sub-command.
- [#309](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/309): ``docker``: base image upgrade to ``python:3.8-alpine``.

**Bug Fixes:**

- [#302](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/302): ``compute vm set guest-cmd``: ``--env`` option is sent emtpy.
- [#303](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/303): ``compute vm get memory``: throws exception.
- [#305](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/305): ``core``: PEP8 check F541: f-string without any placeholders.
- [#310](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/310): ``docker``: image build broken due to dependency name change from man to man-pages.


## [v0.7.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.7.1) (2020-05-07)

**Improvements:**

- [#296](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/296): ``compute vm set guest-os``: renamed to ``os`` missing command.
- [#298](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/298): ``core``: ``click`` v7.1.1 -> v7.1.2.
- [#299](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/299): ``core``: ``pyvss``  v0.14.1 -> v0.14.2.
- [#300](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/300): ``core``: ``pygments`` v2.4.2 -> v2.6.1.

**Bug Fixes:**

- [#295](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/295): ``compute vm get os``: os missing command.
- [#297](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/297): ``compute vm rm``: does not allow deletion.


## [v0.7.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.7.0) (2020-04-24)

**Improvements:**

- [#278](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/278): ``compute vm ls``: add ``vm_moref`` to default attributes. 
- [#279](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/279): ``compute vm get``: add support to query by ``moref``.
- [#280](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/280): ``compute vm set``: add support to update vm by ``moref``.
- [#281](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/281): ``compute vm set ha-group mk``: update to ``moref`` or ``name``: __breaking__
- [#282](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/282): ``compute vm get ha-group``: update  vm identifier ``moref``: __breaking__
- [#283](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/283): ``compute vm get``: include vm identifier ``moref``.
- [#284](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/284): ``compute vm rm``: allow delete vm by ``name``, ``moref`` or ``uuid``.
- [#285](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/285): ``core``: ``pyvss`` upgrade from 0.13.1-> 0.14.0: __breaking__
- [#286](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/286): ``compute vm get vsphere-link``: provide vSphere client link to vm.
- [#287](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/287): ``request new ls``: provide ``vm_moref``.
- [#287](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/287): ``request change ls``: provide ``vm_moref``.
- [#287](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/287): ``request snapshot ls``: provide ``vm_moref``.
- [#287](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/287): ``request export ls``: provide ``vm_moref``.
- [#288](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/288): ``completion``: support ``vm_moref`` and ``moref`` attributes.
- [#291](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/291): ``core``: ``click-spinner`` v0.1.8 -> v0.1.10.
- [#293](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/293): ``docs``: replace ``uuid`` with ``moref``.
- [#294](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/294): ``compute vm set ha-group mg``: to migrate existing ha-group from ``uuid`` to ``moref``.

**Bug Fixes:**

- [#289](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/289): ``request new get``: autocomplete missing.
- [#290](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/290): ``request snapshot get``: autocomplete missing. 


## [v0.6.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.6.2) (2020-04-09)

**Improvements:**

- [#265](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/265): ``docs``: vmware paravirtual scsi migration how-to (windows).
- [#266](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/266): ``compute vm set snapshot mk``: ``--consolidate`` default to true.
- [#267](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/267): ``core``: ``pyvss`` upgrade from 0.13.0-> 0.13.1.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk from-clone``: ``--power-on`` option to power on vm after deployment.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk from-file``: ``--power-on`` option to power on vm after deployment.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk from-image``: ``--power-on`` option to power on vm after deployment.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk from-spec``: ``--power-on`` option to power on vm after deployment.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk from-template``: ``--power-on`` option to power on vm after deployment.
- [#268](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/268): ``compute vm mk shell``: ``--power-on`` option to power on vm after deployment.
- [#269](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/269): ``core``: ``click`` upgrade from  7.0.0 -> 7.1.1.
- [#270](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/270): ``completion``: support for ``fish``.
- [#271](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/271): ``core``: ``pick`` 0.6.6 -> 0.6.7.
- [#272](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/272): ``core``: ``validators`` 0.14.2 -> 0.14.3.
- [#273](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/273): ``core``: ``tabulate`` 0.8.6 -> 0.8.7.
- [#274](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/274): ``core``: ``--table-format`` support for ``pretty``.
- [#275](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/275): ``core``: ``dateparser`` 0.7.2 -> 0.7.4.
- [#276](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/276): ``core``: ``ruaml.yaml`` 0.16.5 -> 0.16.10.

## [v0.6.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.6.1) (2020-03-25)

**Bug Fixes:**

- [#263](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/263): ``compute vm set domain``: domain does not autocomplete based on name attribute.

## [v0.6.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.6.0) (2020-02-28)

**Improvements:**

- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute vm ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute floppy ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute domain ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute folder ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute image personal ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute image public ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute iso personal ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute iso public ls``: support multiple ``--sort`` options. 
- [#246](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``compute net ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request change ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request export ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request folder ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request image ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request inventory ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request new ls``: support multiple ``--sort`` options. 
- [#247](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/246): ``request snapshot ls``: support multiple ``--sort`` options. 
- [#248](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/248): ``service ls``: support multiple ``--sort`` options. 
- [#249](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/249): ``token ls``: support multiple ``--sort`` options. 
- [#250](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/250): ``key ls``: support multiple ``--sort`` options. 
- [#255](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/255): ``ls``: implementation improvement ``--filter-by``.
- [#257](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/257): ``upgrade``: command improvements to find current python executable.
- [#258](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/258): ``ci``: deploy pre-releases to **PYPI** instead of Test instance of PYPI.
- [#259](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/259): ``upgrade develop``: install available pre-release from PYPI.
- [#260](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/260): ``status``: provide summary of both API and VSS service status.
- [#262](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/262): ``ci``: except deploy to pypi when branch develop and commit msg is `Version release`.

**Bug Fixes:**

- [#251](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/251): ``service ls``: exception thrown.
- [#252](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/252): ``token ls``: exception thrown.
- [#253](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/253): ``key ls``: exception thrown.
- [#254](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/254): ``request ls``: exception thrown.
- [#256](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/256): ``core``: when messages found, warning provides invalid command.


## [v0.5.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.5.2) (2020-02-19)

**Bug Fixes:**

- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute vm ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute floppy ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute domain ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute folder ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute image personal ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute image public ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute iso personal ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute iso public ls``: ``--filter-by`` affected by [pallets/click#472].
- [#244](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/244): ``compute net ls``: ``--filter-by`` affected by [pallets/click#472].


## [v0.5.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.5.1) (2020-02-14)

**Bug Fixes:**

- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute vm ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute floppy ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute domain ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute folder ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute image personal ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute image public ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute iso personal ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute iso public ls``: ``--filter-by`` does not support multiple instances.
- [#240](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/240): ``compute net ls``: ``--filter-by`` does not support multiple instances.
- [#241](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/241): ``upgrade``: upgrade command to prioritize to ``python3 -m pip``.
- [#242](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/242): ``upgrade``:  error when ``git`` is not installed.


## [v0.5.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.5.0) (2020-02-06)

**Improvements:**

- [#231](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/231): ``compute vm set state``: add option ``suspend``.
- [#233](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/233): ``compute vm set state``: confirm only if state is not ``poweredOff``.
- [#234](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/234): ``core``: pyvss upgrade from 0.12.1 -> 0.13.0.
- [#235](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/235): ``compute vm set vss-option``: allow autocompletion.
- [#236](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/236): ``--version``: flag to provide python implementation and version.
- [#237](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/237): ``ci``: set ``expire_in`` to 1week for artifacts.
- [#238](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/238): ``core``: implement wheels packaging.

**Bug Fixes:**

- [#230](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/230): ``compute vm set version``: out of date.
- [#232](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/232): ``compute vm set state``: shutdown invalid tools running validation.


## [v0.4.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.4.1) (2020-01-30)

**Improvements:**

- [#223](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/223): ``core``: pick upgrade from 0.6.4 -> 0.6.6
- [#224](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/224): ``core``: validators upgrade from 0.12.4 -> 0.14.2
- [#225](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/225): ``core``: dateparser upgrade from 0.7.0 -> 0.7.2
- [#226](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/226): ``core``: tabulate upgrade from 0.8.3 -> 0.8.6
- [#229](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/229): ``core``: pyvss upgrade from 0.12.0 -> 0.12.1

**Bug Fixes:**

- [#222](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/222): ``compute inventory dl --launch``: fails with exception.
- [#228](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/228): ``compute vm set controller scsi up --scsi-type paravirtual`` fails with ``KeyError`` exception.

## [v0.4.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.4.0) (2020-01-24)

**Improvements:**

- [#217](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/217): ``core``: pyvss upgrade from 0.11.0 -> 0.12.0
- [#218](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/218): ``compute vm set snapshot mk``: add ``--consolidate`` option
- [#219](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/219): ``compute vm set ha-group mk``: create ``ha-group``
- [#219](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/219): ``compute vm set ha-group rm``: remove current member from ``ha-group``    

**Bug Fixes:**

- [#215](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/215): ``docs``: ``bill-dept`` option was found in docs. Replaced with ``client``
- [#216](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/216): ``compute vm set guest-cmd``: always fails.
- [#220](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/220): ``ci``: release dist step fails due to missing os requirement

## [v0.3.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.3.0) (2019-11-14)

**Improvements:**

- [#211](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/211): ``core``: pyvss upgrade from 0.9.43 -> 0.11.0
- [#210](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210): ``compute vm mk from-clone``: rename ``--bill-dept`` to ``--client``: __breaking__
- [#210](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210): ``compute vm mk from-file``: rename ``--bill-dept`` to ``--client``: __breaking__
- [#210](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210): ``compute vm mk from-image``: rename``--bill-dept`` to ``--client``: __breaking__
- [#210](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210): ``compute vm mk from-spec``: rename ``--bill-dept`` to ``--client``: __breaking__
- [#210](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210): ``compute vm mk shell``: rename ``--bill-dept`` to ``--client``: __breaking__
- [#212](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/212): ``compute vm rm from-template``: support for ``--wait`` flag
- [#208](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/208): ``compute folder mk``: support for multiple values and ``--wait`` flag
- [#207](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/207): ``compute folder rm``: support for multiple values and ``--wait`` flag

**Bug Fixes:**

- [#205](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/205): ``docs``: missing changelog entry for v0.2.7
- [#209](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/209): ``docs``: rst syntax warnings
- [#206](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/206): ``compute folder rm``: fails with AttributeError

## [v0.2.7](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.7) (2019-11-08)

**Improvements:**

- [#199](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/199): ``core``: pyvss upgrade from 0.9.43 -> 0.10.0
- [#200](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/200): ``ci``: new items to gitignore
- [#201](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/201): ``compute vm get state``: add ``create_date`` attribute
- [#202](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202): ``request snapshot ls``: default sort by created date
- [#202](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202): ``request new ls``: default sort by created date
- [#202](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202): ``request inventory ls``: default sort by created date
- [#202](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202): ``request folder ls``: default sort by created date
- [#202](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202): ``request change ls``: default sort by created date
- [#203](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/203): ``request snapshot set``: show ``from_date`` and ``to_date`` attributes

**Bug Fixes:**

- [#198](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/192): ``docs``: command typo in PV SCSI example

## [v0.2.6](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.6) (2019-10-31)

**Improvements:**

- [#196](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/196): ``core``: ``--table-format`` support for CSV

**Bug Fixes:**

- [#192](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/192): ``compute vm rm``: auto completion provides network objects
- [#193](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/193): ``core``: check available updates always provide an up-to-date package
- [#194](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/194): ``compute domain ls``: filters not working properly
- [#195](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/195): ``core``: ``--columns`` width exception thrown when empty result

## [v0.2.5](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.5) (2019-10-25)

**Improvements:**

- [#185](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/185): ``core``: pyvss upgrade from 0.9.42 -> 0.9.43
- [#186](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/186): ``compute vm set disk up``: `--mode` auto completion by api
- [#187](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/187): ``compute vm set controller scsi mk|up``: `--scsi-type` auto completion from API
- [#188](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/188): ``compute vm get console``: update client type
- [#189](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/189): ``core`` :`webdavclient3` dependency to optional
- [#190](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/190): ``compute domain ls``: command update based on `pyvss`

**Bug Fixes:**

- [#181](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/181): ``status``: command failed
- [#182](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/182): ``docs``: some typos or outdated information:  by [jm.lopez]

**New Features:**

- [#183](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/183): ``core``: `--columns-width` option to truncate column values based on user input or terminal size
- [#184](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/184): ``compute vm set vmrc-copy-paste on|off``: enable/disable VMRC copy paste

## [v0.2.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.4) (2019-10-10)

**Improvements:**

- [#174](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/174): ``core``: pyvss upgrade from 0.9.41 -> 0.9.42
- [#172](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172): ``compute vm set``: `--wait` flag support for multiple requests
- [#172](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172): ``compute vm mk``: `--wait` flag support for multiple requests
- [#172](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172): ``compute folder set``: `--wait` flag support for multiple requests
- [#172](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172): ``compute inventory mk``: `--wait` flag support for multiple requests
- [#179](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/179): ``compute vm mk``: sub-command standardization

**Bug Fixes:**

- [#168](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/168): ``docs``: network invalid option to change network adapter
- [#169](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/169): ``compute vm set cd mk``: schema exception when creating a cd
- [#170](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/170): ``message ls --filter``: filters do not work properly
- [#177](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/177): ``compute vm mk from-clone``: ``--extra-config`` flag missing
- [#178](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/178): ``compute vm mk``: ``--notes/-s`` duplicated

**New Features:**

- [#171](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/171): ``compute vm mk from-template``: ``--instances`` flag to deploy multiple instances concurrently
- [#173](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/173): ``compute vm mk shell``: ``--instances`` flag to deploy multiple instances concurrently
- [#175](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/175): ``compute vm mk from-clone``: ``--instances`` flag to deploy multiple instances concurrently
- [#176](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/176): ``compute vm mk from-spec``: ``--instances`` flag to deploy multiple instances concurrently


## [v0.2.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.3) (2019-09-20)

**Improvements:**

- [#156](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/156): ``compute inventory mk``: add ``--transfer/--no-transfer`` option to enable/disable transfer to vskey-stor
- [#157](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/157): ``compute mk set nic mk``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#158](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/158): ``compute vm set nic up``: support for new adapter type format ``--adapter``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute os ls``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm set guest-os``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk shell``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk from-template``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk from-clone``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk from-image``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk from-spec``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#159](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159): ``compute vm mk from-file``: updating camelCase to snake_case attributes: ``guestId``->``guest_id``
- [#160](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/160): ``compute vm set guest-os``: adding interactive options
- [#161](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/161): ``core``: update columns to match attributes in snake_case
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk shell``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk from-template``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk from-clone``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk from-image``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk from-spec``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#162](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162): ``compute vm mk from-file``: support for nic type in option ``-n <net-moref-name>=<nic-type>``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute folder ls``: command sorts by ``path,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute template ls``: command sorts by ``name,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute vm ls``: command sorts by ``name,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute image public ls``: command sorts by ``name,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute iso public ls``: command sorts by ``name,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute floppy public ls``: command sorts by ``name,asc``
- [#163](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163): ``compute net public ls``: command sorts by ``name,asc``
- [#164](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/164): ``docs``: inventory example
- [#166](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/166): ``core``: pyvss upgrade from 0.9.40 -> 0.9.41
- [#167](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167): ``compute vm set``: avoid clear screen when ``--wait`` flag is set:  [jm.lopez]
- [#167](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167): ``compute vm mk``: avoid clear screen when ``--wait`` flag is set:  [jm.lopez]
- [#167](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167): ``compute folder set``: avoid clear screen when ``--wait`` flag is set:  [jm.lopez]
- [#167](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167): ``compute inventory mk``: avoid clear screen when ``--wait`` flag is set:  [jm.lopez]


## [v0.2.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.2) (2019-09-05)

**Improvements:**

- [#145](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/145): ``core``: pyvss upgrade from 0.9.39 -> 0.9.40
- [#147](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/147): ``core``: ruamel.yaml upgrade to 0.16.5
- [#148](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/148): ``core``: Pygments upgrade to 2.4.2
- [#149](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/149): ``core``: click-plugins upgrade to 1.1.1
- [#151](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/151): ``core``: update `Configuration.get_images` attribute methods
- [#152](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/152): ``core``: autocompletion improvements
- [#154](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/154): ``ci``: check-in version and git SHA on VSS API

**Bug Fixes:**

- [#143](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/143): ``core``: `config.get_folder_by_name_or_moref_path` cannot find folder
- [#150](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/150): ``core``: autocompletion not populating all folders

**New Features:**

- [#153](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153): ``compute vm set``: Add a `--wait` flag to commands which generate requests
- [#153](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153): ``compute vm mk``: Add a `--wait` flag to commands which generate requests
- [#153](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153): ``compute folder set``: Add a `--wait` flag to commands which generate requests
- [#153](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153): ``compute inventory mk``: Add a `--wait` flag to commands which generate requests

## [v0.2.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.1) (2019-08-15)

**Improvements:**

- [#129](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/129): ``core``: pyvss upgrade from 0.9.38 -> 0.9.39
- [#131](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/131): ``docs``: vmware paravirtual scsi migration how-to
- [#133](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/133): ``core``: `vss` command as an alias of `vss-cli`
- [#135](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/135): ``docs``: known issues in docs/use.rst 
- [#137](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/137): ``compute vm ls``: improving filtering processing
- [#138](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/138): ``compute template ls``: improving filtering processing
- [#139](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/139): ``compute folder ls``: improving filtering processing
- [#140](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/140): ``compute net ls``: improving filtering processing
- [#141](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/141): ``compute os ls``: improving filtering processing
- [#142](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/142): ``compute iso public ls``: improving filtering processing
 
**Bug Fixes:**

- [#130](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/130): ``core``: `config.get_vm_by_uuid_or_name` cannot find templates
- [#132](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/132): ``core``: `config.get_vm_by_uuid_or_name` cannot find vms
- [#134](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/134): ``compute vm mk from-file``: `-s/--save` expects argument

## [v0.2.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.0) (2019-07-26)

**Improvements:**

- [#125](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/125): ``core``: pyvss upgrade from 0.9.36 -> 0.9.38
- [#124](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/124): ``compute vm ls``: add options to filter and sort: by  [jm.lopez]
- [#126](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/126): ``compute template ls``: add options to filter and sort: by  [jm.lopez]
- [#127](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/127): ``compute vm set disk up --backing-mode``: updates scsi controller used by disk

## [v0.1.9](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.9) (2019-07-19)

**Improvements:**

- [#122](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/122): ``core``: removing config.update_vm_floppy in favour of pyvss
- [#121](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/121): ``core``: pyvss upgrade from 0.9.35 -> 0.9.36
- [#119](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/119): ``compute vm get controller scsi``: command update
- [#118](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/118): ``compute vm get disk scsi``: provides scsi controller used by disk
- [#117](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/117): ``compute vm set disk up --scsi``: updates scsi controller used by disk
- [#116](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/116): ``compute folder get children``: gets children folder of a given folder
- [#115](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/115): ``compute folder get vm``: command update
- [#114](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/114): ``compute folder ls``: add options to filter and sort  [jm.lopez]

**New Features:**

- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): ``compute vm set controller scsi mk``: create vm scsi controllers
- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): ``compute vm set controller scsi up``: update vm scsi controllers
- [#120](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120): ``compute vm set controller scsi rm``: remove vm scsi controllers


## [v0.1.8](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.8) (2019-07-10)

**Improvements:**

- [#109](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/109): ``core``: pyvss upgrade from 0.9.34 -> 0.9.35
- [#107](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/107): ``compute net ls``: add new options to filter and sort
- [#108](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/108): ``compute net get``: update vms command backend
- [#111](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/111): ``compute vm set floppy``: improve image lookup and handling

**Bug Fixes:**

- [#106](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/106): ``docs``: project links > documentation typo in project docs url
- [#110](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/110): ``compute vm set nic mk``: error when creating cards
- [#112](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/112): ``compute vm set client``: update_vm_vss_client missing positional argument


## [v0.1.7](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.7) (2019-06-27)

**Improvements:**

- [#103](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/103): ``core``: update pyvss to 0.9.34
- [#102](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/102): ``compute vm get``: provide floppy attribute
- [#104](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104): ``compute vm set cd mk``: create cd/dvd devices
- [#104](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104): ``compute vm set cd up``: update cd/dvd devices

**Bug Fixes:**

- [#101](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/101): ``compute floppy personal sync``: fails to sync floppy images

## [v0.1.6](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.6) (2019-05-24)

**Improvements:**

- [#99](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/99): ``core``: update pyvss to 0.9.33

**Bug Fixes:**

- [#98](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/98): ``compute vm get nic``: command missing network moref using table format

## [v0.1.5](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.5) (2019-05-14)

**Improvements:**

- [#90](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/90): ``compute vm get spec``: generates a VSS-CLI specification
- [#91](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/91): ``compute vm mk from-file``: checks for VSS CLI specification
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): ``compute vm set extra-cfg mk``: create `guestinfo` option
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): ``compute vm set extra-cfg up``: update `guestinfo` option
- [#92](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92): ``compute vm set extra-cfg rm``: remove `guestinfo` option
- [#95](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/95): ``compute vm get console``: option to generate link for a given client (html5, flash, vmrc)
- [#96](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/96): ``core``: ruamel.yaml upgrade from 0.15.92 -> 0.15.94
- [#97](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/97): ``core``: pyvss upgrade from 0.9.30 -> 0.9.32

**Bug Fixes:**

- [#93](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/93): ``core``: autocompletion is not working properly with multi-endpoint configuration

## [v0.1.4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.4) (2019-05-06)

**Improvements:**

- [#82](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/82): ``core``: setup.cfg improvements
- [#85](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/85): ``core``: upgrade to py-vss v0.9.30
- [#86](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/86): ``token``: ls/get columns
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``token ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``service ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``message ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``key ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``compute floppy ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``compute image ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``compute iso ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``compute os ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request change ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request new ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request export ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request folder ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request image ls``: standardizing relational options
- [#88](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88): ``request inventory ls``: standardizing relational options

**Bug Fixes:**

- [#83](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/83): ``ci``: CI/Docker Job Failed #17142
- [#87](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/87): ``compute``: vm st snapshot rm - Unable to delete snapshot

## [v0.1.3](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.3) (2019-04-18)

**Improvements:**

- [#69](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/69): ``core``: Implement `ruamel.yaml` for yaml mgmt
- [#72](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/72): ``core``: spinner improvements
- [#78](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/78): ``core``: emoji handling/rendering improvements
- [#79](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/79): ``stor``: general improvements

**Bug Fixes:**

- [#68](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/68): ``core``: options are overridden by configuration file
- [#71](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/71): ``upgrade``: stable does not occur due to a missing argument
- [#73](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/73): ``service``: missing column name in table format
- [#74](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/74): ``core``: config.py aka ctx does not match services available
- [#75](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/75): ``configure mk``: missing default endpoint
- [#76](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/76): ``configure migrate``: unhandled exception with invalid configuration file
- [#77](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/77): ``configure set``: cannot change default_endpoint_name when invalid endpoint is found
- [#80](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/80): ``status``: command fails when there's no input format selected.

## [v0.1.2](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.2) (2019-04-12)

**Improvements:**

- [#67](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/67): ``core``: Provide user feedback while CLI processing [jm.lopez]

**Bug Fixes:**

- [#65](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/65): ``core``: configure command mismatch from autocompletion [jm.lopez]
- [#66](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/66): ``core``: configure upgrade missing description [jm.lopez]


## [v0.1.1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.1) (2019-04-05)

**Improvements:**

- [#54](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54): ``docs``: Windows installation steps
- [#55](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55): ``core``: Handle advanced configuration editable by users and via CLI
- [#57](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/57): ``docs``: docs/Add man page build and deploy stage to pipeline

**Bug Fixes:**

- [#63](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/63): ``compute floppy|folder|net``: invalid context in compute, floppy, folder and network commands
- [#61](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/61): ``core``: pyvss/AttributeError: 'Configuration' object has no attribute 'get_vss_services'
- [#59](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/59): ``account set notification request``: missing command account/set/notification/request
- [#58](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/58): ``message get``: message/get does not provide auto-completion
- [#56](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/56): ``upgrade``: vss-cli upgrade fails when there's no pip

**New Features:**

- [#62](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/62): ``request change set scheduled``: request/change/set scheduled and scheduled_datetime


## [v0.1.0](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.0) (2019-03-29)

**Improvements:**

- [#43](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/43): ``compute vm get spec``: download spec and save to file (yaml or json)
- [#50](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/50): ``upgrade``: command to support multiple code branches
- [#41](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/41): ``completion bash|zsh``: Auto-completion for managed objects
- [#32](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/32): ``docs``: Migrate documentation to new vss-cli command structure
- [#48](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/48): ``plugins``: Support externally-installable plugins
- [#40](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/40): ``tests``: Migrate Unit Testing from legacy VSSCLI
- [#37](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/37): ``ci``: Add bump2version to project to manage versioning
- [#36](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/36): ``ci``: Add GitLab Templates
- [#51](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/51): ``ci``: Implement ``isort`` and ``flake8`` in configuration file ``setup.cfg``
- [#42](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/42): ``compute vm mk from-file``:  improve vm creation with VSS-CLI specification file: thanks [alex.tremblay]
- [#53](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/53): ``vss-cli``: support externally-installable plugins scope improvement: by [alex.tremblay]

**Bug Fixes:**

- [#49](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/49): ``compute vm set --schedule``: not working properly
- [#44](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/44): ``vss-cli``: Auto-completion does not prioritize env var over files
- [#45](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/45): ``vss-cli --timeout``: Configuration.timeout not implemented

**New Features:**

- [#13](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/13): ``vss-cli``: Migrate VSSCLI to VSSCLI-NG
- [#4](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/4): ``configure``: Configure VSS CLI options
- [#20](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/20): ``compute``: Manage VMs, networks, folders, etc
- [#22](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/22): ``compute domain``: List domains available
- [#28](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/28): ``compute floppy``: Manage floppy images
- [#30](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/30): ``compute folder``: Manage logical folders
- [#27](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/27): ``compute image`` : Manage your OVA/OVF images
- [#24](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/24): ``compute inventory``: Manage inventory reports
- [#29](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/29): ``compute iso``: Manage ISO images
- [#25](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/25): ``compute net``: List available virtual networks
- [#26](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/26): ``compute os``: Supported OS
- [#31](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/31): ``compute template``: List virtual machine templates
- [#33](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/33): ``compute vm``: Manage virtual machines
- [#46](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/46): ``compute vm set|get vss-option``: Manage VSS options
- [#47](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/47): ``compute vm get|set vss-service``: Manage VSS Services
- [#23](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/23): ``shell``: REPL interactive shell
- [#18](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/18): ``stor``: Manage your personal storage space
- [#12](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/12): ``status``: Check VSS Status
- [#14](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/14): ``upgrade``: Upgrade VSS CLI and dependencies (experimental)
- [#1](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/1):   ``request``: Manage your different requests history
- [#15](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/15): ``token``: Manage your API tokens
- [#17](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/17): ``account``: Manage your VSS account
- [#16](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/16): ``message``: Manage user messages
- [#19](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/19): ``key``: Manage your SSH Public Keys
- [#34](https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/34): ``raw``: Raw calls to API

[jm.lopez]: https://gitlab-ee.eis.utoronto.ca/jm.lopez
[alex.tremblay]: https://gitlab-ee.eis.utoronto.ca/alex.tremblay
[pallets/click#472]: https://github.com/pallets/click/issues/472