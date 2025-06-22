import sys  # to handle command-line arguments
import os  # to handle file system operations (like walking through folders)
from Cryptodome.Cipher import AES  # to use AES encryption from pycryptodomex
from Cryptodome import Random  # to generate random IV (Initialization Vector)

# Function to encrypt all files inside a directory
def encrypt_dir(path):
    for root, _, files in os.walk(path):  # go through all files in the given directory and its subdirectories
        for file in files:  # loop through each file
            file_path = os.path.join(root, file)  # get full path of the file
            print(file_path + " is encrypting.")  # show which file is being encrypted
            encrypt_file(file_path)  # call the function to encrypt this file

# Function to encrypt a single file
def encrypt_file(path):
    with open(path, "rb") as f:  # open the file in binary mode (important for non-text files)
        plain_text = f.read()  # read all content of the file

    key = b'this is a 16 key'  # encryption key (must be 16, 24, or 32 bytes long for AES)

    iv = Random.new().read(AES.block_size)  # generate a random Initialization Vector (16 bytes)
    mycipher = AES.new(key, AES.MODE_CFB, iv)  # create AES cipher object using CFB mode

    ciphertext = iv + mycipher.encrypt(plain_text)  
    # encrypt the plain text and prepend the IV to the ciphertext (we need IV to decrypt later)

    with open(path + ".bin", "wb") as file_out:  # open a new file to save encrypted content
        file_out.write(ciphertext)  # write the encrypted data into the new file

# This block runs only if the script is executed directly (not when imported)
if __name__ == "__main__":
    if len(sys.argv) < 2:  # check if user provided at least one argument (file or directory path)
        print("Usage: python encrypt.py <path_to_file_or_directory>")  # show usage message
        sys.exit(1)  # exit if no argument was provided

    path = sys.argv[1]  # get the path provided by the user

    if os.path.isdir(path) and os.path.exists(path):  # if it's a valid directory
        encrypt_dir(path)  # encrypt all files inside the directory
    elif os.path.isfile(path) and os.path.exists(path):  # if it's a valid file
        encrypt_file(path)  # encrypt the single file
    else:
        print("It's a special file (socket, FIFO, or device file)")  # handle unsupported file types
