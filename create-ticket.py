# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jithinkumar900.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0FbmVeBU4icwofZHPyPEuFU1YV9JBJOWgViGWrIoNDXrW2zkHqJCFhWryC1PYq9w4oj3k0PDWaDEazKhr8HkXWDaQOaUyazwxJ9sseEa4RqRmCNPIMpY7fMCbQdb0DjTNJBxaMwtorIpuZ77QRmzPWh9eaOuBrtA1MD-UQwmE_YU=05739F00"

auth = HTTPBasicAuth("jithinkumar900@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {

    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
  
    "issuetype": {
      "id": "10002"
    },
    "project": {
      "key": "JIT"
    },
    "summary": "Some issue raised in github",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))