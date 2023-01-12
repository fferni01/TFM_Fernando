#!/bin/bash

echo 1 > /proc/sys/net/ipv4/ip_forward

# 1.Configuración inicial de las comunicaciones a través de fw
iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

#iptables -A INPUT -i lo -j ACCEPT
#iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
#iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

#iptables -A FORWARD -i lo -j ACCEPT
#iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
#iptables -A FORWARD -p icmp --icmp-type echo-request -j ACCEPT

# 3. Comunicaciones desde la red interna
#iptables -A FORWARD -p icmp -m state --state RELATED,ESTABLISHED -j ACCEPT
#iptables -A FORWARD -p udp -m state --state RELATED,ESTABLISHED -j ACCEPT
#iptables -A FORWARD -p tcp -m state --state RELATED,ESTABLISHED -j ACCEPT

#iptables -A FORWARD -p icmp -i eth2 -o eth1 -s 10.5.2.20/24 -j ACCEPT
#iptables -A FORWARD -p udp -i eth2 -o eth1 -s 10.5.2.20/24 -j ACCEPT
#iptables -A FORWARD -p tcp -i eth2 -o eth1 -s 10.5.2.20/24 -j ACCEPT


#iptables -t nat -A POSTROUTING -o eth1 -s 10.5.2.0/24 -j SNAT --to 10.5.0.1

# 4. Comunicaciones en la DMZ
#iptables -A FORWARD -p tcp -i eth0 -o eth1 --dport 80 -d 10.5.2.20/24 -j ACCEPT
#iptables -A FORWARD -p tcp -i eth2 -o eth0 --dport 80 -d 10.5.1.20/24 -j ACCEPT
#iptables -A FORWARD -p tcp -i eth2 -o eth0 --dport 22 -s 10.5.2.20/24 -d 10.5.1.20/24 -j ACCEPT



/usr/sbin/sshd -D


