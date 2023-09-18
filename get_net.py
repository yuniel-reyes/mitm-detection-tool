from scapy.all import Ether, ARP, srp, conf

# The conf.ifaces is a dict where each key 
# is the interface name, and the corresponding value is a 
# dictionary containing interface details.
for interface, details in conf.ifaces.items():
        print("Inteface"':' f'{interface}'+'---'+f'{details.mac}'+':'+f'{details.ip}')


ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.0.110.0/24"), timeout=2)

