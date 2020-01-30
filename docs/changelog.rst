
Changelog 📝
============

`v0.4.1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.4.1>`_ (2020-01-30)
--------------------------------------------------------------------------------------

**Improvements:**

- `#226 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/226>`_: ``core``: tabulate upgrade from 0.8.3 -> 0.8.6
- `#225 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/225>`_: ``core``: dateparser upgrade from 0.7.0 -> 0.7.2
- `#224 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/224>`_: ``core``: validators upgrade from 0.12.4 -> 0.14.2
- `#223 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/223>`_: ``core``: pick upgrade from 0.6.4 -> 0.6.6

**Bug Fixes:**

- `#222 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/222>`_: ``compute inventory dl --launch``: fails with exception.

`v0.4.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.4.0>`_ (2020-01-24)
--------------------------------------------------------------------------------------

**Improvements:**

- `#217 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/217>`_: ``core``: pyvss upgrade from 0.11.0 -> 0.12.0
- `#218 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/218>`_: ``compute vm set snapshot mk``: add ``--consolidate`` option
- `#219 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/219>`_: ``compute vm set ha-group mk``: create ``ha-group``
- `#219 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/219>`_: ``compute vm set ha-group rm``: remove current member from ``ha-group``

**Bug Fixes:**

- `#215 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/215>`_: ``docs``: ``bill-dept`` option was found in docs. Replaced with ``client``
- `#216 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/216>`_: ``compute vm set guest-cmd``: always fails.
- `#220 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/220>`_: ``ci``: release dist step fails due to missing os requirement


`v0.3.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.3.0>`_ (2019-11-14)
--------------------------------------------------------------------------------------

**Improvements:**


* `#211 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/211>`_\ : ``core``\ : pyvss upgrade from 0.9.43 -> 0.11.0
* `#210 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210>`_\ : ``compute vm mk from-clone``\ : rename ``--bill-dept`` to ``--client``\ : **breaking**
* `#210 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210>`_\ : ``compute vm mk from-file``\ : rename ``--bill-dept`` to ``--client``\ : **breaking**
* `#210 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210>`_\ : ``compute vm mk from-image``\ : rename\ ``--bill-dept`` to ``--client``\ : **breaking**
* `#210 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210>`_\ : ``compute vm mk from-spec``\ : rename ``--bill-dept`` to ``--client``\ : **breaking**
* `#210 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/210>`_\ : ``compute vm mk shell``\ : rename ``--bill-dept`` to ``--client``\ : **breaking**
* `#212 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/212>`_\ : ``compute vm rm from-template``\ : support for ``--wait`` flag
* `#208 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/208>`_\ : ``compute folder mk``\ : support for multiple values and ``--wait`` flag
* `#207 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/207>`_\ : ``compute folder rm``\ : support for multiple values and ``--wait`` flag

**Bug Fixes:**


* `#205 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/205>`_\ : ``docs``\ : missing changelog entry for v0.2.7
* `#209 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/209>`_\ : ``docs``\ : rst syntax warnings
* `#206 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/206>`_\ : ``compute folder rm``\ : fails with AttributeError

`v0.2.7 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.7>`_ (2019-11-08)
--------------------------------------------------------------------------------------

**Improvements:**


* `#199 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/199>`_\ : ``core``\ : pyvss upgrade from 0.9.43 -> 0.10.0
* `#200 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/200>`_\ : ``ci``\ : new items to gitignore
* `#201 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/201>`_\ : ``compute vm get state``\ : add ``create_date`` attribute
* `#202 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202>`_\ : ``request snapshot ls``\ : default sort by created date
* `#202 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202>`_\ : ``request new ls``\ : default sort by created date
* `#202 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202>`_\ : ``request inventory ls``\ : default sort by created date
* `#202 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202>`_\ : ``request folder ls``\ : default sort by created date
* `#202 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/202>`_\ : ``request change ls``\ : default sort by created date
* `#203 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/203>`_\ : ``request snapshot set``\ : show ``from_date`` and ``to_date`` attributes

**Bug Fixes:**


* `#198 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/192>`_\ : ``docs``\ : command typo in PV SCSI example

`v0.2.6 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.6>`_ (2019-10-31)
--------------------------------------------------------------------------------------

