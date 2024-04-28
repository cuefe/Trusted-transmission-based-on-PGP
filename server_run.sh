timer() {
    local start end runtime
    start=$(gdate +%s.%3N)
    "$@"
    end=$(gdate +%s.%3N)
    runtime=$(awk "BEGIN {print $end - $start}")
    echo "$@ : $runtime s."
    echo
}
commands=(
    "python server_receive.py"
    "python decode_compressed_message.py"
    "python decompress.py"
    "python extract_plaintext_and_verify_signature.py"
    "python acknowledge.py"
    "python server_send.py"
)
for cmd in "${commands[@]}"; do
    timer $cmd
done