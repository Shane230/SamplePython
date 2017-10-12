
#import pywin32
import win32serviceutil
import win32service
import win32event

from subprocess import Popen, PIPE

import psutil
import os

MASTER_MT = "Jenkins"
MT_SERVICE_NAME = "Jenkins,Tomcat9"
s1,s2 = MT_SERVICE_NAME.split(",")


def checkServiceStatus(server):
    status = None
    try:
        service = psutil.win_service_get(server)
        status = service.as_dict()
    except Exception as ex:
        print(str(ex))

    return status

statusS1 = checkServiceStatus(s1)

#print(statusS1.__getitem__(0))
#print('s1 status'+ statusS1 )


try:
    win32serviceutil.StopService(s1)
    print('{} stopped'.format(s1))
except(RuntimeError):
    print ('could not stop service {}'.format(s1))


