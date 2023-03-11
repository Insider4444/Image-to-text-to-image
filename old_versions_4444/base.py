import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = 16
KEY_SIZE = 32

def get_aes_key():
    key = input("Enter encryption key: ")
    return key

def get_aes_key_bytes(key):
    return key.encode('utf-8').rjust(KEY_SIZE, b'\0')

def encrypt_image(filename, key):
    key_bytes = get_aes_key_bytes(key)
    iv = os.urandom(BLOCK_SIZE)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    with open(filename, "rb") as f:
        image_data = f.read()
    encrypted_data = iv + cipher.encrypt(pad(image_data, BLOCK_SIZE))
    with open(f"{os.path.splitext(filename)[0]}.bin", "wb") as f:
        f.write(encrypted_data)
    print("Image encrypted and saved as binary file.")

def decrypt_text(filename, key):
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    key_bytes = get_aes_key_bytes(key)
    iv = encrypted_data[:BLOCK_SIZE]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[BLOCK_SIZE:]), BLOCK_SIZE)
    with open(f"{os.path.splitext(filename)[0]}.jpg", "wb") as f:
        f.write(decrypted_data)
    print("Image decrypted and saved as JPEG file.")

def main():
    choice = input("Enter 'E' to encrypt an image or 'D' to decrypt a text: ")
    if choice.lower() == 'e':
        filename = input("Enter image filename (with extension): ")
        key = get_aes_key()
        encrypt_image(filename, key)
    elif choice.lower() == 'd':
        filename = input("Enter encrypted text filename (with extension): ")
        key = input("Enter key: ")
        decrypt_text(filename, key)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == '__main__':
    main()
