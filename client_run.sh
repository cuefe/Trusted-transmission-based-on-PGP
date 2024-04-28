rm ./sender_file/plaintext.txt

timer() {
    local start end runtime
    start=$(date +%s.%3N)
    "$@"
    end=$(date +%s.%3N)
    runtime=$(awk "BEGIN {print $end - $start}")
    echo "$@ : ${runtime}s."
    echo
}

commands=(
    "python generate_plaintext_and_hash.py"

    # Not necessary for Unix user
    "dos2unix ./sender_file/plaintext.txt"
    
    "python compress_message_and_signature.py"
    "python encode_compressed_message.py"
    "python client_send.py"
    "python client_receive.py"
    "python verify_acknowledgement.py"
)

for cmd in "${commands[@]}"; do
    timer $cmd
done