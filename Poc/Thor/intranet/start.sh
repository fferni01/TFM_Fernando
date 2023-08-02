#!/bin/bash
route del default gw 10.5.6.254
route add default gw 10.5.6.1
# inicio el servidor apache
httpd-foreground
/usr/sbin/sshd -D


