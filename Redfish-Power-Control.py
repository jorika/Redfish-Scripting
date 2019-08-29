#Redfish Power Control for Gigabyte/AMI systems
#2019-08-28
#Python 2 is required
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import json
import sys

print("Redfish Power Control for Gigabyte/AMI systems")
print("Python 2 is required [2019-08-28]")

userIP = raw_input ("Please enter the IP address AMI BMC: ")
print("You have entered IP: " + userIP)
userName = raw_input ("Please enter the Username: [by default Administrator] ")
userPassword = raw_input ("Please enter the Password: [by default superuser] ")

sys = requests.get('https://%s/redfish/v1/Systems/Self' % (userIP),verify=False,auth=(userName,userPassword))
sysData = sys.json()
print "Current power state:	{}".format(sysData[u'PowerState'])

print(" ")
print("Please choose the Power State (Please use uppercase and lowercase as below) : ")
print("")
userPower = raw_input ("GracefulShutdown, ForceOff, ForceRestart, or On:   ")

url = 'https://%s/redfish/v1/Systems/Self/Actions/ComputerSystem.Reset' % (userIP)
payload = {'ResetType': userPower}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers,verify=False,auth=(userName,userPassword))
