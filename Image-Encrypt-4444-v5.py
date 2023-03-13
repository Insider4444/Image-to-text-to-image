import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.style import Style


BLOCK_SIZE = 16
KEY_SIZE = 32


def get_aes_key():
    key = Prompt.ask("Enter [bold green underline]Encryption[/] Key")
    return key


def get_aes_key_bytes(key):
    key_bytes = key.encode('utf-8')
    key_bytes_padded = key_bytes.ljust(KEY_SIZE, b'\0')
    return key_bytes_padded


def encrypt_image(filename, key):
    key_bytes = get_aes_key_bytes(key)
    iv = os.urandom(BLOCK_SIZE)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    with open(filename, "rb") as f:
        image_data = f.read()
    encrypted_data = iv + cipher.encrypt(pad(image_data, BLOCK_SIZE))
    with Progress(
        TextColumn("[bold green]Encrypting"), BarColumn(), TextColumn("[progress]"), console=console
    ) as progress:
        task = progress.add_task("[bold green]Encrypting image...", total=len(encrypted_data), start=False)
        with open(f"{os.path.splitext(filename)[0]}.txt", "wb") as f:
            for i in range(0, len(encrypted_data), BLOCK_SIZE):
                chunk = encrypted_data[i:i+BLOCK_SIZE]
                f.write(chunk)
                progress.update(task, advance=len(chunk))
    console.print(Panel(Text("Image encrypted and saved as text file.", style="bold green")))


def decrypt_text(filename, key):
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    key_bytes = get_aes_key_bytes(key)
    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data[BLOCK_SIZE:]), BLOCK_SIZE)
        with Progress(
            TextColumn("[bold green]Decrypting"), BarColumn(), TextColumn("[progress]"), console=console
        ) as progress:
            task = progress.add_task("[bold green]Decrypting image...", total=len(decrypted_data), start=False)
            with open(f"{os.path.splitext(filename)[0]}.jpg", "wb") as f:
                for i in range(0, len(decrypted_data), BLOCK_SIZE):
                    chunk = decrypted_data[i:i+BLOCK_SIZE]
                    f.write(chunk)
                    progress.update(task, advance=len(chunk))
        console.print(Panel(Text("Image decrypted and saved as JPEG file.", style="bold green")))
        return True
    except ValueError:
        console.print(Panel(Text("Error: Incorrect key entered. Please try again.", style="bold red")))
        return False


console = Console()
progress = Progress(
    "[progress.description]{task.description}",
    BarColumn(),
    "[progress.percentage]{task.percentage:>3.0f}%",
    TimeRemainingColumn(),
) 



def display_menu():
    console.print("="*50, style="bold yellow")
    console.print(" " * 10 + "IMAGE ENCRYPTION/DECRYPTION TOOL", style="bold yellow")
    console.print(" " * 15 + "BY TEAM 4444 & CP6E", style="bold red")
    console.print("="*50, style="bold yellow")
    console.print("Choose an option:", style="cyan")
    console.print("1. Encrypt an image", style="cyan")
    console.print("2. Decrypt an image", style="cyan")
    console.print("3. Exit", style="cyan")
    console.print("="*50, style="bold yellow")


def main():
    while True:
        console.clear()
        display_menu()
        choice = Prompt.ask("Enter your choice (1-3):", choices=["1", "2", "3"])
        if choice == '1':
            filename = Prompt.ask("Enter image filename (with extension)", default="")
            filename = filename.strip("\"'")
            key = get_aes_key()
            encrypt_image(filename, key)
            input("Press Enter to continue...")
        elif choice == '2':
            filename = Prompt.ask("Enter encrypted image filename (with extension)", default="")
            filename = filename.strip("\"'")
            while True:
                key = Prompt.ask("Enter key", password=True, default="")
                if decrypt_text(filename, key):
                    input("Press Enter to continue...")
                    break
        elif choice == '3':
            console.clear()
            console.print("Thanks for using our tool", style="bold red")
            console.print("4444 & CP6E", style="cyan")
            names = ["P Bhargav Sai - 20751A3340", "M Lakshmi kanth - 20751A3334", "U Mukesh - 20751A3355", "S Mohammed Khadeer - 20751A3351"]
            panel = Panel(Text("\n".join(names), style=Style.parse('cyan bold'), justify='left'), title=Text("Project Made by", style=Style(bgcolor='red', color='white')), width=50)
            console.print(panel)
            break
        else:
            input("Invalid choice. Press Enter to continue...")


if __name__ == '__main__':
    main()
