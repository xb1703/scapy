#! /usr/bin/env python

from scapy.all import *

data = "kikoololping"
ping = Ether() / IP(dst='216.58.204.228') / ICMP() / data
ping.show()
###[ Ethernet ]###
dst='64:00:6A:74:EE:69'
src='08:00:27:56:b8:73'
type=0x800
###[ IP ]###
version= 4
ihl= None
tos= 0x0
len= None
id= 1
flags= ''
frag= 0
ttl= 64
proto='icmp'
chksum= None
src= '10.3.107.101'
dst= '216.58.204.228'


###[ ICMP ]###
type='echo-request'
code= 0
chksum= None
id= 0x0
seq= 0x0

rep = srp1(ping)
rep.show()
#rep = sr1(IP(dst='216.58.204.228') / ICMP())