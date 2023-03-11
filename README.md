# Image Encryption/Decryption Tool

This is a command-line tool written in Python for encrypting and decrypting images using the Advanced Encryption Standard (AES) algorithm. The tool uses the `Cryptodome` library for AES encryption and the `tqdm` library for progress bars.

## Features

- Encrypts an image file using a user-provided encryption key.
- Decrypts an encrypted image file using the correct encryption key.
- Displays progress bars during encryption and decryption.

## Requirements

- Python 3.x
- Cryptodome library (`pip install pycryptodomex`)
- tqdm library (`pip install tqdm`)
- termcolor library (`pip install termcolor`)

## Usage

1. Clone the repository to your local machine.
2. Install the required libraries using the `requirements.txt` file: `pip install -r requirements.txt`.
3. Navigate to the repository directory in your terminal or command prompt.
4. Run the `Image-Encrypt-4444-v4.py` file: `python Image-Encrypt-4444-v4.py`.

## Code Explanation

The following is a brief explanation of the code:

- The `get_aes_key()` function prompts the user to enter an encryption key, which is used for both encryption and decryption.
- The `get_aes_key_bytes(key)` function converts the encryption key string to bytes and pads it to the required length for AES encryption.
- The `encrypt_image(filename, key)` function reads the image data from the specified file, encrypts it using AES encryption with a randomly generated initialization vector (IV), and saves the encrypted data to a text file with the same name as the original image file.
- The `decrypt_text(filename, key)` function reads the encrypted data from the specified text file, decrypts it using the correct encryption key and IV, and saves the decrypted data to a JPEG file with the same name as the original image file.
- The `display_menu()` function displays a simple menu for the user to choose between encrypting an image, decrypting an image, or exiting the tool.
- The `main()` function is the entry point for the program and handles user input to call the appropriate functions.

## Credits

This tool was created by Team 4444 and CP6E as part of a Mini project @SITAMS
Made By
- [@Insider4444](https://www.github.com/Insider4444)
- M Lakhsmi Kanth
- U Mukesh
- S Mohammed Khadeer

