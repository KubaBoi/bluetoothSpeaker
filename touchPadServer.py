#!/usr/bin/env python3
import pyautogui
import socket

class TouchPadServer:
    def __init__(self):
        pass

    def start(self):
        HOST = ""  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        print("Running...")
        conn, addr = s.accept()
        print("Connected by", addr)
        i = 0

        self.down = False

        while True:
            try:
                self.oldPosition = pyautogui.position()
                deltaPosition = [0,0]
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    self.newPosition = pyautogui.position()

                    if (deltaPosition[0] == 0 and deltaPosition[1] == 0 and
                        self.newPosition[0] - self.oldPosition[0] != 0 and
                        self.newPosition[1] - self.oldPosition[1] != 0):
                        self.oldPosition = self.newPosition
                    

                    deltaPosition = []
                    deltaPosition.append(self.newPosition[0] - self.oldPosition[0])
                    deltaPosition.append(self.newPosition[1] - self.oldPosition[1])

                    self.oldPosition = self.newPosition
                    r = str(deltaPosition[0]) + "," + str(deltaPosition[1])
                    print(r)
                    conn.sendall(bytes(r, "utf-8"))

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
    

touchPad = TouchPadServer()
touchPad.start()