**Improvements:**


* `#196 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/196>`_\ : ``core``\ : ``--table-format`` support for CSV

**Bug Fixes:**


* `#192 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/192>`_\ : ``compute vm rm``\ : auto completion provides network objects
* `#193 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/193>`_\ : ``core``\ : check available updates always provide an up-to-date package
* `#194 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/194>`_\ : ``compute domain ls``\ : filters not working properly
* `#195 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/195>`_\ : ``core``\ : ``--columns`` width exception thrown when empty result

`v0.2.5 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.5>`_ (2019-10-25)
--------------------------------------------------------------------------------------

**Improvements:**


* `#185 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/185>`_\ : ``core``\ : pyvss upgrade from 0.9.42 -> 0.9.43
* `#186 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/186>`_\ : ``compute vm set disk up``\ : ``--mode`` auto completion by api
* `#187 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/187>`_\ : ``compute vm set controller scsi mk|up``\ : ``--scsi-type`` auto completion from API
* `#188 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/188>`_\ : ``compute vm get console``\ : update client type
* `#189 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/189>`_\ : ``core`` :`webdavclient3` dependency to optional
* `#190 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/190>`_\ : ``compute domain ls``\ : command update based on ``pyvss``

**Bug Fixes:**


* `#181 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/181>`_\ : ``status``\ : command failed
* `#182 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/182>`_\ : ``docs``\ : some typos or outdated information:  by `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_

**New Features:**


* `#183 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/183>`_\ : ``core``\ : ``--columns-width`` option to truncate column values based on user input or terminal size
* `#184 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/184>`_\ : ``compute vm set vmrc-copy-paste on|off``\ : enable/disable VMRC copy paste

`v0.2.4 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.4>`_ (2019-10-10)
--------------------------------------------------------------------------------------

**Improvements:**


* `#174 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/174>`_\ : ``core``\ : pyvss upgrade from 0.9.41 -> 0.9.42
* `#172 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172>`_\ : ``compute vm set``\ : ``--wait`` flag support for multiple requests
* `#172 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172>`_\ : ``compute vm mk``\ : ``--wait`` flag support for multiple requests
* `#172 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172>`_\ : ``compute folder set``\ : ``--wait`` flag support for multiple requests
* `#172 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/172>`_\ : ``compute inventory mk``\ : ``--wait`` flag support for multiple requests
* `#179 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/179>`_\ : ``compute vm mk``\ : sub-command standardization

**Bug Fixes:**


* `#168 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/168>`_\ : ``docs``\ : network invalid option to change network adapter
* `#169 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/169>`_\ : ``compute vm set cd mk``\ : schema exception when creating a cd
* `#170 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/170>`_\ : ``message ls --filter``\ : filters do not work properly
* `#177 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/177>`_\ : ``compute vm mk from-clone``\ : ``--extra-config`` flag missing
* `#178 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/178>`_\ : ``compute vm mk``\ : ``--notes/-s`` duplicated

**New Features:**


* `#171 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/171>`_\ : ``compute vm mk from-template``\ : ``--instances`` flag to deploy multiple instances concurrently
* `#173 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/173>`_\ : ``compute vm mk shell``\ : ``--instances`` flag to deploy multiple instances concurrently
* `#175 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/175>`_\ : ``compute vm mk from-clone``\ : ``--instances`` flag to deploy multiple instances concurrently
* `#176 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/176>`_\ : ``compute vm mk from-spec``\ : ``--instances`` flag to deploy multiple instances concurrently

`v0.2.3 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.3>`_ (2019-09-20)
--------------------------------------------------------------------------------------

**Improvements:**


