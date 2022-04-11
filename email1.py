#!/usr/bin/python

from cgitb import html
from email import message
import smtplib
import os
import sys

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']




def func(JOB_NAME, BUILD_NUMBER, BUILD_URL):
   message= '''
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
   return message

try:
   
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
   print(os.environ['JOB_NAME'])
   print(os.environ['BUILD_NUMBER'])
   print(os.environ['BUILD_URL'])
   print ('Number of arguments:', len(sys.argv), 'arguments.')
   print ('Argument List:', str(sys.argv[1]))
   print ('Argument List:', str(sys.argv[2]))
   print ('Argument List:', str(sys.argv[3]))
except Exception as ex:
   print ("Error: unable to send email",ex)
