#!/bin/bash

apt-get update

apt-get install build-essential libssl-dev yasm libgmp-dev libpcap-dev libnss3-dev libkrb5-dev pkg-config libopenmpi-dev openmpi-bin zlib1g-dev libbz2-dev

apt-get install flex cmake bison git

cd /opt
git clone https://github.com/teeshop/rexgen.git
cd rexgen
./install.sh
ldconfig

cd /opt
git clone https://github.com/m8r0wn/nullinux
cd nullinux
chmod +x setup.sh
./setup.sh

cd /opt
git clone https://github.com/SecureAuthCorp/impacket
cd impacket
pip install .

cd /opt
git clone https://github.com/magnumripper/JohnTheRipper
cd JohnTheRipper/src/
./configure --enable-mpi
make -s clean && make -sj4
cd ../run
./john --test