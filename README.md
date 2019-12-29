# HotspotAutoLogin

Ferdowsi University of Mashhad Hotspot network auto login

Due to limitation in number of IPs permitted to connect to each student ID in FUM's hotspot system, it frequently happened to me that I wanted to switch devices and needed the internet on the other device but the process of disconnecting the first one, then connecting the second one felt agonizing, so I decided to write a bot in order to automate this process.

# Libraries used:
1. requests
2. BeautifulSoup

# What does it do?
Connects or disconnects from Hotspot network.

# Help
 Works using CLI commands, to show complete list of supported commands use '-h' or '--help' command.
 
# How to use
1. Install libraries.
1. Config bot, using '-cnf' or '--config' command.
2. To run the file using a short command, put this line in ~/.bashrc file: alias HOTSPOT="python3 /path/to/file/autoLogin.py"
3. Type the following command each time you want to connect to the Internet: HOTSPOT
  
  ![Help command output](https://github.com/rezza007/HotspotAutoLogin/screenshot.png)
