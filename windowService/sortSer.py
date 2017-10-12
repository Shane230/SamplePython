
import psutil
import win32serviceutil


MASTER_MT = "Jenkins"
MT_SERVICE_NAME = "Jenkins,Tomcat9,AdobeARMservice"
s1,s2,s3 = MT_SERVICE_NAME.split(",")


def checkServiceStatus(server):
    status = None

    service = psutil.win_service_get(server)
    status = service.as_dict()
    print("%s (%s)" % (status['name'], status['display_name']))
    print("status: %s, start: %s, username: %s, pid: %s" % (status['status'], status['start_type'], status['username'], status['pid']))
    print("binpath: %s" % status['binpath'])

    return status

def StopService(service):
    try:
        win32serviceutil.StopService(service)
        print('{} has been stopped'.format(service))
        print(" ")
    except Exception:
        pass
        print('could not stop service {}'.format(service))
        print(" ")


def server1():
    if (MASTER_MT!= s1 and len(s1)>0):
        statusS1 = checkServiceStatus(s1)
        if(statusS1.get('status') != 'Stopped'):
            StopService(s1)
        else:
            print(s1 +' service already in stopped status')

def server2():
    if (MASTER_MT!= s2 and len(s2)>0):
        statusS2 = checkServiceStatus(s2)
        if(statusS2.get('status') != 'Stopped'):
            StopService(s2)
        else:
            print(s2 +' service already in stopped status')


def server3():
    if (MASTER_MT!= s3 and len(s3)>0):
        statusS3 = checkServiceStatus(s3)
        if(statusS3.get('status') != 'Stopped'):
            StopService(s3)
        else:
            print(s3 +' service already in stopped status')
            print(" ")



options= {
        s1: server1,
        s2: server2,
        s3: server3,
        }

options[s1]()
options[s2]()
options[s3]()
