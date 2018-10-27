import sys
import os
import subprocess


metasploit = False                                       # Change To True if Metasploit Not Installed
armitage = False                                         # Change To True if you want to Install Armitage
nikto = False                                            # Change To True if Nikto Not Installed
hydra = False                                            # Change To True if Hydra Not Installed
johnTheRipper = False                                    # Change To True if John The Ripper Not Installed
nmap = False                                             # Change To True if Nmap Not Installed
kaliGUI = False                                          # Change To True if you want to Install Kali GUI
ubuntuGUI = False                                        # Change To True if you want to Install Ubuntu GUI
wireshark = False                                        # Change To True if you want to Install Wireshark
dirbuster = False                                        # Change To True if you want to Install Dirbuster
# WordList for dirb https://github.com/v0re/dirb/tree/master/wordlists
burp = False                                             # Change To True if you want to Burp Suite Free Version
#postman/editmycookie
#ophcrack
# Nessus -- https://www.tenable.com/downloads/nessus



####### This installs Metasploit on Ubuntu #######
if metasploit:
    print("\n ####### Installing METASPLOIT ####### \n")
    subprocess.call("wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run \
                    && wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run.sha1 \
                    && echo $(cat metasploit-latest-linux-x64-installer.run.sha1)'  'metasploit-latest-linux-x64-installer.run > metasploit-latest-linux-x64-installer.run.sha1 \
                    && shasum -c metasploit-latest-linux-x64-installer.run.sha1 \
                    && chmod +x ./metasploit-latest-linux-x64-installer.run && sudo ./metasploit-latest-linux-x64-installer.run", shell=True)


####### This installs Armitage on Ubuntu #######
if armitage:
    print("\n ####### Installing ARMITAGE ####### \n")
    subprocess.call("sudo apt-get -y install postgresql", shell=True)
    subprocess.call("wget -o armitage.tgz http://www.fastandeasyhacking.com/download/armitage150813.tgz \
                    && sudo tar xzvf armitage.tgz", shell=True)


####### This installs Nikto on Ubuntu #######
if nikto:
    print("\n ####### Installing NIKTO ####### \n")
    subprocess.call("sudo apt-get -y install nikto", shell= True)


####### This installs Hydra on Ubuntu #######
if hydra:
    print("\n ####### Installing HYDRA ####### \n")
    subprocess.call("sudo apt-get -y install hydra", shell=True)


####### This installs John The Ripper on Ubuntu #######
if johnTheRipper:
    print("\n ####### Installing JOHN THE RIPPER ####### \n")
    subprocess.call("sudo apt-get -y install john", shell=True)


####### This installs Nmap on Ubuntu #######
if nmap:
    print("\n ####### Installing NMAP ####### \n")
    subprocess.call("sudo apt-get -y install nmap", shell=True)


####### This installs Kali Desktop GUI on Ubuntu #######
if kaliGUI:
    print("\n ####### Installing KALI LINUX DESKTOP ####### \n")
    subprocess.call("sudo apt-get -y install kali-linux-full", shell=True)


####### This installs Actual Ubuntu Desktop GUI on Ubuntu #######
if ubuntuGUI:
    print("\n ####### Installing UBUNTU DESKTOP ####### \n")
    subprocess.call("sudo apt-get -y install ubuntu-desktop", shell=True)


####### This installs Wireshark on Ubuntu #######
if wireshark:
    print("\n ####### Installing WIRESHARK ####### \n")
    subprocess.call("sudo apt-get -y install wireshark", shell=True)



'''
####### This installs Dirbuster on Ubuntu #######
if dirbuster:
    print("\n ####### Installing DIRBUSTER ####### \n")
    subprocess.call("wget -o dirbuster.tar.bz2 https://netcologne.dl.sourceforge.net/project/dirbuster/DirBuster\%20\%28jar\%20\%2B\%20\lists%29/0.12/DirBuster-0.12.tar.bz2 \
                    && sudo tar xzvf armitage.tgz", shell=True)
    subprocess.call("sudo apt-get -y install wireshark", shell=True)



####### This installs BurpSuite Free on Ubuntu #######
if burp:
    print("\n ####### Installing BURP SUITE ####### \n")
    subprocess.call("sudo apt-get -y install openjdk-8-jre", shell=True)
    subprocess.call("wget https://portswigger.net/burp/releases/download?product=community&version=1.7.36&type=linux \
                    && ")
'''