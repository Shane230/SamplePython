import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np
import matplotlib.pyplot as plt
from email.mime.image import MIMEImage
import shutil
import os
import time



##Chart generation

values = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(values))
performance = [100, 80, 60, 40, 20, 10]
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, values)

path = 'c://Python_Lessons//charts//'
os.chdir(path)
for File in os.listdir("."):
    if File.endswith(".png"):
        shutil.move('c://Python_Lessons//charts/Chart.png', 'c://Python_Lessons//backup/Chart.png')
        os.rename('c://Python_Lessons//backup/Chart.png', 'c://Python_Lessons//backup/Chart.png'+time.strftime("%H:%M:%S"))
    else:
        continue

plt.savefig(path+'Chart.png')

attachment = 'c://Python_Lessons//charts//Chart.png'

#email section

gmail_user = 'cthangam230@gmail.com'
gmail_password = 'Ganesha33+'

sent_from = gmail_user
to = ['prabu.ts@gmail.com']
subject = "OMG Super Important Message"
body = 'Hey, what"s up?\n\n- You'

msg = MIMEMultipart('alternative')

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (body, attachment), 'html')
msg.attach(msgText)

fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print('Email sent!')
except:
    print ('Something went wrong...')
