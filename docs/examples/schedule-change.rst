.. _SchedulingChange:

Scheduling Virtual Machine Changes
==================================

Scheduling changes provides flexibility to execute API actions at any
given time. For instance, scheduling to automatically upgrade VMware
Tools, or to Shutdown VM and then increase memory or CPU can be
accomplished by just adding the schedule attribute to any
``vss-cli compute set <moref> <attribute>`` as described below:

.. code-block:: bash

    vss-cli compute vm set --help

      Manage virtual machine attributes such as cpu, memory, disk, network
      backing, cd, etc..

    Options:
      -s, --schedule [%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M]
                                      Schedule change in a given point in time
                                      based on format YYYY-MM-DD HH:MM.
      -u, --user-meta TEXT            User metadata in key=value format. These
                                      tags are stored in the request.
      --help                          Show this message and exit.


This guide exemplifies the scheduling process for the following actions:

* Shutdown/Power Off VM to run at ``2019-04-06 00:08``: **state**
* Add CPU to run at ``2019-04-06 00:10``: **cpu count**
* Update boot delay at ``2019-04-06 00:11``: **boot-delay**
* Add Memory to run at ``2019-04-06 00:12``: **memory size**
* Power On VM to run at ``2019-04-06 00:15``: **state**
* Reschedule the **memory size** change.
* Cancel **boot-delay** change.

Virtual Machine ID
------------------

**Optional**. Get virtual machine ``MOREF`` or ``UUID``
with ``vss-cli compute vm ls`` and apply any filtering if required:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the ``MOREF``, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name=Front

    moref    name             folder.path                  cpu_count    memory_gb  power_state    ip_address
    -------  ---------------  -------------------------  -----------  -----------  -------------  ------------
    vm-2183  2004T-Frontend2  VSS > Development > Dev02            2            2  poweredOff


Once you got the target virtual machine ``MOREF`` proceed to scheduling
the changes.

Power Off
---------
Schedule the power off task by adding the ``--schedule`` option with
the desired value to the ``state off`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2019-04-06 00:08" cranky_sinoussi state off
    # or
    vss-cli compute vm set --schedule "2019-04-06 00:08" vm-2183 state off

Add CPU
-------
Schedule the task to add cpu with the ``--schedule`` option with the
desired value to the ``cpu count <numCpu>`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2019-04-06 00:10" Frontend2 cpu count 2
    # or
    vss-cli compute vm set --schedule "2019-04-06 00:10" vm-2183 cpu count 2

Update boot delay
-----------------
Schedule the task to update ``boot-delay`` with the ``--schedule``
option and the desired value to the ``boot-delay <milliseconds>``
command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2019-04-06 00:11" cranky_sinoussi boot-delay 10000
    # or
    vss-cli compute vm set --schedule "2019-04-06 00:11" vm-2183 boot-delay 10000

Add Memory
----------
Schedule the task to add memory with the ``--schedule`` option
with the desired value to the ``memory size <numCpu>`` command
as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2019-04-06 00:12" cranky_sinoussi memory size 2
    # or
    vss-cli compute vm set --schedule "2019-04-06 00:12" vm-2183 memory size 2


Power ON
--------
Schedule the power on task by adding the ``--schedule`` option
with the desired value to the ``state on`` command as follows:

.. code-block:: bash

    vss-cli compute vm set --schedule "2019-04-06 00:15" cranky_sinoussi state on
    # or
    vss-cli compute vm set --schedule "2019-04-06 00:15" vm-2183 state on


Reschedule Memory Change
------------------------
To reschedule a scheduled update, use the command
``vss-cli request change set {request_id} schedule`` with
the option ``-d/--date-time``:

.. code-block:: bash

    Usage: vss-cli request change set schedule [OPTIONS]

    Options:
      -c, --cancel                    Cancel scheduling
      -d, --date-time [%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M]
                                      Update datetime YYYY-MM-DD HH:MM.
      --help                          Show this message and exit.


Assuming you got change request ``24542`` as a result of submitting the
memory change, the command to update the scheduled datetime should be something like:

.. code-block:: bash

    vss-cli request change set 24542 schedule --date-time "2019-04-06T00:13:00"

Cancel Boot Delay Change
------------------------
To cancel a scheduled update, use the command
``vss-cli request change set {request_id} schedule`` with the option
``-c/--cancel``:

.. code-block:: bash

    Usage: vss-cli request change set schedule [OPTIONS]

    Options:
      -c, --cancel                    Cancel scheduling
      -d, --date-time [%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M]
                                      Update datetime YYYY-MM-DD HH:MM.
      --help                          Show this message and exit.

Assuming you got change request ``24545`` as a result of submitting the
memory change, the command to update the scheduled datetime should be something like:

.. code-block:: bash

    vss-cli request change set 24545 schedule --cancel


For now, you just wait for the tasks to be executed in the requested
date and time.
