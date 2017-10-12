import cx_Oracle
import csv





conn_str = u'CHINOOK/summer2017@localhost:1521/xe'
connVariable = cx_Oracle.connect(conn_str)
c = connVariable.cursor()
c.execute(u'select distinct ar.NAME,count(*) as "No Of Album" from album al,artist ar where ar.ARTISTID = al.ARTISTID group by ar.NAME having count(*) >=10 order  by count(*) desc')

with open('c://Python_Lessons//report//out.csv', 'w') as csvfile:
    fileWriter = csv.writer(csvfile)

    for row in c:
        print(row)
        fileWriter.writerow(row)

connVariable.close()
csvfile.close()

