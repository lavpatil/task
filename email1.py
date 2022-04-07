#!/usr/bin/python

import smtplib
import os

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

var1 = os.environ['JOB_NAME']
var2 = os.environ['BUILD_NUMBER']
var3 = os.environ['JOB_URL']

body = """From: From Person <lavpatil2015@gmail.com>
To: To Person <lavpatil2015@gmail.com>
Content-type: text/html
Subject: SMTP HTML e-mail test
<html>
<p style="color : black ; font-size : 11px;">Hi All,</p>
<head>
<style>
table {
font-family: arial, sans-serif;
border-collapse: collapse;
width: 100%;
}
td, th, td {
border: 1px solid black;
text-align: left;
padding: 8px;
}
tr:nth-child(even) {
background-color: #dddddd;
}
</style>
</head>
<body>
<h2>Jobs Performed</h2>
<table>
<tr>
<th>Job Name</th>
<th>Build Number</th>
<th>Build URL</th>
</tr>
<tr>
<td>${JOB_NAME}</td>
<td>${BUILD_NUMBER}</td>
<td>${BUILD_URL}</td>
</tr>
</tr>
</table>
<p>Note:-</p>
<p style="color : black ; font-size : 11px;">*This is auto generated mail kindly do not reply.</p>
<p style="color : black ; font-size : 11px;">*For any build query contact CI-Team@kpit.com.</p>
</body>
</html>
"""

try:
   smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtpObj.login(gmail_user, gmail_password)
   smtpObj.sendmail(sender, receivers, body)         
   print ("Successfully sent email")
   print(os.environ['JOB_NAME'])
   print(os.environ['BUILD_NUMBER'])
except Exception as ex:
   print ("Error: unable to send email",ex)
