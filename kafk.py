import requests
from requests.auth import HTTPBasicAuth


res = requests.get("http://localhost:9090/job/jenk1/6/wfapi",auth = HTTPBasicAuth('lav', 'Nokia@2021'))


print(res.text)
