import socket
import time
import os 

host = input("Enter host address: ")
port = input("Enter port: ") 
try:
    port = int(port)
except:
    print("Failed to convert port string to integer!")

try: 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except:
    print("An error occured connecting! Make sure server is running and the informating you entered is correct!")

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
