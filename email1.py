#!/usr/bin/python

import smtplib
import os

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

jn= os.environ['JOB_NAME']
jb= os.environ['BUILD_NUMBER']
ju= os.environ['JOB_URL']

message = """From: From Person <lavpatil2015@gmail.com>
To: To Person <lavpatil2015@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

<!DOCTYPE html>
<html>
   <head>
      <style>
         table, th, td {
            border: 1px solid black;
         }
      </style>
   </head>
   <body>
      <h2>JOB Details</h2>
      <table>
         <tr>
            <th>Job Name</th>
            <th>Build Number</td>
            <th>Job URL</td>
         </tr>
         <tr>
            <td>jn</td>
            <td>jb</td>
            '<td>' +ju+ '</td>'
         </tr>
      </table>
   </body>
</html>
"""

try:
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
   print(os.environ['JOB_NAME'])
   print(os.environ['BUILD_NUMBER'])
   print(os.environ['BUILD_URL'])
except Exception as ex:
   print ("Error: unable to send email",ex)

