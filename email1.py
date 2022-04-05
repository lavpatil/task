from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
  

msg = MIMEMultipart()
  
  
message = "Thank you"
  

password = "nokia@2021"
msg['From'] = "lavpatil2015@gmail.com"
msg['To'] = "lavpatil2015@gmail.com"
msg['Subject'] = "Subscription"
  

msg.attach(MIMEText(message, 'plain'))
  

server = smtplib.SMTP('smtp.gmail.com: 587')
  
server.starttls()
  

server.login(msg['From'], password)
  
  

server.sendmail(msg['From'], msg['To'], msg.as_string())
  
server.quit()
  
print("successfully sent email to %s:" % (msg['To']))
