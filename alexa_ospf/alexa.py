import time
from flask import Flask, render_template, request
app = Flask(__name__)

from netmiko import Netmiko
from getpass import getpass

username = "networkchuck"
password = "Password123!"

router1 = {
    "host": "10.1.1.1",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

router2 = {
    "host": "10.1.1.2",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

router3 = {
    "host": "10.1.1.3",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

router4 = {
    "host": "10.1.1.4",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

router5 = {
    "host": "10.1.1.5",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

ospfconfig = ["router ospf 77", "network 10.1.1.0 0.0.0.255 area 0"]
routerlist = [router1, router2, router3, router4, router5]

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName == 'addospf':
        for x in routerlist:
            ospfconfig = ["router ospf 77", "network 10.1.1.0 0.0.0.255 area 0", "do cop r s"]
            net_connect = Netmiko(**x)
            print("configuring " + x["host"])
            configit = net_connect.send_config_set(ospfconfig)
            print("Finished configuring " + x["host"])
    if deviceName == 'ospfremove':
        ospfconfig = ["no router ospf 77", "do cop r s"]
        for x in routerlist:
            net_connect = Netmiko(**x)
            print("configuring " + x["host"])
            configit = net_connect.send_config_set(ospfconfig)
            print("Finished configuring " + x["host"])
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
