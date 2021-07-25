#!/usr/bin/env python3

import json
import pyautogui
import socket

HOST = "192.168.0.107"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"1")
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        data = decoded.split(",")

        position = pyautogui.position()
        pyautogui.dragTo(position[0] + int(data[0]), position[1] + int(data[1]))

print('Received', repr(data))

#pyautogui.moveTo(x+10, y+50)
