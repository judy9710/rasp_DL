#ftp_server.py
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
 
FTP_HOST = '192.168.219.110'
FTP_PORT = 21


FTP_USERS_DIR = os.path.join(os.getcwd(), 'VideoImage/Input')

 
def main():
    authorizer = DummyAuthorizer()
    
    authorizer.add_user('user', '', FTP_USERS_DIR, perm='elradfmwMT')
 
    handler = FTPHandler
    handler.banner = "Hyoyoung's FTP Server."
 
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535)
    
    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)
    
    server.max_cons = 256
    server.max_cons_per_ip = 5
 
    server.serve_forever()
 
if __name__ == '__main__':
    main()
