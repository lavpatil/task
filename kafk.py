# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request
res = requests.get('http://localhost:9090/, ',auth = HTTPBasicAuth('lav', 'Nokia@2021'))

# print request object
print(res)
