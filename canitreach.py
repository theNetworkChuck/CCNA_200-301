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

core2 = {
    "host": "10.16.0.2",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

r1az = {
    "host": "10.16.6.5",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

r2nv = {
    "host": "10.16.7.6",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

r3fl = {
    "host": "10.16.7.7",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

core1 = {
    "host": "10.16.0.1",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

devices = [flswitch, access1, core1, core2, r3fl, r2nv, r1az]

client = input("What is the IP address that your client can't reach? ")

for x in devices:
    net_connect = Netmiko(**x)
    showver = net_connect.send_command("show version", use_textfsm=True)
    hostname = showver[0]['hostname']
    ping = net_connect.send_command("ping " + client)
    if "....." in ping:
        print(hostname + " can't connect.")
    else:
        print(hostname + " -------> is good")
    net_connect.disconnect()
