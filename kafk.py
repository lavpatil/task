import json
import datetime
import os
import sys
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth


#res = requests.get("http://localhost:9090/job/jenk1/wfapi",auth = HTTPBasicAuth('lav', 'Nokia@2021'))
resu = requests.get("http://localhost:9090/job/jenk1/9/wfapi",auth = HTTPBasicAuth('lav', 'Nokia@2021'))

#print(type(res.text))
j_object=json.loads(resu.text)
#j_object2=json.loads(res.text)

with open('dat.json', 'w') as f:
    json.dump(j_object, f)
 #   json.dump(j_object2, f)    

f=open('dat.json')
data=json.load(f)
#data1=json.load(f)

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv[1])  ) 

job_name = (sys.argv,os.environ['JOB_NAME'])
print(job_name)

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

def stage():
 for key in data['stages'][1:]:
    stagename=key['name']
    stageid=key['id']
    stagestatus=key['status']
    stageduration=key['durationMillis']//1000
    stagestarttime=datetime.fromtimestamp(data['startTimeMillis']//1000).isoformat()
    stageendtime=datetime.fromtimestamp(data['endTimeMillis']//1000).isoformat()

    dta = {"Stage_Name":stagename,"Stage_ID":stageid,"Stage_Status":stagestatus,"Stage_Duration":stageduration,"Stage_StartTime":stagestarttime,"Stage_endTime":stageendtime}
    return(dta)

st=stage()
print(st)
