from scapy.all import *

while 1:
	frame = Ether( \
	src=RandMAC(), \
	dst='02:00:99:63:09:02') \
	/IP(src="10.10.111.0",dst="255.255.255.255")\
	/UDP(sport=68,dport=67)\
	/BOOTP(chaddr=RandString(12,'abcd1234efgh'))\
	/DHCP(options=[("message-type","discover"),"end"] \
	)
