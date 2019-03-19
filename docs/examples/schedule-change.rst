.. _SchedulingChange:

Scheduling Virtual Machine Changes
==================================

Scheduling changes provides flexibility to execute API actions at any given time.
For instance, scheduling to automatically upgrade VMware Tools, or to Shutdown VM and
then increase memory or CPU can be accomplished by just adding the schedule attribute
to any ``vss-cli compute set <uuid> <attribute>`` as described below:

.. code-block:: bash

    vss-cli compute vm set --help

    Usage: vss-cli compute vm set [OPTIONS] UUID_OR_NAME COMMAND [ARGS]...

      Set given virtual machine attribute such as cpu, memory, disk, network
      backing, cd, etc.

    Options:
      -s, --schedule TEXT  Schedule change in a given point in time based on format
                           YYYY-MM-DD HH:MM.
      --help               Show this message and exit.


This guide, will exemplify how to schedule the following actions:

* Shutdown/Power Off VM to run at ``2017-03-30 00:08``
* Add CPU to run at ``2017-03-30 00:10``
* Add Memory to run at ``2017-03-30 00:12``
* Power On VM to run at ``2017-03-30 00:14``


Virtual Machine UUID
--------------------

**Optional**. Get virtual machine ``UUID`` with ``vss-cli compute vm ls``
and apply any filtering if required:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the UUID, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name cranky
    uuid                                  name
    ------------------------------------  ---------------------
    50128577-2026-908a-7bb7-df5a34fea7bf  1610T-cranky_sinoussi

Once you got the target virtual machine ``UUID`` proceed to scheduling the changes.

Power Off
---------
Schedule the power off task by adding the ``--schedule`` option with the desired value
to the ``state off`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2017-03-30 00:08" cranky_sinoussi state off
    # or
    vss-cli compute vm set --schedule "2017-03-30 00:08" 50128577-2026-908a-7bb7-df5a34fea7bf state off

Add CPU
-------
Schedule the task to add cpu with the ``--schedule`` option with the desired value
to the ``cpu count <numCpu>`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2017-03-30 00:10" cranky_sinoussi cpu count 2
    # or
    vss-cli compute vm set --schedule "2017-03-30 00:10" 50128577-2026-908a-7bb7-df5a34fea7bf cpu count 2

Add Memory
----------
Schedule the task to add memory with the ``--schedule`` option with the desired value
to the ``memory size <numCpu>`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2017-03-30 00:10" cranky_sinoussi memory size 2
    # or
    vss-cli compute vm set --schedule "2017-03-30 00:10" 50128577-2026-908a-7bb7-df5a34fea7bf memory size 2


Power ON
--------
Schedule the power on task by adding the ``--schedule`` option with the desired value
to the ``state on`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2017-03-30 00:08" cranky_sinoussi state on
    # or
    vss-cli compute vm set --schedule "2017-03-30 00:08" 50128577-2026-908a-7bb7-df5a34fea7bf state on

For now, you just wait for the tasks to be executed in the requested date and time.