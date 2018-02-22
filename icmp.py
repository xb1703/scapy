#! /usr/bin/env python

from scapy.all import *


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

data = "kikoololping"
ping = Ether() / IP(dst='216.58.204.228') / ICMP() / data
ping.show()

###[ Fragments ]###
frags=fragment(ping,fragsize=8)
counter=1
for fragment in frags:
  print "Packet no#"+str(counter)
  print "==================================================="
  fragment.show() #displays each fragment
  counter+=1
  send(fragment)


#Recuperation de l'id du header IP
pingr = IP(dst="216.58.204.228")/ICMP()
resp = sr1(pingr)
resp.show2()

for elem in resp :
		id = elem[0].id

###[ IP ]###
version= 4
ihl= None
tos= 0x0
len= None
id= id+1
flags= ''
frag= 0
ttl= 64
proto='icmp'
chksum= None
src= '10.3.107.101'
dst= '216.58.204.228'

rep = srp1(ping)
rep.show()

###PARTIE 2###
# Frag3 cree des alertes pour les fragments de 8 bytes (en dessous de la valeur minimum de snort.conf: min_fragment_length 100)

