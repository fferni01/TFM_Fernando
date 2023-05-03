#
#
# Copyright (c) 2020 Adrian Campazas Vega, Ignacio Samuel Crespo Martinez, Angel Manuel Guerrero Higueras.
#
# This file is part of DOROTHEA 
#
# DOROTHEA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOROTHEA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

#from celery.result import ResultSet
from .tasks_DDOS import torshammer
from celery.result import ResultSet
from .end_attack.end_attack import end_attack
import time
import random

def start_attack():
    global r
    r = ResultSet([])
    a= True
    
    ip=["140.30.20.5"]
    #ips = randomize_ip()
    #ports = [80, 443, 8080]
    port = 80

    for i in range(10):
        ataque = torshammer.delay(ip, port) 
        r.add(ataque)
        time.sleep(10)
        
    
def end_attacks():
    global r
    r.join()
    if r.ready() == True:
        end_attack()

if __name__ == '__main__':
    start_attack()
    end_attacks()
