.. _Floppy_Images:

Manage Floppy Images wit the vss-cli
======================================

In some operating systems, such as the most recent versions of Windows,
you need to provide the device drivers to properly recognize basic devices
like the **VMXNET3** network adapter or **Paravirtual SCSi controllers**.
These drivers are provided by VMware and now, they are available
for you to use on demand by the ``floppy`` command ``vss-cli compute floppy``.

.. code-block:: bash

    Usage: vss-cli compute floppy [OPTIONS] COMMAND [ARGS]...

      Available floppy images in both the VSS central store and your personal
      VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      personal  Browse current user images
      public    Browse public images


Public
~~~~~~

Currently, users can only list and use public Floppy images with
``vss-cli compute floppy public ls`` and those can be filtered and
sorted with including the proper options:

.. code-block:: bash

    Usage: vss-cli compute floppy public ls [OPTIONS]

      List available Floppy images in the VSS central store.

      Filter by path or name path=<path> or name=<name>. For example:

          vss-cli compute floppy ls -f name=like,pv% -s path asc

    Options:
      -f, --filter-by <TEXT TEXT>...  filter list by <field_name>
                                      <operator>,<value>
      -s, --sort <TEXT TEXT>...       sort by <field_name> <asc|desc>
      -a, --show-all                  show all results  [default: False]
      -p, --page                      page results in a less-like format
      --help                          Show this message and exit.


For instance, to look for a **Windows** drivers image, the command
should be something like:


.. code-block:: bash

    vss-cli compute floppy public ls -f name=like,%Windows%

    path                                          name
    --------------------------------------------  ----------------------
    [] /vmimages/floppies/pvscsi-Windows2008.flp  pvscsi-Windows2008.flp
    [] /vmimages/floppies/pvscsi-Windows2003.flp  pvscsi-Windows2003.flp
    [] /vmimages/floppies/pvscsi-WindowsXP.flp    pvscsi-WindowsXP.flp

The process of mounting the image to a VM is the same:
first get the VM UUID and then execute
``vss-cli compute vm set <name-or-uuid> floppy <unit> --image <path>`` as shown below:

.. code-block:: bash

    vss-cli compute vm set 501257e0-81f5-9c2a-84e5-e900212fef76 floppy 1 --image "[] /vmimages/floppies/pvscsi-Windows2008.flp"


Personal
~~~~~~~~
The ``floppy`` command resource also provides available ``.flp``
images from your `VSKEY-STOR`_ space, so you are free to upload any
custom floppy image and mount it to a Virtual Machine.

User provided VM images can be managed with the
``vss-cli compute floppy personal`` command:

.. code-block:: bash

    Usage: vss-cli compute floppy personal [OPTIONS] COMMAND [ARGS]...

      Available Floppy images in your personal VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      ls    list personal Floppy images
      sync  Sync personal Floppy images


In order to list or load a user Floppy into a VM, users should **upload**
the file to `VSKEY-STOR`_and then execute a ``sync`` command to make the
image file available in the ITS Private Cloud.

.. note:: Assuming you have already uploaded a file, the command
    ``vss-cli compute floppy personal sync`` should be executed.

Once you get a confirmation notification (email or message) Floppy images
should be visible through the CLI. To list just execute
``vss-cli compute floppy personal ls`` and the output should look as follows:

.. code-block:: bash

    vss-cli compute floppy personal ls

    path                                    name
    --------------------------------------  ----------
    [vssUser-xfers] jm/floppies/pvscsi.flp  pvscsi.flp

The process of mounting the image to a VM is the same:
first get the VM UUID and then
execute ``vss-cli compute vm set <name-or-uuid> floppy <unit> --image <path>``
as shown below:

.. code-block:: bash

    vss-cli compute vm set 501257e0-81f5-9c2a-84e5-e900212fef76 floppy 1 --image "[vssUser-xfers] jm/floppies/pvscsi.flp"

.. note:: Every time a new floppy image file has been added or removed from your `VSKEY-STOR`_ account,
     please run ``vss-cli compute floppy personal sync`` to update your account records.


.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
