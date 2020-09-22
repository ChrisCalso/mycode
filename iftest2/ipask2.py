#!/usr/bin/env python3
import ipaddress
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway
if ipchk  == "192.168.70.1":
    ipaddress == ipaddress.ip_address(ipchk)
    print("Looks like the IP address of the Gateway was set: " + ipaddress + " This is not recommended.")

elif ipchk.ip_address(): # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

