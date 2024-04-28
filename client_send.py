import socket

def sendFileToServer(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
        # sendto() is used in UDP which may cause no response from the server
        clientSock.send(file_data) 
        print(f"File '{filename}' sent successfully.")

if __name__ == "__main__":
    # Modify the SERVER_IP_ADDRESS to the IP address of the server
    SERVER_IP_ADDRESS = "192.168.137.29"
    TCP_PORT_NO = 5001
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect((SERVER_IP_ADDRESS, TCP_PORT_NO))
    
    file = "sender_file/encrypted_message_and_symmetric_key.txt"
    sendFileToServer(file)

    clientSock.close()
