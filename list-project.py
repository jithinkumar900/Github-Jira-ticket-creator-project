# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jithinkumar900.atlassian.net/rest/api/3/project"

API_TOKEN ="ATATT3xFfGF0FbmVeBU4icwofZHPyPEuFU1YV9JBJOWgViGWrIoNDXrW2zkHqJCFhWryC1PYq9w4oj3k0PDWaDEazKhr8HkXWDaQOaUyazwxJ9sseEa4RqRmCNPIMpY7fMCbQdb0DjTNJBxaMwtorIpuZ77QRmzPWh9eaOuBrtA1MD-UQwmE_YU=05739F00"

auth = HTTPBasicAuth("jithinkumar900@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

needed_response=json.loads(response.text)

for i in range(len(needed_response)):
    name = needed_response[i]["name"]
    print(name)