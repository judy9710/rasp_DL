import socket
import argparse

def run(host, port):
    input_dir = './VideoImage'+'/'+'Input'
    cnt=1;

    cs=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((host, port))

    cs.sendall("Are_you_ready".encode())
    reSize = cs.recv(1024)
    reSize = reSize.decode()
    if reSize == "error":
        sleep(5)
        print("exit !!! ")
        return 

    while True:
        fileName=input_dir+'/'+"cough-"+str(cnt)+".wav"
        cnt += 1

    # Get the expected length (eight bytes long, always)
        expected_size = b""
        while len(expected_size) < 8:
            more_size = cs.recv(8 - len(expected_size))
            if not more_size:
                raise Exception("Short file length received")
            expected_size += more_size

    # Convert to int, the expected file length
        expected_size = int.from_bytes(expected_size, 'big')

    # Until we've received the expected amount of data, keep receiving
        packet = b""  # Use bytes, not str, to accumulate
        while len(packet) < expected_size:
            buffer = cs.recv(expected_size - len(packet))
            if not buffer:
                raise Exception("Incomplete file received")
            packet += buffer
        f=open(fileName, 'wb')
        f.write(packet)
        f.close()

        print("file name : "+fileName)
        print("size : "+str(expected_size))

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p))