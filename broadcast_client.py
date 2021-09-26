import socket
import threading 
import datetime as datetime
import time
import os 

port = 8080
host = input("Enter host address: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 8080))

def recieve():
    while True:
        message = client.recv(1024).decode()
        if message == "servercmd0":
            print("Server issued disconnect command!")
            client.close()
            time.sleep(1)
            os._exit(1)
        else:
            print(message)
recieve()