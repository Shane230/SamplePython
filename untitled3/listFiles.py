
import sys,os

#root = "C:\H1b\\"
path = 'C:\H1b'#os.path.join(root, "H1b_2017")

for pathx, subdirs, files in os.walk(path):
    for name in files:
        print(os.path.join(pathx, name))