* `#156 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/156>`_\ : ``compute inventory mk``\ : add ``--transfer/--no-transfer`` option to enable/disable transfer to vskey-stor
* `#157 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/157>`_\ : ``compute mk set nic mk``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#158 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/158>`_\ : ``compute vm set nic up``\ : support for new adapter type format ``--adapter``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute os ls``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm set guest-os``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk shell``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk from-template``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk from-clone``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk from-image``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk from-spec``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#159 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/159>`_\ : ``compute vm mk from-file``\ : updating camelCase to snake_case attributes: ``guestId``\ ->\ ``guest_id``
* `#160 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/160>`_\ : ``compute vm set guest-os``\ : adding interactive options
* `#161 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/161>`_\ : ``core``\ : update columns to match attributes in snake_case
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk shell``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk from-template``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk from-clone``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk from-image``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk from-spec``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#162 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/162>`_\ : ``compute vm mk from-file``\ : support for nic type in option ``-n <net-moref-name>=<nic-type>``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute folder ls``\ : command sorts by ``path,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute template ls``\ : command sorts by ``name,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute vm ls``\ : command sorts by ``name,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute image public ls``\ : command sorts by ``name,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute iso public ls``\ : command sorts by ``name,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute floppy public ls``\ : command sorts by ``name,asc``
* `#163 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/163>`_\ : ``compute net public ls``\ : command sorts by ``name,asc``
* `#164 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/164>`_\ : ``docs``\ : inventory example
* `#166 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/166>`_\ : ``core``\ : pyvss upgrade from 0.9.40 -> 0.9.41
* `#167 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167>`_\ : ``compute vm set``\ : avoid clear screen when ``--wait`` flag is set:  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#167 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167>`_\ : ``compute vm mk``\ : avoid clear screen when ``--wait`` flag is set:  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#167 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167>`_\ : ``compute folder set``\ : avoid clear screen when ``--wait`` flag is set:  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#167 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/167>`_\ : ``compute inventory mk``\ : avoid clear screen when ``--wait`` flag is set:  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_

`v0.2.2 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.2>`_ (2019-09-05)
--------------------------------------------------------------------------------------

**Improvements:**


* `#145 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/145>`_\ : ``core``\ : pyvss upgrade from 0.9.39 -> 0.9.40
* `#147 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/147>`_\ : ``core``\ : ruamel.yaml upgrade to 0.16.5
* `#148 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/148>`_\ : ``core``\ : Pygments upgrade to 2.4.2
* `#149 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/149>`_\ : ``core``\ : click-plugins upgrade to 1.1.1
* `#151 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/151>`_\ : ``core``\ : update ``Configuration.get_images`` attribute methods
* `#152 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/152>`_\ : ``core``\ : autocompletion improvements
* `#154 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/154>`_\ : ``ci``\ : check-in version and git SHA on VSS API

**Bug Fixes:**


* `#143 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/143>`_\ : ``core``\ : ``config.get_folder_by_name_or_moref_path`` cannot find folder
* `#150 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/150>`_\ : ``core``\ : autocompletion not populating all folders

**New Features:**


* `#153 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153>`_\ : ``compute vm set``\ : Add a ``--wait`` flag to commands which generate requests
* `#153 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153>`_\ : ``compute vm mk``\ : Add a ``--wait`` flag to commands which generate requests
* `#153 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153>`_\ : ``compute folder set``\ : Add a ``--wait`` flag to commands which generate requests
* `#153 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/153>`_\ : ``compute inventory mk``\ : Add a ``--wait`` flag to commands which generate requests

`v0.2.1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.1>`_ (2019-08-15)
--------------------------------------------------------------------------------------

**Improvements:**


* `#129 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/129>`_\ : ``core``\ : pyvss upgrade from 0.9.38 -> 0.9.39
* `#131 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/131>`_\ : ``docs``\ : vmware paravirtual scsi migration how-to
* `#133 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/133>`_\ : ``core``\ : ``vss`` command as an alias of ``vss-cli``
* `#135 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/135>`_\ : ``docs``\ : known issues in docs/use.rst 
* `#137 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/137>`_\ : ``compute vm ls``\ : improving filtering processing
* `#138 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/138>`_\ : ``compute template ls``\ : improving filtering processing
* `#139 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/139>`_\ : ``compute folder ls``\ : improving filtering processing
* `#140 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/140>`_\ : ``compute net ls``\ : improving filtering processing
* `#141 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/141>`_\ : ``compute os ls``\ : improving filtering processing
* `#142 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/142>`_\ : ``compute iso public ls``\ : improving filtering processing

**Bug Fixes:**


