#!/usr/bin/env python3
import pyautogui
import json
import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("Running...")
conn, addr = s.accept()
print("Connected by", addr)
i = 0

while True:
    try:
        oldPosition = pyautogui.position()
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            
            newPosition = pyautogui.position()

            print(newPosition)
            print(oldPosition)

            deltaPosition = []
            deltaPosition.append(newPosition[0] - oldPosition[0])
            deltaPosition.append(newPosition[1] - oldPosition[1])

            oldPosition = newPosition
            print(deltaPosition)
            print(json.dumps(deltaPosition))
            print(bytes(json.dumps(deltaPosition), "utf-8"))

            conn.sendall(bytes(json.dumps(deltaPosition), "utf-8"))
    except Exception as e:
        print("Disconnected by", addr)
        print(str(i) + ": ")
        print(e)
        i += 1
        conn, addr = s.accept()
        print("Connected by", addr)