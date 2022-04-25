import socket
import sys

IP_COMP = "127.0.0.1"
GATEWAY = "198.162.10.0"
PORT = 65432
tries = 0

#10bit = 1024, 12bit = 4096
totBits = 1024

while True:
    argument = input("Do you like to start connection?: ")
    if argument.lower() == "yes":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as compressor:
            print(f"Waiting to connect with IP:{IP_COMP} on port {PORT}")
            compressor.bind((IP_COMP, PORT))
            compressor.listen()
            connection, address = compressor.accept()
            while connection:
                print(f"Connected to address: {address}")
                try:
                    while True:
                        print("Waiting to recieve data")
                        data = connection.recv(totBits)
                        if not data:
                            break
                        connection.sendall(data)
                        print(f"Received: {data}")
                    print("Done receiving")
                    compressor.close()
                    break
                except KeyboardInterrupt:
                    print("Closing socket")
                    compressor.close()
                    sys.exit()
    elif argument.lower() == "no":
        print("quitting!")
        break