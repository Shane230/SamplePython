import subprocess
p = subprocess.Popen(["TASKLIST", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('Httpd' in out):
    print('Httpd running')
if ('mysql' in out):
    print('mysql running')