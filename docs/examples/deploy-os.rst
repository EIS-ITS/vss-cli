.. _DeployOS:

Deploying a Development Environment
===================================

This tutorial details how to deploy a development environment in the ITS Private Cloud using
the VSS CLI. It assumes you already have set up a VSS account with access to the REST API.

Install VSS CLI
---------------
Install VSS CLI either by using `pip`_, from source `download the tarball`_ or from
UofT's `GitLab instance`_.

Linux, macOS, Unix
~~~~~~~~~~~~~~~~~~

Python 2.7 is prerequired to run the following steps:

1. Download `pip`_:

.. code-block:: bash

    curl https://bootstrap.pypa.io/get-pip.py | python

2. Install VSS CLI using `pip`_:

.. code-block:: bash

    pip install vsscli

3. Test VSS CLI by running ``--version``:

.. code-block:: bash

    vss --version


Configure VSS CLI
-----------------

Run ``vss configure`` at the command line to set up your credentials:

.. code-block:: bash

    vss configure
    Username []: username
    Password:
    Repeat for confirmation:



Launch Instance
---------------

Before launching the virtual machine instance we need the following items:

* Operating system
* Network
* Folder
* ISO image

Then, all is ready to deploy a brand new virtual machine.

Operating system
~~~~~~~~~~~~~~~~

Run ``vss compute os ls`` to display the list of supported operating systems in
the ITS Private Cloud. In order to narrow down the list to only **CentOS** operating
systems, use the ``--filter/-f`` option which is structured
``<field_name>,<operator>,<value>`` and available operators are
**eq, ne, lt, le, gt, ge, like, in**. So, to limit results to just **CentOS**, use
the following filter:


.. code-block:: bash

    vss compute os ls --filter guestFullName,like,CentOS%
      id  guestId        guestFullName
    ----  -------------  -------------------
       8  centosGuest    CentOS 4/5
      11  centos64Guest  CentOS 4/5 (64-bit)

Set the ``OS`` environment variable to ``centos64Guest`` to save the ``guestId``:

.. code-block:: bash

    export OS=centos64Guest


Network
~~~~~~~

Run ``vss compute net ls`` to list available network segments to your account. You must
have at least ``VL-1584-VSS-PUBLIC`` which is our public network.

.. code-block:: bash

    vss compute net ls -f name public
    moref              name                description         subnet            ports
    -----------------  ------------------  ------------------  --------------  -------
    dvportgroup-11052  VL-1584-VSS-PUBLIC  VSS Public network  142.1.216.0/23       32



Save ``dvportgroup-11052`` in ``NET`` environment variable:

.. code-block:: bash

    export NET=dvportgroup-11052

Folder
~~~~~~

Logical folders can be listed by running ``vss compute folder ls``. Select the target
``moref`` folder to store the virtual machine on:

.. code-block:: bash

    vss compute folder ls -f name API
    moref        name     parent    path
    -----------  -------  --------  ----------------------------
    group-v6736  APIDemo  jm        jm > Demo

Set the ``FOLDER`` environment variable to the target folder (the folder moref may vary):

.. code-block:: bash

    export FOLDER=group-v6736


ISO Image
~~~~~~~~~

Since this tutorial creates a virtual machine from scratch, an ISO image is required to
install the operating system. Run ``vss compute iso public ls`` to display  available
ISO images in both the VSS central store and your personal VSKEY-STOR space.

