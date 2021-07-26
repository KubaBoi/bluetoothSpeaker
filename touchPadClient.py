#!/usr/bin/env python3

import json
from tkinter.constants import NONE
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

        try:
            pyautogui.dragRel(int(data[0]), int(data[1]))
        except Exception as e:
            print(str(e))
