# HotspotAutoLogin

Ferdowsi University of Mashhad Internet hotspot login bot

Due to limitation in number of IPs permitted to connect to each student ID number in FUM's hotspot, it frequently happened to me that I want to switch devices and need internet on the other device and the process of disconnecting the first device and connection the second felt agonizing, so I decided to write a bot to automate this process.

# Libraries used:
1. requests
2. BeautifulSoup

# How to use
1. put your sudent ID and password in "autoLogin.py" file.
2. copy both bash file and python script to a common directory.
3. put this command in ~/.bashrc to have access to this file from anywhere : PATH=$PATH:/path/to/directory
4. in order to run the file using a short command, put this command in ~/.bashrc: alias FUMConnect="python3 autoLogin.py"
5. type following command in CLI each time you want to connect to the internet:
  FUMConnect
