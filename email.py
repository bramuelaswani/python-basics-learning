'''import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")'''
   
   
   
   
import smtplib
from smtplib import SMTPException

sender = "user@gmail.com"
receiver = ["user@gmail.com"]
message = "Hello!"

try:
    session = smptlib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,'password')
    session.sendmail(sender,receiver,message)
    session.quit()
except SMTPException:
    print('Error')