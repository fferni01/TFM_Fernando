Http
-t is for the target, some domain or ip-address.
-p is for port Defaults to 80.
-r is for the threads, how many threads we want to run for this attack.
-T adds the Tor function which provides security, as well, as providing a new identity in case the site is programmed to ban IP addresses which leave an open connection for "x" amount of time. Tor'shammer's method of combining this is clever and effective, making it the powerful tool it is. However, Tor'shammer is only effective to apache servers which do not run nginx.

python torshammer.py -t 10.5.6.20 -p 80 -r 5000