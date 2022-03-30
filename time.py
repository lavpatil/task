from urllib.request import urlopen
    from urllib.parse import quote
except ImportError:  # Python 2
    from urllib2 import urlopen, quote

import json
import contextlib

status_list_dict = {}
with contextlib.closing(
    urlopen("http://localhost:8080/api/json")
) as job_list_response:
    job_list = json.load(job_list_response)["jobs"]

for job in job_list:
    status_counts = [0,0,0,0]

    with contextlib.closing(
        urlopen(
            "http://localhost:8080/job/jobA/lastBuild/wfapi/describe".format(
                job_name=quote(job["name"])
            )
        )
    ) as build_list_response:
        build_list = json.load(build_list_response)["allBuilds"]

        for build_data in build_list:
            if build_data["result"] == "SUCCESS":
                status_counts[0] += 1
            elif build_data["result"] == "FAILURE":
                status_counts[1] += 1
            elif build_data["result"] == "UNSTABLE":
                status_counts[2] += 1
            elif build_data["result"] == "ABORTED":
                status_counts[3] += 1

     status_list_dict[job["name"]] = status_counts
