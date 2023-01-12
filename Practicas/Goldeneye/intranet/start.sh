#!/bin/bash
route del default gw 10.5.36.254
route add default gw 10.5.36.1
# inicio el servidor apache
service apache2 start
/usr/sbin/sshd -D
