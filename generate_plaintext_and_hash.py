import os
import hashlib
import concurrent.futures

# Writes the content of "basical_plaintext.txt" to the "plaintext.txt" file 120000 times.
def writeToFile(basical_plaintext, plaintext):
    for _ in range(1):
        plaintext.write(basical_plaintext)

# Creates a ThreadPoolExecutor and submits the writeToFile function to the executor 8 times.   
def generatePlaintext(basical_plaintext, plaintext):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create 8 threads to write to the file
        # which can be modified according to the machine's CPU
        for _ in range(1):
            executor.submit(writeToFile, basical_plaintext, plaintext)

# Computes the hash value of the "plaintext.txt" file and returns it.
def outputHash():
    sha256_hash = hashlib.sha256()

    with open("./sender_file/plaintext.txt", "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # # TESTCASE 
    # with open("./testcases/hello.txt", "rb") as f:
    #     # Read and update hash string value in blocks of 4K
    #     for byte_block in iter(lambda: f.read(4096), b""):
    #         sha256_hash.update(byte_block)
    

    return sha256_hash.hexdigest()

# Reads the content of the "plaintext.txt" file and returns it.
def outputPlaintext():
    with open("./sender_file/plaintext.txt", "rb") as plaintext:
        return plaintext.read()

    # # TESTCASE    
    # with open("./testcases/hello.txt", "rb", ) as plaintext:
    #     return plaintext.read()
    

if __name__ == "__main__":
    with open("./sender_file/basical_plaintext.txt", "r", encoding='utf-8') as basical_plaintext, open("./sender_file/plaintext.txt", "a", encoding='utf-8') as plaintext:
        generatePlaintext(basical_plaintext.read(), plaintext)

    