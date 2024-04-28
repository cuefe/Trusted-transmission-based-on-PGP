import zlib

def decompressFile(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        compressed_data = f_in.read()

        decompressed_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as f_out:
        f_out.write(decompressed_data)

    print("Decompress successfully.")

if __name__ == "__main__":
    input_file = "receiver_file/compressed_message.txt"
    output_file = "receiver_file/decompressed_message.txt"
    decompressFile(input_file, output_file)

