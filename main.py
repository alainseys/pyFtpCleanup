import time
import ftputil

ftp_host = 'enterhostname'
ftp_username = ''
ftp_password = ''
ftp_path = ''

host = ftputil.FTPHost(ftp_host,ftp_username,ftp_password)
now = time.time()
host.chdir(ftp_path)
names = host.listdir(host.curdir)
for name in names:
    if host.path.getmtime(name) < (now - (5 * 86400)):
        if host.path.isdir(name):
            host.rmtree(name, ignore_errors=False, onerror=None)
            print('Folder: '+ftp_path+'/'+name+ ' has been deleted from server')
        print('ftp connection closed')
        host.close()
