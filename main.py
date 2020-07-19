import time
import ftputil
import logging

logging.basicConfig(filename='ftplog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start program')
ftp_host = 'enterhostname'
ftp_username = 'enterusername'
ftp_password = 'enterpassword'
ftp_path = '/PATH/TO/DIRECOTRY/TO/PROCESS'

host = ftputil.FTPHost(ftp_host,ftp_username,ftp_password)
now = time.time()
host.chdir(ftp_path)
names = host.listdir(host.curdir)
for name in names:
    if host.path.getmtime(name) < (now - (5 * 86400)):
        if host.path.isdir(name):
            host.rmtree(name, ignore_errors=False, onerror=None)
            print('Folder: '+ftp_path+'/'+name+ ' has been deleted from server')
            logging.debug('Folder: '+ftp_path+'/'+name+ ' has been deleted from server')
        else:
            logging.debug('Noting to do')
print('ftp connection closed')
logging.debug('ftp connection closed')
host.close()
logging.debug('end of program execution')
