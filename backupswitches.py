#!/usr/bin/env python

from netmiko import Netmiko
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d%m%Y_%H-%M-%S")

username = "networkchuck"
password = "Password123!"



Switch1 = {
    "host": "192.168.243.146",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch2 = {
    "host": "192.168.243.149",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch3 = {
    "host": "192.168.243.150",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch4 = {
    "host": "192.168.243.148",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch5 = {
    "host": "192.168.243.147",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

myswitches = [Switch1, Switch2, Switch3, Switch4, Switch5]

for x in myswitches:
    net_connect = Netmiko(**x)
    showver = net_connect.send_command("show version", use_textfsm=True)
    showrun = net_connect.send_command("show run")
    hostname = showver[0]['hostname']
    backupfilename = hostname + "_" + dt_string + ".txt"
    file = open(backupfilename, "w")
    file.write(showrun)
    file.close()
    print(hostname + " has been backed up" + "\n")
    net_connect.disconnect()
