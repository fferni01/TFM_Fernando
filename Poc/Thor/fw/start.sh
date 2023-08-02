#!/bin/bash

echo 1 > /proc/sys/net/ipv4/ip_forward

# 1.Configuración inicial de las comunicaciones a través de fw
iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

/usr/sbin/sshd -D


