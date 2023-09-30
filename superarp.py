from scapy.all import ARP, sniff, conf, srp, Ether
from colorama import Fore
import get_arptable
import create_static_arp
import available_ifaces
import logo
import dots
from clear_arp import _clear_arp


#######################################################
# DETECTION

# Select adapter
def select_adapter():
    # Get adapters
    adapters = available_ifaces.get_active_ifaces()

    while True:       
        # print(adapters)
        print('The availabe interfaces are:')
        for eachAdp in adapters:
            print(Fore.LIGHTRED_EX + "Interfaces:" f'{eachAdp}' + Fore.RESET)
        selection = input('Select interface with name: ')
        while selection not in adapters:
            selection = input(Fore.LIGHTRED_EX + "[*] Not such device! Select interface: " + Fore.RESET)
        return selection
       

# Do a ARP request with Source IP Adress from sniffed Packet:pdst=psrc
def get_original_mac(packet_ip): 
    # Create an ARP (Address Resolution Protocol) request 
    request_arp = ARP(pdst=packet_ip)
    # Create an Ethernet frame with a destination MAC address of "ff:ff:ff:ff:ff:ff". 
    _broadcast = Ether(dst = "ff:ff:ff:ff:ff:ff")
    # Combining ARP Request and Ethernet Frame
    arp_rq_broadcast = _broadcast / request_arp
    # Send packet
    srp_response = srp(arp_rq_broadcast, timeout=5, verbose=False)[0]
    # Return mac associated to IP
    if srp_response:
        return srp_response[0][1].hwsrc
    else:
        get_original_mac(packet_ip)


def arp_monitor(pkt):

    # Check if packet contains ARP code is at (reply packet)
    if ARP in pkt and pkt[ARP].op == 2: 
        # Get current sniffed packet mac
        current_mac_packet = pkt[ARP].hwsrc 
        # Call and get original mac
        original_mac = get_original_mac(pkt[ARP].psrc)
        # Check lastest ARP table in cache
        get_arptable.current_table()

        # Lets compare
        ip_and_mac = False
        with open("arp-table.txt", "r") as table:
            arp_entries = table.readlines()
            # Iterate over the returned list
            for eachMach in arp_entries:
                mac_a_ip_list = eachMach.rsplit(',')
                mac_a_ip_list1 = mac_a_ip_list[1].replace('\n', '')
                mac_a_ip_list[1] = mac_a_ip_list1
                if (str(pkt[ARP].psrc) == mac_a_ip_list[0]) and (str(current_mac_packet) == mac_a_ip_list[1]):
                    ip_and_mac = True

        # This will mean your ARP table is poisoned, meaning you are vulnerable to MITM
        if (original_mac != current_mac_packet) and (ip_and_mac == True):
            print(Fore.LIGHTRED_EX + "[*]ALERT!! You have been hacked!" + Fore.RESET)
            
        # This will mean you are under attack
        elif (original_mac != current_mac_packet) and (ip_and_mac == False):
            print(Fore.LIGHTRED_EX + "You are under attack!" + Fore.RESET)
                
    
# Start capturing packets
def start_watcher():
    # Select the adapter to sniff on
    _iface = select_adapter()
    print(Fore.LIGHTRED_EX + "Watcher is running" + Fore.RESET)
    dots.print_dots()
    # The store parameter is set to 0 so that the sniff() 
    # function will not store anything (as it would do otherwise) and thus can run forever
    packets = sniff(iface=_iface, prn=arp_monitor, filter="arp", store=0)


#####################################################################
# DEFENSE
# Create ARP static cache table
# Get all machines in the interface
# Every device on the WAN will be pinged which will cause the arp
# table to be updated with the MAC addresses for all the devices.



def start_defense():
    selection = select_adapter()
    create_static_arp.static_arp()
            

###############################################
# START PROGRAM
def start_program():
    logo.dense_ascii_suparp()
    print(Fore.LIGHTRED_EX + "[1] Watcher mode" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "[2] Defense mode" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "[3] Clear the ARP table" + Fore.RESET)
    print('')
    selection = input("Select: ")
    match selection:
        case '1':
            start_watcher()
        case '2':
            start_defense()
        case '3':
            _clear_arp()



start_program()


