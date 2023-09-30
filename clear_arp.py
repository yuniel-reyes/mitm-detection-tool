import get_arptable
import subprocess
from colorama import Fore
import dots

def _clear_arp():
    # 
    get_arptable.current_table()
    with open('arp-table.txt', 'r') as lastest_table:
        read_table = lastest_table.readlines()
        for eachMach in read_table:
            # print(eachMach.rsplit(',')[0])
            subprocess.run(['sudo', 'arp', '-d', eachMach.rsplit(',')[0]])
            subprocess.run(['sudo', 'ip', '-s', '-s', 'neigh', 'flush', 'all'])

    print(Fore.LIGHTBLUE_EX + 'Clearing Arp table' + Fore.RESET)
    dots.print_dots()
    print(Fore.LIGHTBLUE_EX + 'Arp table was cleared' + Fore.RESET)