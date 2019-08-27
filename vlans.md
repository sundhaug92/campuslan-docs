# VLANs
VLANs, or Virtual Local Area Networks, are a way to logically segment a network. When using VLANs, a switch-port is either **tagged** or **untagged**. Traffic on an untagged port does not include a tag telling the ends what VLAN it belongs to, useful when connecting to end-user devices, or devices that don't understand VLANs. Traffic on a tagged port *does* have a tag telling the ends what VLAN it belongs to, useful when connecting infrastructure-gear (switches, routers, ...), or say a hypervisor host (so you can have management and different VMs on separate VLANs), to the network.

Note: Remember to protect against [VLAN hopping](https://en.wikipedia.org/wiki/VLAN_hopping)