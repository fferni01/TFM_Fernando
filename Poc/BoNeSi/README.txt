Ip addres de las maquinas ->
- fw: 
ip address:
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000      
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
204: eth2@if205: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:05:02:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.2.1/24 brd 10.5.2.255 scope global eth2
       valid_lft forever preferred_lft forever
206: eth1@if207: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:05:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.0.1/24 brd 10.5.0.255 scope global eth1
       valid_lft forever preferred_lft forever
208: eth0@if209: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:05:01:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.1.1/24 brd 10.5.1.255 scope global eth0
       valid_lft forever preferred_lft forever

ip route:
default via 10.5.1.254 dev eth0
10.5.0.0/24 dev eth1 proto kernel scope link src 10.5.0.1 
10.5.1.0/24 dev eth0 proto kernel scope link src 10.5.1.1 
10.5.2.0/24 dev eth2 proto kernel scope link src 10.5.2.1

- Int1:
ip address:
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
216: eth0@if217: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:0a:05:02:14 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.2.20/24 brd 10.5.2.255 scope global eth0
       valid_lft forever preferred_lft forever

ip route:

default via 10.5.2.1 dev eth0 
10.5.2.0/24 dev eth0 proto kernel scope link src 10.5.2.20 

- Int2:
ip address:
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
212: eth0@if213: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:0a:05:02:15 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.2.21/24 brd 10.5.2.255 scope global eth0
       valid_lft forever preferred_lft forever

ip route:
default via 10.5.2.1 dev eth0
10.5.2.0/24 dev eth0 proto kernel scope link src 10.5.2.21 

- Ext:
ip address:
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
210: eth0@if211: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:0a:05:00:14 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.0.20/24 brd 10.5.0.255 scope global eth0
       valid_lft forever preferred_lft forever

ip route:
default via 10.5.0.1 dev eth0
10.5.0.0/24 dev eth0 proto kernel scope link src 10.5.0.20 

- DMZ:
ip address: 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000      
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
214: eth0@if215: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:05:01:14 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.1.20/24 brd 10.5.1.255 scope global eth0
       valid_lft forever preferred_lft forever

ip route:
default via 10.5.1.1 dev eth0
10.5.1.0/24 dev eth0 proto kernel scope link src 10.5.1.20 
