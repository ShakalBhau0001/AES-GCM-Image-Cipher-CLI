from core.crypto import encrypt_file, decrypt_file
from cli.display import (
    print_success,
    print_error,
    print_info,
)


def encrypt_command(args):
    try:
        print_info("Encrypting file...")
        output = encrypt_file(
            src_path=args.file,
            password=args.password,
            out_dir=args.output,
            progress_cb=lambda pct: None,
            log_cb=print_info,
        )
        print_success(f"Encrypted file saved:\n{output}")
    except Exception as e:
        print_error(str(e))


def decrypt_command(args):
    try:
        print_info("Decrypting file...")
        output = decrypt_file(
            src_path=args.file,
            password=args.password,
            out_dir=args.output,
            progress_cb=lambda pct: None,
            log_cb=print_info,
        )
        print_success(f"Decrypted file saved:\n{output}")
    except Exception as e:
        print_error(str(e))
