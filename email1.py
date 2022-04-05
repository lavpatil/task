import smtplib
import codecs

gmail_user = 'lavpatil2015@gmail.com'
gmail_password = 'nokia@2021'

sent_from = gmail_user
to = ['lavpatil2015@gmail.com']
subject = 'this first jenkins'
body = 'table.py'


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
    
f=codecs.open("table.html", 'r')
print f.read()
