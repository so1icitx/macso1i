# **macso1i**  
A simple MAC address changer for Linux, written in Python.

![Arch Linux](https://img.shields.io/badge/Arch-Linux-blue?logo=arch-linux)  
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features  
- 🛠️ Change MAC address for any network interface.  
- 🔍 Show available network interfaces.  

---

## 📚 Installation  
```bash
git clone https://github.com/trxycs/macso1i.git
cd macso1i
```


## ⚠️ Requirements  
- Python 3  
- `ifconfig` (usually part of the `net-tools` package)  
- Root privileges (`sudo`) 
---


## 🚀 Usage  
### Change the MAC address:  
```bash
sudo python3 mac_changer.py -i wlan0 --mac 00:11:22:33:44:55
```

### View available network interfaces (e.g., wlan0, enp4s0, etc.):  
```bash
python3 mac_changer.py --show
```

---
### Shows commands and how to use the mac changer:
```bash
python3 mac_changer.py -h
```
 

---

## 📝 License  
This project is licensed under the **MIT License**.  

---
