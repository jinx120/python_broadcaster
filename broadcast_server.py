import socket
import threading 
from datetime import datetime
import time
import os 

host = '127.0.0.1' 
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

clients = []

def broadcast(message, clients):
    if message =="dcusrs":
        for client in clients:
            client.send(f'servercmd0'.encode())
        clients = []
    else:   
        for client in clients:
            try:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                client.send(f'Server {current_time}: {message}'.encode())
            except:
                print("removing client")
                index = clients.index(client)
                clients.remove(client)
                client.close()
                break

def connect():
    while True:
        client, address = server.accept()
        client.send("Remote connection established.. Welcome!".encode())
        clients.append(client)


def write():
    while True:
        message = input("Enter message to broadcast: ")
        broadcast(message, clients)

print("Server started.. ")
write_thread = threading.Thread(target=write)
write_thread.start()
connect()