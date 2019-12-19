#!/usr/bin/env python

import csv
import json
from netmiko import Netmiko
from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")
username = "networkchuck"
password = "Password123!"

site = input("Which site are you configuring?: ")

thecsvsitefile = "sites.csv"
thejsonsitefile = "sites_" + site + ".json"
sitedata = {}
with open(thecsvsitefile) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['Site_Name']
        sitedata[id] = rows

with open(thejsonsitefile, 'w') as jsonFile:
    jsonFile.write(json.dumps(sitedata, indent=4))

with open(thejsonsitefile) as f:
    jsondata = f.read()
json_dict = json.loads(jsondata)
sitenumber = json_dict[site]["Site Number"]


router_vlan7 = "10." + sitenumber + ".1.1 255.255.255.0"
router_vlan9 = "10." + sitenumber + ".2.1 255.255.255.0"
router_vlan999 = "10.99." + sitenumber + ".1 255.255.255.0"

switch_vlan999 = "10.99." + sitenumber + ".2 255.255.255.0"


router = {
    "host": json_dict[site]["Router IP"],
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

switch = {
    "host": json_dict[site]["Switch IP"],
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

devices = [router, switch]





for device in devices:
    if device == router:
        template = ENV.get_template("router_template.j2")
        deviceconfig_dict = {
            "hostname": site + "RTR01",
            "vlan7": router_vlan7,
            "vlan9": router_vlan9,
            "vlan999": router_vlan999,
        }
        config = template.render(siteinfo=deviceconfig_dict).split('\n')
        print("Configuring the router")
        net_connect = Netmiko(**device)
        output = net_connect.send_config_set(config)
        net_connect.disconnect()
        print("Router configuration complete")
    else:
        template = ENV.get_template("switch_template.j2")
        deviceconfig_dict = {
        "hostname": site + "SW01",
        "vlan999": switch_vlan999,
        }
        config = template.render(siteinfo=deviceconfig_dict).split('\n')
        print("Configuring the switch")
        net_connect = Netmiko(**device)
        output = net_connect.send_config_set(config)
        print("Switch configuration complete")
        net_connect.disconnect()
    