* `#130 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/130>`_\ : ``core``\ : ``config.get_vm_by_uuid_or_name`` cannot find templates
* `#132 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/132>`_\ : ``core``\ : ``config.get_vm_by_uuid_or_name`` cannot find vms
* `#134 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/134>`_\ : ``compute vm mk from-file``\ : ``-s/--save`` expects argument

`v0.2.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.2.0>`_ (2019-07-26)
--------------------------------------------------------------------------------------

**Improvements:**


* `#125 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/125>`_\ : ``core``\ : pyvss upgrade from 0.9.36 -> 0.9.38
* `#124 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/124>`_\ : ``compute vm ls``\ : add options to filter and sort: by  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#126 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/126>`_\ : ``compute template ls``\ : add options to filter and sort: by  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#127 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/127>`_\ : ``compute vm set disk up --backing-mode``\ : updates scsi controller used by disk

`v0.1.9 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.9>`_ (2019-07-19)
--------------------------------------------------------------------------------------

**Improvements:**


* `#122 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/122>`_\ : ``core``\ : removing config.update_vm_floppy in favour of pyvss
* `#121 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/121>`_\ : ``core``\ : pyvss upgrade from 0.9.35 -> 0.9.36
* `#119 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/119>`_\ : ``compute vm get controller scsi``\ : command update
* `#118 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/118>`_\ : ``compute vm get disk scsi``\ : provides scsi controller used by disk
* `#117 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/117>`_\ : ``compute vm set disk up --scsi``\ : updates scsi controller used by disk
* `#116 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/116>`_\ : ``compute folder get children``\ : gets children folder of a given folder
* `#115 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/115>`_\ : ``compute folder get vm``\ : command update
* `#114 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/114>`_\ : ``compute folder ls``\ : add options to filter and sort  `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_

**New Features:**


* `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_\ : ``compute vm set controller scsi mk``\ : create vm scsi controllers
* `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_\ : ``compute vm set controller scsi up``\ : update vm scsi controllers
* `#120 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/120>`_\ : ``compute vm set controller scsi rm``\ : remove vm scsi controllers

`v0.1.8 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.8>`_ (2019-07-10)
--------------------------------------------------------------------------------------

**Improvements:**


* `#109 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/109>`_\ : ``core``\ : pyvss upgrade from 0.9.34 -> 0.9.35
* `#107 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/107>`_\ : ``compute net ls``\ : add new options to filter and sort
* `#108 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/108>`_\ : ``compute net get``\ : update vms command backend
* `#111 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/111>`_\ : ``compute vm set floppy``\ : improve image lookup and handling

**Bug Fixes:**


* `#106 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/106>`_\ : ``docs``\ : project links > documentation typo in project docs url
* `#110 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/110>`_\ : ``compute vm set nic mk``\ : error when creating cards
* `#112 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/112>`_\ : ``compute vm set client``\ : update_vm_vss_client missing positional argument

`v0.1.7 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.7>`_ (2019-06-27)
--------------------------------------------------------------------------------------

**Improvements:**


* `#103 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/103>`_\ : ``core``\ : update pyvss to 0.9.34
* `#102 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/102>`_\ : ``compute vm get``\ : provide floppy attribute
* `#104 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104>`_\ : ``compute vm set cd mk``\ : create cd/dvd devices
* `#104 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/104>`_\ : ``compute vm set cd up``\ : update cd/dvd devices

**Bug Fixes:**


* `#101 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/101>`_\ : ``compute floppy personal sync``\ : fails to sync floppy images

`v0.1.6 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.6>`_ (2019-05-24)
--------------------------------------------------------------------------------------

**Improvements:**


* `#99 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/99>`_\ : ``core``\ : update pyvss to 0.9.33

**Bug Fixes:**


* `#98 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/98>`_\ : ``compute vm get nic``\ : command missing network moref using table format

`v0.1.5 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.5>`_ (2019-05-14)
--------------------------------------------------------------------------------------

**Improvements:**


