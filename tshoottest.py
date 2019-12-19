#!/usr/bin/env python

from netmiko import Netmiko

username = "networkchuck"
password = "Password123!"



access1 = {
    "host": "10.16.0.11",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

flswitch = {
    "host": "10.16.20.10",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

myswitches = [flswitch, access1]

for x in myswitches:
    net_connect = Netmiko(**x)
    ping = net_connect.send_command("show mac address-table address 0050.7966.6802", use_textfsm=True)
    showver = net_connect.send_command("show version", use_textfsm=True)
    hostname = showver[0]['hostname']
    try:
        thehost = ping[0]['destination_address']
    except TypeError:
        thehost = "nope"
    if thehost != "nope":
        print("The host is connected to " + hostname)

print("done")
