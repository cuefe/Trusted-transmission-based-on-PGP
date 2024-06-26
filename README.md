# Introduction
Crypto is a simple encryption and decryption project that uses RSA and SHA256
algorithms to encrypt and decrypt messages. It also uses zlib to compress and
decompress messages. The tool is written in Python and is compatible with 
Python 3.10 and above.

This project is finished by *Kaisuping*, *Cuefe* and *Faith*.

# Usage
Before use, add permissions to the shell scripts:
- `chmod u+x local_run.sh`
- `chmod u+x client_run.sh`
- `chmod u+x server_run.sh`

If you want to test this on a local machine, 
    run `./local_run.sh`

![Reference](show.gif)

If you want to test this in client/server mode:
1. In the server, run `./server_run.sh`
2. In the client, run `./client_run.sh`

We use port **5001** as the default port for both server and client in TCP communication.
Make sure it has opened before running the script above. And change the IP address in 
the `client_send.py` according to your requirement.

# Algorithms
- Hash: sha256
- Compress: zlib
- Signature: rsa, 2048bits
- Symmetric encryption: AES, 256bits

# File structure
```
├── acknowledge.py
├── build_Docker.sh
├── client_receive.py
├── client_run.sh
├── client_send.py
├── compress_message_and_signature.py
├── decode_compressed_message.py
├── decompress.py
├── encode_compressed_message.py
├── extract_plaintext_and_verify_signature.py
├── generate_plaintext_and_hash.py
├── local_run.sh
├── README.md
├── receiver_file
│   ├── pk_receiver.pem
│   ├── pk_sender.pem
│   └── sk_receiver.pem
├── sender_file
│   ├── basical_plaintext.txt
│   ├── pk_receiver.pem
│   ├── pk_sender.pem
│   └── sk_sender.pem
├── server_receive.py
├── server_run.sh
├── server_send.py
├── sign_hash.py
├── testcases
│   └── hello.txt
└── verify_acknowledgement.py

4 directories, 26 files
