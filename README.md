# macso1i 
A simple MAC address changer for Linux, written in Python.

![Demo](https://img.shields.io/badge/Arch-Linux-blue?logo=arch-linux) 
![License](https://img.shields.io/badge/License-MIT-green)

## Features ✨
- Change MAC address for any network interface.
- Show available interfaces.


## Installation 📦
'''bash
git clone https://github.com/trxycs/macso1i.git
cd macso1i
## Usage :accessibility:
'''bash
To change the MAC address:
sudo ./mac_changer.py -i wlan0 --mac 00:11:22:33:44:55
To view available interfaces(wlan0, enp4s0, etc):
./mac_changer.py --show



