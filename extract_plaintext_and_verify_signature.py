import hashlib     
import datetime
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import serialization,hashes 

def extract():
    with open('receiver_file/decompressed_message.txt','rb') as f:
        decompressed_message = f.read()
       
    time_and_plaintext = decompressed_message[:decompressed_message.index(b'###SEPARATOR###')]
    timestamp = time_and_plaintext[:8]
    plaintext = time_and_plaintext[8:]

    with open('receiver_file/plaintext.txt','wb') as f:
        f.write(plaintext)
    
    dt_object = datetime.datetime.fromtimestamp(int.from_bytes(timestamp, byteorder='big'))
    print("Time of send: ",dt_object)

    signature = decompressed_message[decompressed_message.index(b'###SEPARATOR###')+len(b'###SEPARATOR###'):]
    # signature = b"123"

    hash_value = hashlib.sha256(plaintext).hexdigest()
    # hash_value = "123"

    with open('receiver_file/hash_value.txt','w') as f:
        f.write(hash_value)

    return timestamp, plaintext, signature, hash_value

def verifySignature():
    with open('receiver_file/pk_sender.pem', 'rb') as f:
        pubkey = serialization.load_pem_public_key(
            f.read()
        )

    timestamp, plaintext, signature, hash_value = extract()

    # print(signature)
    
    try:
        verifier = pubkey.verify(
            signature,
            hash_value.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            # padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Signature is valid.")
    except Exception as e:
        print("Signature is invalid.")

def main():
   verifySignature()

if __name__ == "__main__":
    main()