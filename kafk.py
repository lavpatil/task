import json
import datetime
from datetime import datetime
from decimal import Decimal
import requests
from requests.auth import HTTPBasicAuth


res = requests.get("http://localhost:9090/job/jenk1/6/wfapi",auth = HTTPBasicAuth('lav', 'Nokia@2021'))

#print(type(res.text))
j_object=json.loads(res.text)

with open('dat.json', 'w') as f:
    json.dump(j_object, f)

f=open('dat.json')
data=json.load(f)

def d_json():
    job_name=data['name']
    job_id=data['id']
    job_status=data['status']
    job_duration=data['durationMillis']//1000
    starttime=datetime.fromtimestamp(data['startTimeMillis']//1000).isoformat()
    endtime=datetime.fromtimestamp(data['endTimeMillis']//1000).isoformat()

    job_details = {"job_name":job_name,"job_id":job_id,"job_status":job_status,"job_duration":job_duration,"starttime":starttime,"endtime":endtime}
    return(job_details)

jo=d_json()        
print(jo)


