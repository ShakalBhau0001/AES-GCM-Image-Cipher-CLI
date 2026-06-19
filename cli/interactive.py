from rich.prompt import Prompt
from rich.prompt import IntPrompt
from core.crypto import encrypt_file, decrypt_file
from cli.display import (
    show_banner,
    print_success,
    print_error,
)


def start():
    show_banner()

    while True:
        print()
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        print()

        choice = IntPrompt.ask(
            "Select an option",
            choices=["1", "2", "3"],
        )

        try:
            if choice == 1:
                file_path = Prompt.ask("Enter file path")
                password = Prompt.ask(
                    "Enter password",
                    password=True,
                )
                output_dir = Prompt.ask("Output directory", default=".")
                result = encrypt_file(
                    src_path=file_path,
                    password=password,
                    out_dir=output_dir,
                    progress_cb=lambda pct: None,
                    log_cb=print_success,
                )
                print_success(f"Encrypted file saved:\n{result}")
            elif choice == 2:
                file_path = Prompt.ask("Enter file path")
                password = Prompt.ask(
                    "Enter password",
                    password=True,
                )
                output_dir = Prompt.ask("Output directory", default=".")
                result = decrypt_file(
                    src_path=file_path,
                    password=password,
                    out_dir=output_dir,
                    progress_cb=lambda pct: None,
                    log_cb=print_success,
                )
                print_success(f"Decrypted file saved:\n{result}")
            else:
                print_success("See You Later !")
                break
        except KeyboardInterrupt:
            print()
            print_error("Operation cancelled.")
            break
        except Exception as e:
            print_error(str(e))