* `#90 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/90>`_\ : ``compute vm get spec``\ : generates a VSS-CLI specification
* `#91 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/91>`_\ : ``compute vm mk from-file``\ : checks for VSS CLI specification
* `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_\ : ``compute vm set extra-cfg mk``\ : create ``guestinfo`` option
* `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_\ : ``compute vm set extra-cfg up``\ : update ``guestinfo`` option
* `#92 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/92>`_\ : ``compute vm set extra-cfg rm``\ : remove ``guestinfo`` option
* `#95 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/95>`_\ : ``compute vm get console``\ : option to generate link for a given client (html5, flash, vmrc)
* `#96 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/96>`_\ : ``core``\ : ruamel.yaml upgrade from 0.15.92 -> 0.15.94
* `#97 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/97>`_\ : ``core``\ : pyvss upgrade from 0.9.30 -> 0.9.32

**Bug Fixes:**


* `#93 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/93>`_\ : ``core``\ : autocompletion is not working properly with multi-endpoint configuration

`v0.1.4 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.4>`_ (2019-05-06)
--------------------------------------------------------------------------------------

**Improvements:**


* `#82 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/82>`_\ : ``core``\ : setup.cfg improvements
* `#85 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/85>`_\ : ``core``\ : upgrade to py-vss v0.9.30
* `#86 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/86>`_\ : ``token``\ : ls/get columns
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``token ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``service ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``message ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``key ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``compute floppy ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``compute image ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``compute iso ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``compute os ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request change ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request new ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request export ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request folder ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request image ls``\ : standardizing relational options
* `#88 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/88>`_\ : ``request inventory ls``\ : standardizing relational options

**Bug Fixes:**


* `#83 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/83>`_\ : ``ci``\ : CI/Docker Job Failed #17142
* `#87 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/87>`_\ : ``compute``\ : vm st snapshot rm - Unable to delete snapshot

`v0.1.3 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.3>`_ (2019-04-18)
--------------------------------------------------------------------------------------

**Improvements:**


* `#69 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/69>`_\ : ``core``\ : Implement ``ruamel.yaml`` for yaml mgmt
* `#72 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/72>`_\ : ``core``\ : spinner improvements
* `#78 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/78>`_\ : ``core``\ : emoji handling/rendering improvements
* `#79 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/79>`_\ : ``stor``\ : general improvements

**Bug Fixes:**


* `#68 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/68>`_\ : ``core``\ : options are overridden by configuration file
* `#71 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/71>`_\ : ``upgrade``\ : stable does not occur due to a missing argument
* `#73 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/73>`_\ : ``service``\ : missing column name in table format
* `#74 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/74>`_\ : ``core``\ : config.py aka ctx does not match services available
* `#75 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/75>`_\ : ``configure mk``\ : missing default endpoint
* `#76 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/76>`_\ : ``configure migrate``\ : unhandled exception with invalid configuration file
* `#77 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/77>`_\ : ``configure set``\ : cannot change default_endpoint_name when invalid endpoint is found
* `#80 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/80>`_\ : ``status``\ : command fails when there's no input format selected.

`v0.1.2 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.2>`_ (2019-04-12)
--------------------------------------------------------------------------------------

**Improvements:**


* `#67 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/67>`_\ : ``core``\ : Provide user feedback while CLI processing `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_

**Bug Fixes:**


* `#65 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/65>`_\ : ``core``\ : configure command mismatch from autocompletion `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_
* `#66 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/66>`_\ : ``core``\ : configure upgrade missing description `jm.lopez <https://gitlab-ee.eis.utoronto.ca/jm.lopez>`_

`v0.1.1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.1>`_ (2019-04-05)
--------------------------------------------------------------------------------------

**Improvements:**


* `#54 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/54>`_\ : ``docs``\ : Windows installation steps
* `#55 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/55>`_\ : ``core``\ : Handle advanced configuration editable by users and via CLI
* `#57 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/57>`_\ : ``docs``\ : docs/Add man page build and deploy stage to pipeline

**Bug Fixes:**


* `#63 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/63>`_\ : ``compute floppy|folder|net``\ : invalid context in compute, floppy, folder and network commands
* `#61 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/61>`_\ : ``core``\ : pyvss/AttributeError: 'Configuration' object has no attribute 'get_vss_services'
* `#59 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/59>`_\ : ``account set notification request``\ : missing command account/set/notification/request
* `#58 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/58>`_\ : ``message get``\ : message/get does not provide auto-completion
* `#56 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/56>`_\ : ``upgrade``\ : vss-cli upgrade fails when there's no pip

