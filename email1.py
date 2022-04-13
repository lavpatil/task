#!/usr/bin/python
from cgitb import html
import smtplib
import ssl
from email import encoders, message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jenkinsapi.jenkins import Jenkins



def func(JOB_STATUS, BUILD_NUMBER, BUILD_URL):
   html= '''
   <!DOCTYPE html>
   <html>
      <head>
         <style>
            table, th, td {{
               border: 1px solid black;
            }}
         </style>
      </head>
      <body>
         <h2>JOB Details</h2>
         <table>
            <tr>
               <th>Job Status</th>
               <th>Build Number</td>
               <th>Job URL</td>
            </tr>
            <tr>
               <td>{JOB_STATUS}</td>
               <td>{BUILD_NUMBER}</td>
               <td>{BUILD_URL}</td>
            </tr>
         </table>
      </body>
   </html>
   '''.format(JOB_STATUS=JOB_STATUS, BUILD_NUMBER=BUILD_NUMBER, BUILD_URL=BUILD_URL)
   return html


def emai():
   J = Jenkins('http://localhost:8080', 'lav', 'nokia@2021')
   job = J['email']
   lgb = job.get_last_build()
   BUILD_URL = lgb.get_build_url()
   BUILD_NUMBER = lgb.get_number()
   JOB_STATUS = lgb.get_status()
   sender_email = "lavpatil2015@gmail.com"
   receiver_email = "lavpatil2015@gmail.com"
   password = "nokia@2021"
   
   
   msg = MIMEMultipart("alternative")
   msg["Subject"] = "Build Details"
   msg["From"] = sender_email
   msg["To"] = receiver_email
   html=func(JOB_STATUS, BUILD_NUMBER, BUILD_URL)
   message=MIMEText(html,'html')
   msg.attach(message)
   
   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print ("Successfully sent email")

emai()
