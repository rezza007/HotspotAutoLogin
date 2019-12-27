# HotspotAutoLogin

Ferdowsi University of Mashhad Internet hotspot login bot

Due to limitation in number of IPs permitted to connect to each student ID in FUM's hotspot system, it frequently happened to me that I wanted to switch devices and needed the internet on the other device but the process of disconnecting the first one, then connecting the second one felt agonizing, so I decided to write a bot in order to automate this process.

# Libraries used:
1. requests
2. BeautifulSoup

# How to use
1. put your sudent ID and password in "autoLogin.py" file.
2. to run the file using a short command, put this line in ~/.bashrc: alias FUMConnect="python3 /path/to/file/autoLogin.py"
3. type the following command each time you want to connect to the internet:
  FUMConnect