**New Features:**


* `#62 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/62>`_\ : ``request change set scheduled``\ : request/change/set scheduled and scheduled_datetime

`v0.1.0 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/tags/v0.1.0>`_ (2019-03-29)
--------------------------------------------------------------------------------------

**Improvements:**


* `#43 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/43>`_\ : ``compute vm get spec``\ : download spec and save to file (yaml or json)
* `#50 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/50>`_\ : ``upgrade``\ : command to support multiple code branches
* `#41 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/41>`_\ : ``completion bash|zsh``\ : Auto-completion for managed objects
* `#32 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/32>`_\ : ``docs``\ : Migrate documentation to new vss-cli command structure
* `#48 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/48>`_\ : ``plugins``\ : Support externally-installable plugins
* `#40 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/40>`_\ : ``tests``\ : Migrate Unit Testing from legacy VSSCLI
* `#37 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/37>`_\ : ``ci``\ : Add bump2version to project to manage versioning
* `#36 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/36>`_\ : ``ci``\ : Add GitLab Templates
* `#51 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/51>`_\ : ``ci``\ : Implement ``isort`` and ``flake8`` in configuration file ``setup.cfg``
* `#42 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/42>`_\ : ``compute vm mk from-file``\ :  improve vm creation with VSS-CLI specification file: thanks `alex.tremblay <https://gitlab-ee.eis.utoronto.ca/alex.tremblay>`_
* `#53 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/53>`_\ : ``vss-cli``\ : support externally-installable plugins scope improvement: by `alex.tremblay <https://gitlab-ee.eis.utoronto.ca/alex.tremblay>`_

**Bug Fixes:**


* `#49 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/49>`_\ : ``compute vm set --schedule``\ : not working properly
* `#44 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/44>`_\ : ``vss-cli``\ : Auto-completion does not prioritize env var over files
* `#45 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/45>`_\ : ``vss-cli --timeout``\ : Configuration.timeout not implemented

**New Features:**


* `#13 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/13>`_\ : ``vss-cli``\ : Migrate VSSCLI to VSSCLI-NG
* `#4 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/4>`_\ : ``configure``\ : Configure VSS CLI options
* `#20 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/20>`_\ : ``compute``\ : Manage VMs, networks, folders, etc
* `#22 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/22>`_\ : ``compute domain``\ : List domains available
* `#28 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/28>`_\ : ``compute floppy``\ : Manage floppy images
* `#30 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/30>`_\ : ``compute folder``\ : Manage logical folders
* `#27 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/27>`_\ : ``compute image`` : Manage your OVA/OVF images
* `#24 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/24>`_\ : ``compute inventory``\ : Manage inventory reports
* `#29 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/29>`_\ : ``compute iso``\ : Manage ISO images
* `#25 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/25>`_\ : ``compute net``\ : List available virtual networks
* `#26 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/26>`_\ : ``compute os``\ : Supported OS
* `#31 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/31>`_\ : ``compute template``\ : List virtual machine templates
* `#33 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/33>`_\ : ``compute vm``\ : Manage virtual machines
* `#46 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/46>`_\ : ``compute vm set|get vss-option``\ : Manage VSS options
* `#47 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/47>`_\ : ``compute vm get|set vss-service``\ : Manage VSS Services
* `#23 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/23>`_\ : ``shell``\ : REPL interactive shell
* `#18 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/18>`_\ : ``stor``\ : Manage your personal storage space
* `#12 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/12>`_\ : ``status``\ : Check VSS Status
* `#14 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/14>`_\ : ``upgrade``\ : Upgrade VSS CLI and dependencies (experimental)
* `#1 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/1>`_\ :   ``request``\ : Manage your different requests history
* `#15 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/15>`_\ : ``token``\ : Manage your API tokens
* `#17 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/17>`_\ : ``account``\ : Manage your VSS account
* `#16 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/16>`_\ : ``message``\ : Manage user messages
* `#19 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/19>`_\ : ``key``\ : Manage your SSH Public Keys
* `#34 <https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/issues/34>`_\ : ``raw``\ : Raw calls to API
