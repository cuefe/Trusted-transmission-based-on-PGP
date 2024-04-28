from cryptography.fernet import Fernet 
from extract_plaintext_and_verify_signature import extract

def loadFromFile(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

def saveToFile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def encryptHashValue(key, hashValue):
    f = Fernet(key)
    encrypted_hash_value = f.encrypt(hashValue)
    return encrypted_hash_value

def main():
    symmetric_key = loadFromFile('receiver_file/symmetric_key.pem')
    hash_value = loadFromFile('receiver_file/hash_value.txt')
    encrypted_hash_value = encryptHashValue(symmetric_key, hash_value)
    saveToFile(encrypted_hash_value, 'receiver_file/encrypted_hash_value.txt')

if __name__ == "__main__":
    main()
