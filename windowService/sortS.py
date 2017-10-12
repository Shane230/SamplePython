import psutil
import win32serviceutil
def checkServiceStatus(server):
    status = None
    try:
        service = psutil.win_service_get(server)
        status = service.as_dict()
        print("%s (%s)" % (status['name'], status['display_name']))
        print("status: %s, start: %s, username: %s, pid: %s" % (
        status['status'], status['start_type'], status['username'], status['pid']))
        print("binpath: %s" % status['binpath'])
        print(" ")
        win32serviceutil.StopService(server)
    except Exception:
        pass
    return status

checkServiceStatus('Tomcat9')
checkServiceStatus('AdobeARMservice')

