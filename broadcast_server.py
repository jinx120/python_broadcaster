import socket
import threading 
from datetime import datetime



# host = input("Enter IP Address to use: ")
host = '0.0.0.0'
port = input("Enter port to use: ")
try: 
    port = int(port)
except:
    print("Failed to convert port string to integer!")
    os._exit(1)

try: 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
except:
    print("Error starting server please try again!")
    os._exit(1)
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
                index = clients.index(client)
                clients.remove(client)
                client.close()
                break

def connect():
    while True:
        client, address = server.accept()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        client.send(f'Server {current_time}: Remote connection established!'.encode())
        clients.append(client)


def write():
    while True:
        message = input("Enter message to broadcast: ")
        broadcast(message, clients)

print("Server started.. ")
write_thread = threading.Thread(target=write)
write_thread.start()
connect()
