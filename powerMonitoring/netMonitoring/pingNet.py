import sys
from termcolor import colored, cprint

#print colored('hello', 'red'), colored('world', 'green')

import os

router = '192.168.0.1'
lcom   = '192.168.0.105'
ubnt   = '192.168.0.77'
seccam = '192.168.0.88'
HPprint= '192.168.0.112'
#nanaph = '192.168.0.115' #these won't ping...
#myphon = '192.168.0.101' #these won't ping...

router_response = os.system("ping -c 1 " + router)
lcom_response   = os.system("ping -c 1 " + lcom)
ubnt_response   = os.system("ping -c 1 " + ubnt)
seccam_response = os.system("ping -c 1 " + seccam)
HPprint_response= os.system("ping -c 1 " + HPprint)
#nanaph_response = os.system("ping -c 1 " + nanaph)
#myphon_response = os.system("ping -c 1 " + myphon)

#and then check the response...
if router_response == 0:
  print colored('Router is up', 'green')
else:
  print colored('router is down','red')

if lcom_response == 0:
  print colored('DoomAlpha is up', 'green')
else:
  print colored('DoomAlpha is down', 'red')

if ubnt_response == 0:
  print colored('Nana UBNT','green')
else:
  print colored('Nana UBNT','red')

if seccam_response == 0:
  print colored('Cameras are up','green')
else:
  print colored('Cameras are down','red')
