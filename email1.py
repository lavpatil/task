#!/usr/bin/python

from cgitb import html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

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
            <td>${JOB_NAME}</td>
            <td>${BUILD_NUMBER}</td>
            <td>${JOB_URL}</td>
         </tr>
      </table>
   </body>
</html>
"""

try:
   email_message = MIMEMultipart()
   email_message.attach(MIMEText(html, "html"))
   email_string = email_message.as_string()
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, email_string)         
   print ("Successfully sent email")
except Exception as ex:
   print ("Error: unable to send email",ex)
