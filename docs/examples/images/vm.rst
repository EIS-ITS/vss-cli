.. _VM__OVA_Images:

Manage Virtual Machine OVA/OVF Images with the vss-cli
======================================================

The ITS Private Cloud API has the ability to deploy OVA or
OVF virtual machines from either our public repository or an
Open Virtualization Format file provided by a user and
uploaded to `VSKEY-STOR`_, either for a single or multiple deployments.

Public and personal VM images can be managed with the
``vss-cli compute image`` command:

.. code-block:: bash

    Usage: vss-cli compute image [OPTIONS] COMMAND [ARGS]...

      Available OVA/OVF images in both the VSS central store and your personal
      VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      personal  Browse current user images
      public    Browse public images


Public
~~~~~~
The public repository holds an OVA catalog of common linux distributions
such as Ubuntu, VMware PhotonOS and CoreOS optimized for cloud deployment.

Currently, users can only list and use public VM images with
``vss-cli compute image public ls`` and those can be filtered and sorted
with including the proper options:

.. code-block:: bash

    Usage: vss-cli compute image public ls [OPTIONS]

      List available OVA/OVF VM images in the VSS central store.

      Filter by name and sort desc. For example:

          vss-cli compute image public ls -f name=like,Cent% -s path asc

    Options:
      -f, --filter-by <TEXT TEXT>...  filter list by <field_name>
                                      <operator>,<value>
      -s, --sort <TEXT TEXT>...       sort by <field_name> <asc|desc>
      -a, --show-all                  show all results  [default: False]
      -p, --page                      page results in a less-like format
      --help                          Show this message and exit.

For instance, to look for a publicly available **Photon OS** image,
the command could be something like:

.. code-block:: bash

    vss-cli compute image public ls -f name=like,%photon% -s path asc

    path                                                              name
    ----------------------------------------------------------------  ----------------------------------
    [vss-ISOs] VmImages/photon-os/photon-custom-hw11-2.0-304b817.ova  photon-custom-hw11-2.0-304b817.ova
    [vss-ISOs] VmImages/photon-os/photon-custom-hw13-2.0-304b817.ova  photon-custom-hw13-2.0-304b817.ova


.. note:: To successfully deploy a VM from a public VM image, **Path** should be added to the VM command.

For further instructions on how to deploy a virtual machine from
image, please refer to :doc:`Deploy Instance from Image <deploy-image>`.


Personal
~~~~~~~~

User provided VM images can be managed with the
``vss-cli compute image personal`` command:

.. code-block:: bash

    Usage: vss-cli compute image personal [OPTIONS] COMMAND [ARGS]...

      Available OVA/OVF VM images in your personal VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      ls    list personal OVA/OVF VM images
      sync  Sync personal OVA/OVF VM images


In order to deploy a VM from a provided VM image, users should **upload**
the file to `VSKEY-STOR`_ and then execute a ``sync`` command to make the
image file available in the ITS Private Cloud.

.. note:: Assuming you have already uploaded the OVA file or OVF+Disks (VMDKs), the command
    ``vss-cli compute image personal sync`` should be executed.

Once you get a confirmation notification (email or message) VM images
should be visible through the CLI. To list just execute
``vss-cli compute image personal ls`` and the output should look as follows:

.. code-block:: bash

    vss-cli compute image personal ls
    path                                                                                     name
    ---------------------------------------------------------------------------------------  ---------------------------------------
    [vssUser-xfers] jm/images/photon-custom-hw10-1.0-13c08b6-GA.ova                          photon-custom-hw10-1.0-13c08b6-GA.ova
    [vssUser-xfers] jm/images/CentOS_64-bit_vmx10.ova                                        CentOS_64-bit_vmx10.ova
    [vssUser-xfers] jm/images/graylog-2.1.2-1.ova                                            graylog-2.1.2-1.ova
    [vssUser-xfers] jm/images/wily-server-cloudimg-amd64.ova                                 wily-server-cloudimg-amd64.ova
    [vssUser-xfers] jm/images/photon-custom-hw10-1.0-13c08b6.ova                             photon-custom-hw10-1.0-13c08b6.ova

For further instructions on how to deploy a virtual machine from image,
please refer to :doc:`Deploy Instance from Image <deploy-image>`.

.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
