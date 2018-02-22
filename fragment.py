#! /usr/bin/env python

from scapy.all import *
import random

payload = "A"*8+"B"*8+"C"*8+"D"*8+"E"*8+"F"*8+"G"*8+"H"*8
packet =IP(dst='216.58.204.228')/ICMP()/payload
 
frags=fragment(packet,fragsize=16)
# ordre aleatoire
random.shuffle(frags)
 
counter=1
for fragment in frags:
  print "Packet no#"+str(counter)
  print "==================================================="
  fragment.show() #displays each fragment
  counter+=1
  send(fragment)

## snort log
#10/18-14:48:33.578311  [**] [1:9999:0] ICMP Packet found [**] [Priority: 0] {ICMP} 10.3.107.101 -> 216.58.204.228
#10/18-14:48:33.578311  [**] [1:384:5] ICMP PING [**] [Classification: Misc activity] [Priority: 3] {ICMP} 10.3.107.101 -> 216.58.204.228
