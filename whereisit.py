#!/usr/bin/env python

from netmiko import Netmiko

username = "networkchuck"
password = "Password123!"



access1 = {
    "host": "192.168.243.238",
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



devices = [flswitch, access1]

clientmac = input("What is the mac address of the PC?: ")

for x in devices:
    net_connect = Netmiko(**x)
    here = net_connect.send_command("show mac address-table address " + clientmac, use_textfsm=True)
    showver = net_connect.send_command("show version", use_textfsm=True)
    hostname = showver[0]['hostname']
    try:
        thehost = here[0]['destination_address']
    except TypeError:
        thehost = "nope"
    if thehost != "nope":
        port = here[0]['destination_port']
        vlan = here[0]['vlan']
        print("The host is connected to " + hostname + ", " + port + " on vlan " + vlan + ".")


print("done")
