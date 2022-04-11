#!/usr/bin/python

import smtplib
import os
import sys

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

str = "os.environ['JOB_NAME']{}"

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
            <td>str.format{"a "}</td>
            <td>${result.BUILD_NUMBER}</td>
            <td>{${result.BUILD_NUMBER}}</td>
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
   print(str.format("a "))
   print ('Number of arguments:', len(sys.argv), 'arguments.')
   print ('Argument List:', str(sys.argv[1]))
   print ('Argument List:', str(sys.argv[2]))
   print ('Argument List:', str(sys.argv[3]))
except Exception as ex:
   print ("Error: unable to send email",ex)

