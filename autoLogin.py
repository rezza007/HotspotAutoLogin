import requests
from bs4 import BeautifulSoup
import hashlib
import os
import sys
import socket

def logIn(data : dict):
  global hotspotURL
  if (requests.post(hotspotURL, data).status_code != 200):
    printError(r.status_code)
    exit()

def kickUser(data : dict):
  global vpnReportLoginURL
  global vpnReportKillURL
  session = requests.session()
  r = session.post(vpnReportLoginURL, data)
  doc = BeautifulSoup(str(r.content), 'html.parser')
  data['ras_ip'] = doc.find('input', {'name' : 'ras_ip'})['value']
  data['unique_id_val'] = doc.find('input', {'name' : 'unique_id_val'})['value']
  session.post(vpnReportKillURL, data)

def ping():
  global pingURL
  return os.system("ping -c 1 {}".format(pingURL))

def printError(errorCode : int):
  print("Connection failed, Code:{}".format(errorCode))


# User dependent variables
studentId = 1234567890
password = 'password'

# These URLs may change in future
hotspotURL = 'https://hotspot.um.ac.ir/login'
vpnReportLoginURL = 'https://vpn-report.um.ac.ir/IBSng/user/'
vpnReportKillURL = 'https://vpn-report.um.ac.ir/IBSng/user/home.php'
pingURL = 'google.com'

# All parameters needed
data = {'username': studentId, 'normal_username': studentId,
        'password': hashlib.md5('ramzenet'.encode("utf-8")).hexdigest(),
        'normal_password': password, 'kill_me': 1}

# Other parameters that forms send but they seem unnecessary
# data['lang'] = 'en'
# data['x'] = 24
# data['y']= 7
# data['dst'] = ''
# data['popup'] = True

logIn(data)
while (ping() != 0):
  kickUser(data)
  logIn(data)
print("Connected!")
