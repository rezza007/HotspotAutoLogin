import requests
from bs4 import BeautifulSoup
import hashlib
import os
import sys
import socket
from getpass import getpass

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def logIn() -> None:
  global loginURL
  global data
  try:
    if (requests.post(loginURL, data).status_code != 200):
      printError(r.status_code)
      exit()
  except:
    print('No network available')
    exit()

def logOut() -> None:
  global logOutURL
  try:
    if (requests.get(logOutURL).status_code != 200):
      printError(r.status_code)
      exit()
  except:
    print('No network available')
    exit()

def kickUser() -> None:
  global vpnReportLoginURL
  global vpnReportKillURL
  global data
  session = requests.session()
  r = session.post(vpnReportLoginURL, data)
  doc = BeautifulSoup(str(r.content), 'html.parser')
  try:
    data['ras_ip'] = doc.find('input', {'name' : 'ras_ip'})['value']
    data['unique_id_val'] = doc.find('input', {'name' : 'unique_id_val'})['value']
  except:
    print('Invalid ID or Password')
    exit()
  session.post(vpnReportKillURL, data)

def ping() -> int:
  global pingURL
  return os.system('ping -c 1 {} >/dev/null 2>&1'.format(pingURL))

def printError(errorCode : int) -> None:
  print('Connection failed, Code:{}'.format(errorCode))

def doLogOut() -> None:
  while ping() == 0:
    logOut()
  print("Disconnected!")

def doLogIn() -> None:
  logIn()
  while ping() != 0:
    kickUser()
    logIn()
  print("Connected!")

def init() -> None:
  global studentId
  global password
  global data
  global workingDir
  
  try: # Reading configurations
    with open(workingDir+'/.conf.txt', 'r', encoding='utf-8') as config:
      for line in config:
        if line.startswith('ID: '):
          studentId = line[len('ID: '):].rstrip('\n')
        if line.startswith('Password: '):
          password = line[len('Password: '):].rstrip('\n')

    data = {'username': studentId, 'normal_username': studentId,
          'password': hashlib.md5(password.encode("utf-8")).hexdigest(),
          'normal_password': password, 'kill_me': 1}
  except: # Configurations not found
    print("Configuration not found, config now? (y/n)")
    while True:
      answer = input()
      if answer == 'y' or answer == 'yes':
        doConfig()
        break
      if answer == 'n' or answer == 'no':
        break

def doConfig() -> None:
  global studentId
  global password
  global workingDir
  while True:
    studentId = input('Hotspot ID: ')
    password = getpass('Password: ')
    if type(studentId) == type(password) == str:
      config = open(workingDir+'/.conf.txt', 'w')
      config.write('ID: '+studentId+"\n")
      config.write('Password: '+password+"\n")
      print('Done!')
      break
    else:
      print('Invalid input')

# User variables
studentId = None
password = None

# These URLs may change in future
loginURL = 'https://hotspot.um.ac.ir/login'
logOutURL = 'http://hotspot.um.ac.ir/logout'
vpnReportLoginURL = 'https://vpn-report.um.ac.ir/IBSng/user/'
vpnReportKillURL = 'https://vpn-report.um.ac.ir/IBSng/user/home.php'
pingURL = 'google.com'

# All parameters needed
data = None
workingDir = os.path.dirname(os.path.realpath(__file__))

# Other parameters that forms send but they seem unnecessary
# data['lang'] = 'en'
# data['x'] = 24
# data['y']= 7
# data['dst'] = ''
# data['popup'] = True

if __name__ == "__main__":
  # Initialize needed arguments
  init()
  # Commands
  if len(sys.argv) > 1:
    if sys.argv[1] == '-c' or sys.argv[1] == '--connect': # Connect
      doLogIn()
    elif sys.argv[1] == '-cnf' or sys.argv[1] == '--config': # Configure
      doConfig()
    elif sys.argv[1] == '-d' or sys.argv[1] == '--disconnect': # Disconnect
      doLogOut()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help': # Help
      print(color.DARKCYAN+color.BOLD+'Ferdowsi University of Mashhad Hotspot Network Auto login.'+color.END+color.END)
      print(color.UNDERLINE+'Written by Reza Latifi'+color.END)
      print(color.GREEN+'    Default'+color.END+'\n\t    Connect to the Internet.')
      print(color.GREEN+'    (-c | --connect)'+color.END+'\n\t    Connect to the Internet.')
      print(color.GREEN+'    (-d | --disconnect)'+color.END+'\n\t    Disconnect from the Internet.')
      print(color.GREEN+'    (-cnf | --config)'+color.END+'\n\t    Configure user authentication.')
      print(color.GREEN+'    (-h | --help)'+color.END+'\n\t    User manual.')  
    else:
      print('Command not found try "--help"')
  else: # Default
    doLogIn()
