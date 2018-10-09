import sys
import os
import subprocess


metasploit = False                                       # Change To True if Metasploit Not Installed
nikto = False                                            # Change To True if Nikto Not Installed
hydra = False                                            # Change To True if Hydra Not Installed
johnTheRipper = False                                    # Change To True if John The Ripper Not Installed
nmap = False                                             # Change To True if Nmap Not Installed
kaliGUI = False                                          # Change To True if you want to Install Kali GUI
ubuntuGUI = False                                        # Change To True if you want to Install Ubuntu GUI



####### This installs Metasploit on Ubuntu #######
if metasploit:
    subprocess.call("wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run \
                    && wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run.sha1 \
                    && echo $(cat metasploit-latest-linux-x64-installer.run.sha1)'  'metasploit-latest-linux-x64-installer.run > metasploit-latest-linux-x64-installer.run.sha1 \
                    && shasum -c metasploit-latest-linux-x64-installer.run.sha1 \
                    && chmod +x ./metasploit-latest-linux-x64-installer.run && sudo ./metasploit-latest-linux-x64-installer.run", shell=True)


####### This installs Nikto on Ubuntu #######
if nikto:
    subprocess.call("sudo apt-get -y install nikto", shell= True)


####### This installs Hydra on Ubuntu #######
if hydra:
    subprocess.call("sudo apt-get -y install hydra", shell=True)


####### This installs John The Ripper on Ubuntu #######
if johnTheRipper:
    subprocess.call("sudo apt-get -y install john", shell=True)


####### This installs Nmap on Ubuntu #######
if nmap:
    subprocess.call("sudo apt-get -y install nmap", shell=True)


####### This installs Kali Desktop GUI on Ubuntu #######
if kaliGUI:
    subprocess.call("sudo apt-get -y install kali-linux-full", shell=True)


####### This installs Actual Ubuntu Desktop GUI on Ubuntu #######
if ubuntuGUI:
    subprocess.call("sudo apt-get -y install ubuntu-desktop", shell=True)
