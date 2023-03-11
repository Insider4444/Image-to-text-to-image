import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from termcolor import colored
from os import system, name

BLOCK_SIZE = 16
KEY_SIZE = 32

def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_aes_key():
    key = input("Enter encryption key: ")
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
    with open(f"{os.path.splitext(filename)[0]}.txt", "wb") as f:
        f.write(encrypted_data)
    print(colored("Image encrypted and saved as text file.", "green"))

def decrypt_text(filename, key):
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    key_bytes = get_aes_key_bytes(key)
    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data[BLOCK_SIZE:]), BLOCK_SIZE)
        with open(f"{os.path.splitext(filename)[0]}.jpg", "wb") as f:
            f.write(decrypted_data)
        print(colored("Image decrypted and saved as JPEG file.", "green"))
    except ValueError:
        print(colored("Error: Incorrect key entered. Please try again.", "red"))

def display_menu():
    clear()
    print(colored("="*50, "yellow"))
    print(colored(" "*10 + "IMAGE ENCRYPTION/DECRYPTION TOOL", "yellow"))
    print(colored(" "*15 + "BY TEAM 4444 & CP6E", "red"))
    print(colored("="*50, "yellow"))
    print(colored("Choose an option:", "cyan"))
    print(colored("1. Encrypt an image", "cyan"))
    print(colored("2. Decrypt an image", "cyan"))
    print(colored("3. Exit", "cyan"))
    print(colored("="*50, "yellow"))

def main():
    while True:
        display_menu()
        choice = input(colored("Enter your choice (1-3): ", "green"))
        if choice == '1':
            filename = input(colored("Enter image filename (with extension): ", "green"))
            key = get_aes_key()
            encrypt_image(filename, key)
            input(colored("Press Enter to continue...", "cyan"))
        elif choice == '2':
            filename = input(colored("Enter encrypted image filename (with extension): ", "green"))
            key = input(colored("Enter key: ", "green"))
            decrypt_text(filename, key)
            input(colored("Press Enter to continue...", "cyan"))
        elif choice == '3':
            clear()
            print(colored("Exiting program.", "red"))
            break
        else:
            input(colored("Invalid choice. Press Enter to continue...", "red"))

if __name__ == '__main__':
    main()
