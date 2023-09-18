import scapy.all as scapy

def scan(subnet):
    i = 0
    prev = 0
    while True:
        i+=1
        ans, unans = scapy.arping(subnet, timeout=i, verbose=0)
        num_responses = len(ans)
        print(ans)
        print("Got {} responses in {} seconds".format(num_responses, i))
        if num_responses > prev:
            prev = num_responses
        else:
            break
    print("You should set your timeout to {} seconds".format(i-1))

scan("10.0.110.0/24")



# scapy.layers.l2.arping(net: str, timeout: int = 2, cache: int = 0, verbose: int | None = None, **kargs: Any) \
#     Tuple[ARPingResult, PacketList]