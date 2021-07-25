#!/usr/bin/env python3
import pyautogui
import json
import socket

class TouchPadServer:
    def __init__(self):
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
                    if not data:
                        break
                    
                    newPosition = pyautogui.position()

                    deltaPosition = []
                    deltaPosition.append(newPosition[0] - oldPosition[0])
                    deltaPosition.append(newPosition[1] - oldPosition[1])

                    oldPosition = newPosition
                    r = str(deltaPosition[0]) + "," + str(deltaPosition[1])

                    conn.sendall(bytes(r))
            except Exception as e:
                print("Disconnected by", addr)
                print(str(i) + ": ")
                print(str(e))
                i += 1

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((HOST, PORT))
                s.listen(5)
                conn, addr = s.accept()
                print("Connected by", addr)