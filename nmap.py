import os
import sys
import subprocess
import threading
import hashlib


####### Nmap Function To add List of Active Hosts on the Network #######
def scan(ip, subnet):
    print("Starting All Host Discovery")
    output = subprocess.check_output("sudo nmap -n -sn " + str(ip) + "/" + str(subnet) +" -oG - | awk '/Up$/{print $2}'", shell=True).strip().decode('utf-8')
    with open("scanFiles/ipList.txt", 'w+') as file:
        file.write(output)


####### Nmap Function To add Detailed Scan #######
def nmapDetailedScan():
    print("Starting Detailed Host Scanning")
    try:
        with open("scanFiles/ipList.txt", "r") as file:
            for line in file:
                output = subprocess.check_output("sudo nmap -sC -sV -O -sS -T5 -p 1-65535 " + str(line), shell=True).strip().decode('utf-8')
                with open("scanFiles/nmapDetailScan.txt", "a") as file:
                    file.write(line.rstrip('\n') + "\n" + output[output.find('\n')+1:output.rfind('\n') - 1])
                    file.write("\n====================================================================================================== \n\n\n\n")
    except:
        pass

####### Nikto Function To add Port 80 and 443 Scan #######
def niktoScan():            
    print("Starting Nikto Scan on All Hosts")
    try:
        with open("scanFiles/ipList.txt", "r") as file:
            for line in file:
                output = subprocess.check_output("nikto -h " + str(line) + " -p 80,443 ", shell=True).strip().decode('utf-8')
                with open("nikto.txt", "a") as file:
                    file.write(line.rstrip('\n') + "\n" + output)
                    file.write("\n====================================================================================================== \n\n\n\n")
    except:
        pass


####### Nmap Function To check default Credentials #######
def nmapCredScan():
    print("Starting Nmap Credential Scan on All Hosts")
    try:        
        with open("scanFiles/ipList.txt", "r") as file:
            for line in file:
                output = subprocess.check_output("nmap --script http-default-accounts --script-args http-default-accounts.fingerprintfile=~/Recon_Stuff/http-default-accounts-fingerprints-nndefaccts.lua \
                                                -p 80  " + str(line), shell=True).strip().decode('utf-8')
                with open("scanFiles/credentials.txt", "a") as file:
                    file.write(line.rstrip('\n') + "\n" + output[output.find('\n')+1:output.rfind('\n') - 1])
                    file.write("\n====================================================================================================== \n\n\n\n")
    except:
        pass



####### For More Details visit #######
####### https://highon.coffee/blog/nmap-cheat-sheet/ #######
####### https://github.com/danielmiessler/SecLists  #######

if __name__ == "__main__":
    ip = str(sys.argv[1])                                  # Takes IP Address
    subnet = str(sys.argv[2])                              # Takes Subnet to Scan

    ####### Deletes if Nmap Verbose Scan results already exists #######
    if os.path.exists('scanFiles/nmapDetailScan.txt'):
        subprocess.call("rm scanFiles/nmapDetailScan.txt", shell=True)

    ####### Deletes if Nikto Scan results already exists #######
    if os.path.exists('scanFiles/nikto.txt'):
        subprocess.call("rm scanFiles/nikto.txt", shell=True)

    ####### Deletes if Credentials Scan results already exists #######
    if os.path.exists('scanFiles/credentials.txt'):
        subprocess.call("rm scanFiles/credentials.txt", shell=True)

    ####### Downloads the file for Default Credential scan using Nmap #######
    if not os.path.exists("http-default-accounts-fingerprints-nndefaccts.lua"):
        subprocess.call("wget https://github.com/nnposter/nndefaccts/blob/master/http-default-accounts-fingerprints-nndefaccts.lua", shell=True)

    scan(ip, subnet)
    #threading.Thread(target=nmapCredScan).start()
    threading.Thread(target=nmapDetailedScan).start()
    threading.Thread(target=niktoScan).start()
