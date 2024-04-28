import os
import socket

def receive(filename):
    with open(filename, "w") as file:
        pass

    TCP_IP_ADDRESS = "0.0.0.0"
    TCP_PORT_NO = 5001
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((TCP_IP_ADDRESS, TCP_PORT_NO))

    # Listen for incoming connections
    serverSock.listen(5)
    print("TCP server has started and is listening on port", TCP_PORT_NO)

    while True:
        # Accept incoming connection
        clientSock, addr = serverSock.accept()
        print("Connection established with", addr)
        with open("receiver_file/ip.txt","w") as IP:
            IP.write(str(addr[0]))
        while True:
            # Receive data sent by the client
            data = clientSock.recv(1024)

            if not data:  # If no more data is received, close the connection
                print("Connection closed by", addr)
                clientSock.close()
                exit(0)

            print("Received message from", addr, ":", data.decode())

            # Write received data to the local file test.txt
            with open(filename, "a") as file:
                file.write(data.decode())

if __name__ == "__main__":
    filename = "receiver_file/encrypted_message_and_symmetric_key.txt"
    receive(filename)