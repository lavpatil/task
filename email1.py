#!/usr/bin/python

from cgitb import html
import smtplib
import os

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

var1 = os.environ['JOB_NAME']
var2 = os.environ['BUILD_NUMBER']
var3 = os.environ['JOB_URL']

html = """
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
            <td>var1</td>
            <td>var2</td>
            <td>var3</td>
         </tr>
      </table>
   </body>
</html>
"""

try:
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, html)         
   print ("Successfully sent email")
except Exception as ex:
   print ("Error: unable to send email",ex)
