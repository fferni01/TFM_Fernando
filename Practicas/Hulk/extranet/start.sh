#!/bin/bash
route del default gw 10.5.3.254
route add default gw 10.5.3.1

# inicio el servidor apache
# service apache2 start

/usr/sbin/sshd -D
