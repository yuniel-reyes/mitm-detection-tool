from scapy.all import ARP, AsyncSniffer, conf

# Get adapters
def count_adapters():
    # Check available adapters
    adapters = []
    for interface, details in conf.ifaces.items():
        # print('There are: ' + f'{interface}')
        adapters.append(interface)
    return adapters


# Select adapters
def select_adapter():
    while True:
        adapters = count_adapters()
        # print(adapters)
        print('The availabe adapters are' + f'{adapters}')
        selection = input('To select the adapter, enter the corresponding number starting by 0: ')
        # print(adapters[1])
        match selection:
            case '0':
                return adapters[0]
            case '1':
                return adapters[1]
            case '2':
                return adapters[2]
            case '3':
                return adapters[3]
        

def arp_monitor(pkt):
    captured_packets = sniffer.stop_and_wait()
    # This line checks if the captured packet (pkt) is an ARP packet 
    # (ARP in pkt) and whether it has an ARP operation code (pkt[ARP].op) 
    # of 1 (who-has) or 2 (is-at).
    if ARP in captured_packets and pkt[ARP].op in (1,2): #who-has or is-at
        # If the condition is met (i.e., the packet is an 
        # ARP request or reply), this line uses Scapy's sprintf t
        # method to format and return a string containing the 
        # source hardware (MAC) address (%ARP.hwsrc%) and the 
        # source IP address (%ARP.psrc%) from the ARP packet.
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")


# Get current mac/ip paar
# def myfunction(): {}


# Get original mac/ip paar
# def myfunction(): {}


_iface = select_adapter()
sniffer = AsyncSniffer(iface=_iface, prn=arp_monitor, filter="arp", count=10)
sniffer.start()


# def start_sniff():
#     # print(_iface)
#     sniffer.start()

# start_sniff()
# select_adapter()



