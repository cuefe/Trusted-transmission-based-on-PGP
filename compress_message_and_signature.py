import zlib
import time
from sign_hash import outputSignature
from generate_plaintext_and_hash import outputPlaintext

# Compresses the timestamp, plaintext and signature and writes them to the "compressed_message.txt" file.
def compressMessage():
    # Get the current timestamp
    timestamp = int(time.time()).to_bytes(8, byteorder = 'big')

    plaintext = outputPlaintext()
    signature = outputSignature()
  
    # Compress the message into bytes code
    message = timestamp + plaintext + b'###SEPARATOR###' + signature
    compressed_message = zlib.compress(message)

    # Write the compressed message to the file
    with open('./sender_file/compressed_message.txt', 'wb') as f:
        f.write(compressed_message)
        
# Reads the content of the "compressed_message.txt" file and returns it. 
def outputCompressedMessage():
    with open('./sender_file/compressed_message.txt', 'rb') as f:
        return f.read()

if __name__ == "__main__":    
    compressMessage()
    print("Compress successfully.")