import socket
import sys
import threading
import time
import pyaudio

recipient = sys.argv[1]
inPort = int(sys.argv[2])
outPort = int(sys.argv[3])

def poll(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(data.decode())

inSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
outSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

inSock.bind((host, inPort))

polling = threading.Thread(target = poll, args = (inSock,))
polling.daemon = True
polling.start()

while True:
    msg = input()

    if msg == "/q":
        sys.exit()
    else:
        outSock.sendto(str.encode(msg), (recipient, outPort))

