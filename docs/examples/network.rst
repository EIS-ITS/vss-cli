.. _Network:

Manage Networks and Interface Cards
===================================
Virtual networks are mapped to Virtual Distributed Port Groups
in order to simplify and scale the network layer. If you already
have access to one or many virtual networks in our environment you certainly
feel more familiar with this section, if not, you are probably going to use our
public network labeled **VL-1584-VSS-PUBLIC**, which is a
**DHCP enabled network** and has **no firewall** enabled due to its nature as
just being temporary and/or for testing.

We encourage all of our customers to have a custom network segment plumbed into
our environment and that can be done first by contacting
UofT Network Administration Tools and then providing the allocated segment
and VLAN information to the VSS Team.

Virtual Networks
----------------
Virtual networks are unique in our environment and have to be differentiated by
a unique identifier which in this case is the **moref** and stands for
**Managed Object Reference** provided by vCenter server.

The ``vss-cli compute net`` command lists and obtains information regarding
a specific virtual network you have permission on.


.. code-block:: bash

    vss-cli compute net --help

    Usage: vss-cli compute net [OPTIONS] COMMAND [ARGS]...

      List available virtual networks.

    Options:
      --help  Show this message and exit.

    Commands:
      get  Get given virtual network info.
      ls   list virtual networks.


List
~~~~
Run ``vss-cli compute net ls`` to list available networks. Filter list by
name using the option ``--filter-by/-f`` which is structured
``<field_name> <operator>,<value>`` and available operators are
**eq, ne, lt, le, gt, ge, like, in** as follows:

.. code-block:: bash

    vss-cli compute net ls -f name PUBLIC

    moref              name                description                  subnet          vlan_id    vms
    -----------------  ------------------  ---------------------------  --------------  ---------  -----
    dvportgroup-11052  VL-1584-VSS-PUBLIC  VSS Public network           142.1.216.0/23  1584       8



Info
~~~~
Network info is available by ``vss-cli compute net get <name-or-moref>``
and provides basic information of a given network:

.. code-block:: bash

    vss-cli compute net get dvportgroup-11052

    moref               : dvportgroup-11052
    name                : VL-1584-VSS-PUBLIC
    description         : VSS Public network
    subnet              : 142.1.216.0/23
    vlan_id             : 1584
    vms                 : 8
    ports               : 32
    admin               : Jose Manuel Lopez Lujan:000-0000-000:email@eis.utoronto.ca
    client              : EIS
    updated_on          : 2019-07-09 Tue 16:00:05 EDT


If you would like to get a list of your virtual machines available on a given
network, use the ``vss-cli compute net get <name-or-moref> vms`` command.
A list of ``uuid`` and `name` will  be provided.

.. code-block:: bash

    vss-cli compute net get dvportgroup-11052 vms

    uuid                                  name
    ------------------------------------  -----------------------
    501220a5-a091-1866-9741-664236067142  1611T-ecstatic_mccarthy
    501220a5-a091-6652-3215-123456548798  1701T-ecstatic_torvalds


Virtual Machine Network Adapters
--------------------------------

Virtual machine network interface cards backing is always a virtual network.
Virtual machine NICs can be manage by
``vss-cli compute vm <name-or-uuid> <set|get> nic <unit>``. Both `get` and
`set` commands have similar arguments `<unit>` and `set` has a few properties
to set as shown below:


.. code-block:: bash

    vss-cli compute vm get ecstatic_mccarthy nic --help

    Usage: vss-cli compute vm get nic [OPTIONS] [UNIT]

      Virtual machine network interface adapters configuration.

    Options:
      --help  Show this message and exit.


.. code-block:: bash

    Usage: vss-cli compute vm set nic [OPTIONS] COMMAND [ARGS]...

      Add, remove or update virtual machine network adapters

    Options:
      --help  Show this message and exit.

    Commands:
      mk  Create NIC unit
      rm  Remove NIC unit
      up  Update NIC unit


List
~~~~

