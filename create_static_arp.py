import subprocess
import re
import get_arptable
from getmac import get_mac_address
from colorama import Fore
import dots

# Get current ARP entries after pinging


def static_arp():
    get_arptable.current_table()
    #   Read every ip if it has a corresponding mac
    with open("arp-table.txt", 'r') as f:
        ips_and_macs = f.readlines()
        for eachLine in ips_and_macs:
    
            # Define the regular expression pattern
            ip_num_req = r"(\d+\.\d+\.\d+\.\d+)"
            mac_num_req = r"(\b[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}\b)"
            # Get the match 
            ip_num_resl = re.search(ip_num_req, eachLine)
            mac_num_resl = re.search(mac_num_req, eachLine)

            if ip_num_resl and mac_num_resl:
                # Get the ip and the mac - it returns a tuple
                this_mac = get_mac_address(ip=ip_num_resl.group(), network_request=True)
                resull = subprocess.run(['arp', '-s', ip_num_resl.groups()[0], str(this_mac)], stdout=None)
        dots.print_dots()
        print(Fore.CYAN + "[*]The static ARP table was created." + Fore.RESET)
