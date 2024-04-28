import base64
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import serialization, hashes 

def decodeBase64(filename):
    with open(filename, 'r') as f:
        ascii_text = f.read()
    decoded_text = base64.b64decode(ascii_text)
    encrypted_message = decoded_text[:-256]
    encrypted_key = decoded_text[-256:]
    return encrypted_message, encrypted_key

def decryptKey(private_key_path, encrypted_key):
    # Load the private key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    # Decrypt the key
    key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return key

def decryptMessage(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

def writeToFile(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)
    # print(f"{filename} has been created.")

def saveKeyToFile(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def main():
    encrypted_message, encrypted_symmetric_key = decodeBase64("receiver_file/encrypted_message_and_symmetric_key.txt")

    # Decrypt the key using the private key from "sk_receiver.pem"
    symmetric_key = decryptKey("receiver_file/sk_receiver.pem", encrypted_symmetric_key)
    saveKeyToFile(symmetric_key, 'receiver_file/symmetric_key.pem')

    # Decrypt the message using the key
    decrypted_message = decryptMessage(symmetric_key, encrypted_message)

    writeToFile("receiver_file/compressed_message.txt", decrypted_message)
    print("Decode successfully.")

if __name__ == "__main__":
    main()
