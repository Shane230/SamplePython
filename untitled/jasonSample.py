

import json
import pprint
f = open('C:\pythonPractise\sample.json')
data = json.load(f)
f.close()

f=open('C:\pythonPractise\sample.txt', 'w')

for item in data['Employee']:
    f.write(item['name']+' '+item['dept'] +'\n' )


f.close()

