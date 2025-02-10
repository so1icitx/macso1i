#!/usr/bin/env python3
import subprocess
from mac_art import logo
import optparse

def change_mac(choice_mac, mac_add):
    try:
        subprocess.call(["sudo", "ifconfig", choice_mac, "down"])
        subprocess.call(["sudo", "ifconfig", choice_mac, "hw", "ether", mac_add])
        print(f"[+] Changing MAC address for {choice_mac} to {mac_add}")
        subprocess.call(["sudo", "ifconfig", choice_mac, "up"])
        print("[+] MAC address changed successfully.")

        end_result = input("Do you want to see the end results? (yes/no): ").lower()
        if end_result == "yes":
            subprocess.call(["sudo", "ifconfig", choice_mac])
        elif end_result == "no":
            print("[+] Thanks for using MAC Changer.")
        else:
            print("[!] Invalid input. Exiting.")

    except Exception as e:
        print(f"[!] Error: {e}")

def start():
    print(logo)
    parser = optparse.OptionParser(usage="Usage: %prog -i INTERFACE --mac MAC_ADDRESS\nExample: %prog -i wlan0 --mac 00:11:22:33:44:55",description="A tool to change your MAC address for network privacy.")
    
    parser.add_option("-i", dest="interface", help="Network interface (e.g., eth0, wlan0)")
    parser.add_option("--mac", dest="mac", help="New MAC address (e.g., 00:11:22:33:44:55)")
    parser.add_option("--show", dest="show_interfaces", action="store_true", help="Show available interfaces")

    (options, _) = parser.parse_args()

    if options.show_interfaces:
        subprocess.call(["ifconfig"])
        return

    if not options.interface or not options.mac:
        parser.print_help()
        print("\n[!] Error: You must specify both interface and MAC address.")
        return

    change_mac(options.interface, options.mac)

if __name__ == "__main__":
    start()
