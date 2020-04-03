import pyaudio
import socket
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                output = True,
                frames_per_buffer = CHUNK)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9001

sock.bind((host, port))

while True:
    print("Waiting for client...")

    data, addr = sock.recvfrom(4096)

    print("Receiving data from", addr)

    stream.write(data)


