import os
from socket import *
from pip._vendor.distlib.compat import raw_input

host = " " #IP address of target computer
port = 8080
socket = socket(AF_INET, SOCK_DGRAM)

def connect():
    socket.connect((host,port))

def send(data):
    socket.send(data.encode('utf-8'))
    
def close():
    socket.close()
    os._exit(0)