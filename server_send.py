import os
import socket

def sendFileToServer(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
        clientSock.send(file_data) # "sendto" is used in UDP
        print(f"File '{filename}' sent successfully.")

if __name__ == "__main__":
    with open("receiver_file/ip.txt","r") as IP:
        SERVER_IP_ADDRESS = IP.read()
    TCP_PORT_NO = 5001
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    clientSock.connect((SERVER_IP_ADDRESS, TCP_PORT_NO))
    
    file = "receiver_file/encrypted_hash_value.txt"
    sendFileToServer(file)
    clientSock.close()
