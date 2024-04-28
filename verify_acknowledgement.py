from cryptography.fernet import Fernet 
from extract_plaintext_and_verify_signature import extract

def loadFromFile(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

def saveToFile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def decryptHashValue(key, encrypted_hash_value):
    f = Fernet(key)
    decrypted_hash_value = f.decrypt(encrypted_hash_value)
    return decrypted_hash_value

def main():
    symmetric_key = loadFromFile('sender_file/symmetric_key.pem')
    encrypted_hash_value = loadFromFile('sender_file/encrypted_hash_value.txt')
    receiver_hash_value = decryptHashValue(symmetric_key, encrypted_hash_value)
    sender_hash_value = loadFromFile('sender_file/hash_value.txt')
    print(f"receiver_hash_value: {receiver_hash_value.decode()}")
    print(f"sender_hash_value: {sender_hash_value.decode()}")
    if(receiver_hash_value == sender_hash_value):
        print('The plaintext has been received!')

if __name__ == "__main__":
    main()