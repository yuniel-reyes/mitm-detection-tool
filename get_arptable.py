# from arp_table import get_arp_table
from python_arptable import get_arp_table
# Get ARP table
def current_table():

    # Rewrite the arp-table eachtime 
    with open('arp-table.txt', 'w') as table:
        arp_table = get_arp_table()
        for eachMach in arp_table[1:]:
            table.write(f'{eachMach["IP address"]},' f'{eachMach["HW address"]}''\n')                



