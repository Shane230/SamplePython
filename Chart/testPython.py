import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.mime.base import MIMEBase
import mimetypes
from email.mime.multipart import MIMEMultipart
from os import listdir
from os.path import isfile, join
import smtplib, os
from datetime import datetime
#from email import Encoders

path = 'c://Python_Lessons//DB_Charts//'
os.chdir(path)

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)


gmail_user = 'cthangam230@gmail.com'
gmail_password = 'Ganesha33+'

sent_from = gmail_user
to = ['prabu.ts@gmail.com']
subject = "OMG Super Important Message"
body = 'Hey, what"s up?\n\n- You'

msg = MIMEMultipart('alternative')

part = MIMEBase('application', "octet-stream")

part.set_payload(open('C://Python_Lessons//DB_Charts//out.csv', "rb").read())
part.add_header("Content-Disposition", 'attachment', filename='out.csv')
msg.attach(part)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print('Email sent!')
except:
    print ('Something went wrong...')

