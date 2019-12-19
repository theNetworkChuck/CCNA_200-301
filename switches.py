#!/usr/bin/env python

from netmiko import Netmiko

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
    showint = net_connect.send_command("show interfaces", use_textfsm=True)
    showproc = net_connect.send_command("show processes cpu", use_textfsm=True)
    showspan = net_connect.send_command("show spanning-tree", use_textfsm=True)
    hostname = showver[0]['hostname']
    spanstat0 = showspan[0]['status']
    spanstat1 = showspan[1]['status']
    spanstat2 = showspan[2]['status']
    cpu5sec = showproc[0]['cpu_5_sec']
    cpu1min = showproc[0]['cpu_1_min']
    cpu5min = showproc[0]['cpu_5_min']
    inputerrors0 = showint[0]['input_errors']
    inputerrors1 = showint[1]['input_errors']
    inputerrors2 = showint[2]['input_errors']
    duplex0 = showint[0]['duplex']
    duplex1 = showint[1]['duplex']
    duplex2 = showint[2]['duplex']
    stat0 = showint[0]['link_status']
    stat1 = showint[1]['link_status']
    stat2 = showint[2]['link_status']
    prot0 = showint[0]['protocol_status']
    prot1 = showint[1]['protocol_status']
    prot2 = showint[2]['protocol_status']
    ipadd0 = showint[0]['ip_address']
    ipadd1 = showint[1]['ip_address']
    ipadd2 = showint[2]['ip_address']
    print("_________" + hostname + "__________" + "\n" + "CPU Stats ------> 5 seconds: " + cpu5sec + "%, 1 minute: " + cpu1min + "%, 5 min: " + cpu5min + "%\n"
    + "\n\n" )
    print("---->KEY INTERFACE STATS" + "\n")
    print(showint[0]['interface'] + "\n" + "Status: " + stat0 + "\n" + "Protocol: " + prot0 + "\n" + "Duplex: " + 
    duplex0 + "\n" + "Input Errors: " + inputerrors0 + "\n" + "Spanning-Tree Status: " + spanstat0 + "\n" + "IP Address: " + 
    ipadd0 + "\n")
    print(showint[1]['interface'] + "\n" + "Status: " + stat1 + "\n" + "Protocol: " + prot1 + "\n" + "Duplex: " + 
    duplex1 + "\n" + "Input Errors: " + inputerrors1 + "\n" + "Spanning-Tree Status: " + spanstat1 + "\n" + "IP Address: " + 
    ipadd1 + "\n")
    print(showint[2]['interface'] + "\n" + "Status: " + stat2 + "\n" + "Protocol: " + prot2 + "\n" + "Duplex: " + 
    duplex2 + "\n" + "Input Errors: " + inputerrors2 + "\n" + "Spanning-Tree Status: " + spanstat2 + "\n" + "IP Address: " + 
    ipadd2 + "\n")
    net_connect.disconnect()
