import base64
from compress_message_and_signature import outputCompressedMessage
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.asymmetric import rsa, padding 
from cryptography.hazmat.primitives import serialization, hashes 

# Generate a symmetric key using the AES algorithm
def generateKey():
    key = Fernet.generate_key()
    return key

def loadKeyFromFile(filename):
    with open(filename, 'rb') as file:
        key = file.read()
    return key

def encryptMessage(key, compressed_message):
    f = Fernet(key)
    encrypted_message = f.encrypt(compressed_message)
    return encrypted_message

def loadPublicKeyFromFile(filename):
    with open(filename, 'rb') as file:
        public_key = serialization.load_pem_public_key(file.read())
    return public_key

# Encrypt the message using the public key
def rsaEncrypt(public_key, message):
    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

def concatenateAndEncode(encrypted_message, encrypted_symmetric_key):
    # Concatenate the encrypted message and key
    concatenated = encrypted_message + encrypted_symmetric_key
    # Encode the concatenated string to base64
    encoded = base64.b64encode(concatenated)
    return encoded

def saveToFile(data, filename):
    # Save the data to a file
    with open(filename, 'w') as file:
        file.write(data.decode())

def saveKeyToFile(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def main():
    compressed_message = outputCompressedMessage()
    symmetric_key = generateKey()
    saveKeyToFile(symmetric_key, 'sender_file/symmetric_key.pem')
    encrypted_message = encryptMessage(symmetric_key, compressed_message)
   
    # Load the public key from 'pk_receiver.pem' file
    pk_receiver = loadPublicKeyFromFile('sender_file/pk_receiver.pem')

    # Encrypt the symmetric key using the public key
    encrypted_symmetric_key = rsaEncrypt(pk_receiver, symmetric_key)

    # Concatenate and encode the encrypted message and key
    encrypted_message_and_symmetric_key = concatenateAndEncode(encrypted_message, encrypted_symmetric_key)
    saveToFile(encrypted_message_and_symmetric_key, 'sender_file/encrypted_message_and_symmetric_key.txt')
    print("Encode successfully.")

if __name__ == "__main__":
    main()