#!/home/kali/env python
from scapy.all import srp, Ether, ARP, conf
import time
import scapy.all as scapy


# Set the duration in seconds
duration = 100  # Change this to the desired duration

# Get the start time
start_time = time.time()


# Get subnet on the link layer
sub_net = conf.ifaces

# The conf.ifaces is a dict where each key 
# is the interface name, and the corresponding value is a 
# dictionary containing interface details.
# Get ip according to adapater
def get_net():
    for interface, details in conf.ifaces.items():
        if interface == 'eth2':
            return details.ip[:-2]+'.0/24'

# Get active host on subnet
def get_active_host():
    subnet  = get_net()
    # The result variable will contain the list of responses. Each element 
    # in the list is a tuple with two items: the IP address and the corresponding MAC address (if available).
    ans, unans = scapy.arping(subnet) #timeout=3, verbose=0
    print(ans)


# Run the function for the specified duration
while time.time() - start_time < duration:
    get_active_host()






