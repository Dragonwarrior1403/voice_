#!/usr/bin/env python3
import threading
import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT = "Disconnect!"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ADDR))

def handle_client(conn,addr):
    print(f"New connections {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT:
            connected = False
        print(f"[{addr}] {msg }")
    conn.close()

def start():
    server.listen()
    print(f"[Listen] on {SERVER}")
    while True:

        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Active {threading.activeCount()-1}")

print("Server is starting")
start()
