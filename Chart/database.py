from email import encoders
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
import mimetypes
from email.mime.multipart import MIMEMultipart
import cx_Oracle
from os import listdir
from os.path import isfile, join
from email.mime.text import MIMEText
import numpy as np
import matplotlib.pyplot as plt
from email.mime.image import MIMEImage
import smtplib, os
import csv

path = 'c://Python_Lessons//DB_Charts//'
os.chdir(path)

values=[]
performance=[]
conn_str = u'CHINOOK/summer2017@localhost:1521/xe'
connVariable = cx_Oracle.connect(conn_str)
c = connVariable.cursor()
c.execute(u'select distinct ar.NAME,count(*) as "No Of Album" from album al,artist ar where ar.ARTISTID = al.ARTISTID group by ar.NAME having count(*) >=10 order  by count(*) desc')
for row in c:
    values.append(row[0])
    performance.append(row[1])

with open(path+'out.csv', 'w') as csvfile:
    fileWriter = csv.writer(csvfile)

    for row in c:
        print(row)
        fileWriter.writerow(row)

connVariable.close()
csvfile.close()

y_pos = np.arange(len(values))

plt.ylabel('Number Of Albums')
plt.title('Artist')


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, values)

#plt.show()


plt.savefig(path+'BarChart.png')

plt.close()



print(performance)
print(values)
labels = values
sizes = performance
#labels = 'Python', 'C++', 'Ruby', 'Java','Perl'
#sizes = [215, 130, 245, 210,150]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
explode = (0.1, 0.1, 0.1, 0.1,0.1)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.savefig(path+'PieChart.png')
#plt.show()

##attachment part

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)



gmail_user = 'cthangam230@gmail.com'
gmail_password = 'Ganesha33+'

sent_from = gmail_user
to = ['prabu.ts@gmail.com']
subject = "OMG Super Important Message"
body = 'Hey, what"s up?\n\n- You'

msg = MIMEMultipart('alternative')




attachment = []
i=0
for f in onlyfiles:  # add files to the message
        file_path = os.path.join(path, f)
        attachment.append(file_path)
        ctype, encoding = mimetypes.guess_type(file_path)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(file_path)
            # Note: we should handle calculating the charset
            msgText1 = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
            msg.attach(msgText1)

        elif maintype == "image":

            fp = open(file_path, 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            img.add_header('Content-ID', '<{}>'.format(attachment[i]))
            msg.attach(img)

        else:
            fp = open(file_path, "rb")
            attachFile = MIMEBase(maintype, subtype)
            attachFile.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachFile)
            msg.attach(attachFile)

        i+=1

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br><br><img src="cid:%s"><br>' % (body,attachment[0],attachment[2]), 'html')
msg.attach(msgText)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print('Email sent!')
except:
    print ('Something went wrong...')

