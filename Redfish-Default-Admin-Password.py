#Redfish Change Default Password for Gigabyte systems
#2019-11-14
#Python 2 is required
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import json
import sys

print("Redfish Default Password for Gigabyte systems")
print("Python 2 is required [2019-11-14]")

userIP = raw_input ("Please enter the BMC IP address: ")
print("You have entered IP: " + userIP)
userName = raw_input ("Please enter the Username: [by default - Administrator or admin] ")
userPassword = raw_input ("Please enter the Password: [by default - superuser or password] ")
userNewPassword = raw_input ("Please enter the NEW Password: [min: 10 characters]")
userNewCheckPassword = raw_input("Please re-enter the NEW Password: [min: 10 characters]")

if userNewPassword == userNewCheckPassword:
    print("The new password will be: " + userNewPassword)
else:
    print("The password does not match")
    print("Please try again later ...")
    exit()


sys = requests.get('https://%s/redfish/v1/AccountService/Accounts/1' % (userIP),verify=False,auth=(userName,userPassword))
sysData = sys.json()
etag = "{}".format(sysData[u'@odata.etag'])

url = 'https://%s/redfish/v1/AccountService/Accounts/1' % (userIP)

headers = {
    'content-type':'application/json',
    'If-Match':etag,
    }

payload = {
    'UserName':userName,
    'Password':userNewPassword,
    }

response = requests.patch(url, data=json.dumps(payload), headers=headers,verify=False,auth=(userName,userPassword))

if response.status_code == 204:
    print("Success!")
else:
    print("Not Found. Error code - ")
    print(response.status_code)
    exit()
