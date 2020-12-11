import socket
import argparse
from os.path import exists
import os
import time
from time import sleep

#def run_server(port, directory):
def run_server(port):
    host = '' 
    directory="VideoImage"
    ss= socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    ss.bind((host, port))
    ss.listen(1)   
        
    conn, addr = ss.accept()
    Name = conn.recv(1024)
    Name = Name.decode()
        
    if Name != "Are_you_ready":
        msg = "error"
        conn.sendall(msg.encode())
        conn.close()
        return
    else:
        msg = "ready"
        conn.sendall(msg.encode())      

    tmpfile_list = os.listdir(directory)
    infile_list = [file for file in tmpfile_list if file.endswith(".wav")] 
     
    while True:
        print(infile_list)
        if len(infile_list) == 0 :
            sleep(10)

        for i in range(0,len(infile_list)): 
            infilename =  directory+'/'+infile_list[i]
            print(infilename)
               
            f=open(infilename, 'rb')
            data=f.read() 
            conn.sendall(len(data).to_bytes(8, 'big'))

            conn.sendall(data)
            f.close()
            os.remove(infilename)


        tmpfile_list = os.listdir(directory)
        infile_list = [file for file in tmpfile_list if file.endswith(".wav")] 
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port ")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()
    run_server(port=int(args.p))
