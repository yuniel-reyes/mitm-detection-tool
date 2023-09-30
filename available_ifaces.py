from scapy.all import conf
import scapy.all as scapy
import dots
from colorama import Fore

# The conf.ifaces is a dict where each key 
# is the interface name, and the corresponding value is a 
# dictionary containing interface details.
# Get ip according to adapater
def get_active_ifaces():
    print(Fore.GREEN + 'Detecting interfaces' + Fore.RESET)

    dots.print_dots()
    adapters_list = []
    for interface, details in conf.ifaces.items():
        # Check if there are active hosts on that iface
        if get_active_hosts(details.ip[:-2]+'.0/24'):
            adapters_list.append(interface)
    return adapters_list


# Get active host on subnet
def get_active_hosts(subnet):

    # The result variable will contain the list of responses. Each element 
    # in the list is a tuple with two items: the 
    # IP address and the corresponding MAC address (if available).
    ans, unans = scapy.arping(subnet, verbose=0) #timeout=3, verbose=0 a
    if len(ans) != 0:
        return True
    





