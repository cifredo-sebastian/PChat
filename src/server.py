import os
from socket import *
host = ""
port = 8080
buf = 1024
addr = (host, port)
socket = socket(AF_INET, SOCK_DGRAM)

def openserver():
    socket.bind(addr)
    print ("Waiting to receive messages...")
    while True:
        data = socket.recv(buf).decode('utf-8')
        print ("Received message: " + data)
        if data == "exit":
            break