Run ``vss-cli compute vm <name-or-uuid> nic`` to obtain a summary of your
virtual machineconfigured network interface controllers. If you specify
``unit``, the command will provide further information about the given
unit as follows:

.. code-block:: bash

    vss-cli compute vm get 501220a5-a091-1866-9741-664236067142 nic 1


    label               : Network adapter 1
    mac_address         : 00:50:56:00:00:00
    type                : vmxnet3
    network.name        : VL-1584-VSS-PUBLIC
    network.moref       : dvportgroup-11052
    connected           : True
    start_connected     : True


Update
~~~~~~

Update a given virtual machine network interface card
backing network by running
``vss-cli compute vm <name-or-uuid> nic up --network <name-or-moref> <unit>``
where ``uuid`` is the virtual machine UUID or name, ``unit`` is the nic labeled unit and
`moref` is the virtual network identifier or name.

For example, if a given nic needs to be updated to network
``dvportgroup-0000``, the command to use would be:

.. code-block:: bash

    vss-cli compute vm set 501220a5-a091-1866-9741-664236067142 nic up --network dvportgroup-0000 1

    # or

    vss-cli compute vm set TEST nic up --network VL-0000-NETWORK 1

New virtual machines by default are provisioned using the ``vmxnet3``
virtual adapter controller, designed to deliver high performance in
virtual machines, but there are rare cases, the operating system does
not include the ``vmxnet<2|3>`` drivers and the only way of getting
them is online, a virtual machine network adapter should be modified
with a more generic controller, such as ``e1000`` or ``e1000e``.
To do so, run
``vss-cli compute vm set <name-or-uuid> nic up --adapter <e1000|e1000e> 1``,
for example:

.. code-block:: bash

    vss-cli compute vm set 501220a5-a091-1866-9741-664236067142 nic up --adapter e1000e 1

After downloading **OpenVM Tools** which contain the drivers, change
back to the ``vmxnet3`` controller by performing the same bas operation
but replacing ``e1000e`` with ``vmxnet3`` as shown below:

.. code-block:: bash

    vss-cli compute vm set 501220a5-a091-1866-9741-664236067142 nic up --adapter vmxnet3 1


Network interface connection states can also be updated to either
``connect`` or ``disconnect`` given the requirements. To perform a
state change execute
``vss-cli compute vm set <name-or-uuid> nic up --state <connect|disconnect>``:

.. code-block:: bash

    vss-cli compute vm set 501220a5-a091-1866-9741-664236067142 nic up --state connect 1


Create
~~~~~~
Create a new virtual machine network adapter by using the sub command
``mk`` and providing the backing network and type separated by the
``=`` sign in the option. i.e. ``<moref-or-name>=<nic_type>``.

.. code-block:: bash

    Usage: vss-cli compute vm set nic mk [OPTIONS]

      Add network adapters specifying backing network and adapter type.

      vss-cli compute vm set <name-or-uuid> nic mk -n <moref-or-name>=<nic-type> -n <moref-or-name>

    Options:
      -n, --net TEXT  Network adapter <moref-or-name>=<nic-type>.  [required]
      --help          Show this message and exit.


.. note:: If no adapter is set, ``vmxnet3`` is used.


For example:

.. code-block:: bash

    vss-cli compute vm set 1909P-WEB nic mk -n dvportgroup-1083=vmxnet2 -n dvportgroup-1094


Remove
~~~~~~

Network adapter removal will ask for confirmation if flag ``-r/--rm``
is not provided. This is just as fail safe for mistakes that can happen
and since nic removal is a one way action, which disposes the MAC address.

The following example demonstrates how to remove a nic with a
confirmation prompt:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 nic rm 2

    Network adapter:        2
    Mac address:            00:50:56:92:4d:b8
    Network:                Quarantine (dvportgroup-11137)
    Connected:              False

    Are you sure you want to delete listed NICs [y/N]:

    Error: Cancelled by user.

If your answer is **N**, the command will exit as shown above.

To override nic removal confirmation prompt, just add ``-r/--rm``
flag as follows:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 nic rm --rm 2


