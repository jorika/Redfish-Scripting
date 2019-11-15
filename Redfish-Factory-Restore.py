#Redfish Restore Factory Defaults for the Gigabyte systems
#2019-11-13
#Python 2 is required
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import json
import sys

print("Redfish Restore Factory Defaults for the Gigabyte systems")
print("Python 2 is required [2019-11-13]")

userIP = raw_input ("Please enter the BMC IP address: ")
print("You have entered IP: " + userIP)
userName = raw_input ("Please enter the Username: [by default Administrator] ")
userPassword = raw_input ("Please enter the Password: [by default superuser] ")

url = 'https://%s/redfish/v1/Managers/Self/Actions/RedfishDBReset' % (userIP)
payload = {'FactoryResetType': 'ResetAll'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers,verify=False,auth=(userName,userPassword))
