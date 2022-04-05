import smtplib

sender = 'lavpatil2015@gmail.com'
receivers = ['lavpatil2015@gmail.com']

message = """From: From Person <lavpatil2015@gmail.com>
To: To Person <lavpatil2015@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
smtpObj = smtplib.SMTP('8080')
smtpObj.sendmail(sender, receivers, message)         
print ("Successfully sent email")

