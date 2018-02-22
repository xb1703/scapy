#!/usr/bin/env python

from scapy.all import *

# VARIABLES
src = '10.3.107.101'
dst = '10.3.107.74'

# SYN
packet = IP(src=src,dst=dst)/TCP(dport=range(1, 1024), flags="S") 
answered, unanswered = sr(packet, timeout=1)

#Snort module to detect this attack
#sfPortscan