.. code-block:: bash

    vss compute iso public ls -f name like,Cent%
    path                                                           name
    -------------------------------------------------------------  -------------------------------------
    [vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-DVD.iso         CentOS-7.0-1406-x86_64-DVD.iso
    [vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-NetInstall.iso  CentOS-7.0-1406-x86_64-NetInstall.iso
    [vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-Minimal.iso     CentOS-7.0-1406-x86_64-Minimal.iso

Save the desired path to ``ISO`` environment variable:

.. code-block:: bash

    export ISO="[vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-DVD.iso"

Deployment
~~~~~~~~~~

Run ``vss compute vm mk shell`` to deploy a virtual machine without an operating system
installed. Before deploying the virtual machine, display what options and arguments the ``shell``
command takes:


.. code-block:: bash

    Usage: vss compute vm mk shell [OPTIONS] NAME

      Create a new virtual machine with no operating system pre-installed.

    Options:
      -d, --description TEXT          Vm description.  [required]
      -b, --bill-dept TEXT            Billing department.  [required]
      -u, --usage [Test|Prod|Dev|QA]  Vm usage.
      -o, --os TEXT                   Guest operating system id.  [required]
      -m, --memory INTEGER            Memory in GB.
      -c, --cpu INTEGER               Cpu count.
      -f, --folder TEXT               Logical folder moref.  [required]
      -i, --disk INTEGER              Disks in GB.
      -n, --net TEXT                  Networks moref mapped to NICs.  [required]
      -s, --iso TEXT                  ISO image path to be mounted after creation
      -m, --domain TEXT               Target fault domain.
      -h, --high-io                   VM will be created with a VMware Paravirtual
                                      SCSIController.
      -t, --notes TEXT                Custom notes.
      --help                          Show this message and exit.

Now that we have everything, proceed to deploy a new virtual machine with 1GB of memory,
1 vCPU, 20GB disk and a tag Project:CMS as follows:

.. code-block:: bash

    vss compute vm mk shell --description 'NGINX web server' --bill-dept EIS --os $OS \
    --memory 1 --cpu 1 --folder $FOLDER --disk 20 --net $NET --iso "$ISO" --notes 'Project: CMS' \
    FrontEnd_1

A confirmation email will be sent and the command will return the request ``id`` and
``task_id`` as follows:

.. code-block:: bash

    status              : 202
    request             : status: Submitted, id: 1150, task_id: 7c32e09a-b36b-4b89-b6a5-ffc91045db4f
    message             : Request has been accepted for processing
    name                : Accepted


In matter of seconds, a confirmation email will be sent with the allocated IP address, if
``VL-1584-VSS-PUBLIC`` was selected.

Manage Request
--------------

If you prefer to validate the status of the request with VSS CLI, run ``vss request new ls`` to
display a list of your request history.

This command supports filter and sorting by using the ``--filter/-f`` and ``--sort/-s``
respectively. Filter list in the following format ``<field_name>,<operator>,<value>``
where operator is **eq, ne, lt, le, gt, ge, like, in**. For example: status,eq,Processed.
Sort list in the following format ``<field_name>,<asc|desc>``.

In order to obtain the last request submitted, status and resulting virtual machine ``uuid``, run
the following command:

.. code-block:: bash

    vss request new ls -s created_on,desc -c 1
      id  created_on               updated_on               status     vm_name           vm_uuid
    ----  -----------------------  -----------------------  ---------  ----------------  ------------------------------------
    1150  2017-03-13 13:11:41 EDT  2017-03-13 13:12:00 EDT  Processed  1703T-FrontEnd_1  5012f74a-4243-6664-20a9-0993567fbb7e


Access Instance
---------------

The previous command has shown the virtual machine has been successfully created and it has been
assigned ``5012f74a-4243-6664-20a9-0993567fbb7e`` as ``uuid``. To validate the ISO is mounted, run
``vss compute vm get <uuid> cd 1``:

.. code-block:: bash

    vss compute vm get 5012f74a-4243-6664-20a9-0993567fbb7e cd 1
    Uuid                : 5012f74a-4243-6664-20a9-0993567fbb7e
    Label               : CD/DVD drive 1
    Backing             : [vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-DVD.iso
    Connected           : Disconnected
    Controller Type     : IDE 0
    Controller Virtual Device Node: IDE 0:0

Confirming the ISO has been successfully mounted upon provisioning, update the state to ``on`` using
``vss compute vm <uuid> set state on`` as follows:

.. code-block:: bash

    vss compute vm set 5012f74a-4243-6664-20a9-0993567fbb7e state on

A confirmation email will be sent and the command will return the request ``id`` and
``task_id`` as follows:

.. code-block:: bash

    status              : 202
    request             : status: Submitted, id: 5646, task_id: 1c2caca0-5038-4779-8d66-74db39650d57
    message             : Request has been accepted for processing
    name                : Accepted

Launch a one-time link to the virtual machine console with ``vss compute vm get <uuid> console``
and proceed with the operating system install:

.. code-block:: bash

    vss compute vm get 5012f74a-4243-6664-20a9-0993567fbb7e console -l

.. warning:: To generate a console link you just need to have a valid vSphere session
  (unfortunately), and this is due to the nature of vSphere API.

.. image:: centos-install.png


.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
.. _`WebdavClient`: http://designerror.github.io/webdav-client-python/
.. _pip: http://www.pip-installer.org/en/latest/
.. _`download the tarball`: https://pypi.python.org/pypi/vsscli
.. _`GitLab instance`: https://gitlab-ee.eis.utoronto.ca/vss/vsscli
