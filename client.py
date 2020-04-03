import pyaudio
import socket
import sys
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9001

while True:

    data = stream.read(CHUNK)

    sock.sendto(data, (host, port))

stream.stop_stream()
stream.close()
p.terminate()
