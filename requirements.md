# MITM Defender

**TODO**
1. Create venv (done)

 
2. Installing scrapy (done)
A tool designed to detect Man-in-the-Middle (MITM) attacks should possess several 
key characteristics to effectively identify and mitigate such threats:

I. **Detection**
1. **Real-Time Monitoring**: 
The tool should be capable of continuously monitoring ARP network 
traffic in real-time to detect any sudden changes or anomalies. 
 a. Tool should be able first of detect multiple adapters
  - User whould select the adapter to monitor: eth0, eth1...
  - Script should get ARP packets been exchanged
  - Script should get original mac/ip paar and compare with current mac/ip
  - Script should return You are been hacked / Everything is ok!
  - If a tool like X is being used to perform a ARP poisoning, even if your ARP table is static, the detector will show 'you are being hacked' because the original mac is being compared with mac in packet part of the broadcast. 
  To avoid that: 
      If ip of packet and current mac == to ip and mac in table
        *Hacked*
      Else: ARP attack, but coverered 

II. **Defense**:
  - Static ARP Tables 
