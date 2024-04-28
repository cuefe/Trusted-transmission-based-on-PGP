rm ./sender_file/plaintext.txt

timer() {
    local start end runtime
    start=$(date +%s.%3N)
    "$@"
    end=$(date +%s.%3N)
    runtime=$(awk "BEGIN {print $end - $start}")
    echo "$@ : $runtime s."
    echo
}

commands=(
    "python generate_plaintext_and_hash.py" 
    "dos2unix sender_file/plaintext.txt"          
    "python compress_message_and_signature.py"
    "python encode_compressed_message.py"
    "cp sender_file/encrypted_message_and_symmetric_key.txt receiver_file/encrypted_message_and_symmetric_key.txt"
    "python decode_compressed_message.py"
    "python decompress.py"
    "python extract_plaintext_and_verify_signature.py"

    "python acknowledge.py"
    "cp receiver_file/encrypted_hash_value.txt sender_file/encrypted_hash_value.txt"
    "python verify_acknowledgement.py"
)

for cmd in "${commands[@]}"; do
    timer $cmd
done