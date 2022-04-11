#!/usr/bin/python

from cgitb import html
from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import pandas as pd
import os
import sys



def func(JOB_NAME, BUILD_NUMBER, BUILD_URL):
   html= '''
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
            <td>{JOB_NAME}</td>
            <td>{BUILD_NUMBER}</td>
            <td>{BUILD_URL}</td>
         </tr>
      </table>
   </body>
</html>
        '''.format(JOB_NAME=JOB_NAME, BUILD_NUMBER=BUILD_NUMBER, BUILD_URL=BUILD_URL)
   return html

email_from = 'lavpatil2015@gmail.com'
password = 'nokia@2021'
email_to = 'lavpatil2015@gmail.com'


date_str = pd.Timestamp.today().strftime('%Y-%m-%d')


email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'


email_message.attach(MIMEText(html, "html"))

email_string = email_message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
   server.login(email_from, password)
   server.sendmail(email_from, email_to, email_string)
