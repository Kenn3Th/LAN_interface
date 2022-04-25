# echo-client.py

import socket
from time import sleep

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
count = 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while count < 5:
        string = bytes(f"Hei hei, jeg har sendt {count+1} meldinger", encoding='utf-8')
        s.sendall(string)
        data = s.recv(1024)
        sleep(0.5)
        print(f"Received {data!r}, count: {count}")
        count += 1
    s.close()

