import socket
import time
import os 

host = input("Enter host address: ")
port = input("Enter port: ") 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

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
