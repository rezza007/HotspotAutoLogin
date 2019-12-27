# HotspotAutoLogin

Ferdowsi University of Mashhad Internet hotspot login bot

Due to limitation in number of IPs permitted to connect to each student ID number in FUM's hotspot, it frequently happened to me that I want to switch devices and need internet on the other device and the process of disconnecting the first device and connection the second felt agonizing, so I decided to write a bot to automate this process.

# Libraries used:
1. requests
2. BeautifulSoup

# How to use
1. copy both bash file and python script to a common directory.
2. add the directory to a PATH : PATH=$PATH:/path/to/directory
3. put this command in ~/.bashrc : alias FUMConnect="./connect"
4. type following command in CLI each time you want to connect to the internet:
  FUMConnect
