import argparse
import sys
from cli.interactive import start
from cli.commands import (
    encrypt_command,
    decrypt_command,
)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="aes-gcm-image-cipher",
        description="AES-GCM Image Cipher CLI",
    )
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        help="Encrypt a file (shorthand, use with -f/-p/-o)",
    )
    mode_group.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help="Decrypt a file (shorthand, use with -f/-p/-o)",
    )
    parser.add_argument("-f", "--file", help="Input file path")
    parser.add_argument("-p", "--password", help="Encryption/decryption password")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    subparsers = parser.add_subparsers(dest="command")
    encrypt_parser = subparsers.add_parser(
        "encrypt",
        aliases=["enc"],
        help="Encrypt a file",
    )
    encrypt_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Input file path",
    )
    encrypt_parser.add_argument(
        "-p",
        "--password",
        required=True,
        help="Encryption password",
    )
    encrypt_parser.add_argument(
        "-o",
        "--output",
        default=".",
        help="Output directory",
    )
    decrypt_parser = subparsers.add_parser(
        "decrypt",
        aliases=["dec"],
        help="Decrypt a file",
    )
    decrypt_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Encrypted file path",
    )
    decrypt_parser.add_argument(
        "-p",
        "--password",
        required=True,
        help="Decryption password",
    )
    decrypt_parser.add_argument(
        "-o",
        "--output",
        default=".",
        help="Output directory",
    )
    return parser


def main():
    parser = build_parser()

    if len(sys.argv) == 1:
        start()
        return

    args = parser.parse_args()

    if args.command in ("encrypt", "enc") or args.encrypt:
        if not args.file or not args.password:
            parser.error("-f/--file and -p/--password are required to encrypt.")
        encrypt_command(args)
    elif args.command in ("decrypt", "dec") or args.decrypt:
        if not args.file or not args.password:
            parser.error("-f/--file and -p/--password are required to decrypt.")
        decrypt_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
