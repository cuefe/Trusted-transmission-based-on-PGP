from generate_plaintext_and_hash import outputHash
from cryptography.hazmat.primitives import hashes, serialization 
from cryptography.hazmat.primitives.asymmetric import rsa, padding 

# Generates a pair of key and saves them respectively.
def generateKeys():
    privkey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    pubkey = privkey.public_key()

    with open('./sender_file/pk_sender.pem', 'wb') as f:
        f.write(pubkey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    with open('./sender_file/sk_sender.pem', 'wb') as f:
        f.write(privkey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

# Signs the hash value with the private key and returns the signature.
def signHash():
    with open('./sender_file/sk_sender.pem', 'rb') as f:
        privkey = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    hash_value = outputHash()
    with open('sender_file/hash_value.txt','w') as f:
        f.write(hash_value)

    signature = privkey.sign(
        hash_value.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        # padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    return signature

def outputSignature():
    return signHash()

if __name__ == "__main__":
    generateKeys()
    