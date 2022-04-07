
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd


html = '''
html>
<p style="color : black ; font-size : 11px;">Hi All,</p>
<head>
<style>
table {
font-family: arial, sans-serif;
border-collapse: collapse;
width: 100%;
}
td, th, td {
      
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
    '''


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
