import requests
from requests.auth import HTTPBasicAuth


res = requests.get('http://localhost:9090/, ',auth = HTTPBasicAuth('lav', 'Nokia@2021'))


info = server.get_job_info('job-name')
# Loop over builds
builds = info['builds']
for build in builds:
    for build in builds:
        print(server.get_build_info('job-name', 
                                    build['number']))
