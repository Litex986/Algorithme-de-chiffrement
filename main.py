import secrets
import time
from argparse import ArgumentParser

from Class import encrypt, decrypt


def argument():
    # Default complexity settings for encryption/decryption
    comp = [2, 2, 2]
    
    # Parsing command-line arguments
    argParser = ArgumentParser()
    argParser.add_argument("-f", "--file", help="File with message")
    argParser.add_argument("-k", "--key", help="Encryption key")
    argParser.add_argument("-m", "--mode", help="Encrypt (E) / Decrypt (D)")
    args = argParser.parse_args()
    
    # Setting the encryption key or generating a random one if not provided
    if args.key:
        KEY = args.key
    else:
        KEY = hex(secrets.randbits(512))[2:]
        print(KEY)
    
    # Checking if a file path is provided
    assert args.file, "Missing file path with --file <path>"
    
    # Reading the message from the specified file
    message = open(args.file, 'r', encoding="utf-8").read()
    
    # Determining the mode (Encrypt or Decrypt)
    mode = 1 if str(args.mode).lower() == 'd' or str(args.mode).lower() == 'decrypt' else 0
    
    # Encryption or decryption process based on the mode
    if mode == 0:  # Encrypt
        time1 = time.time()
        # Breaking the message into chunks of 128 characters
        message = [message[i:i+128] for i in range(0, len(message), 128)]
        
        # Encrypting each chunk of the message using the specified key and complexity settings
        for i in range(len(message)):
            message[i] = encrypt.Encrypt(KEY, message[i], comp)
        
        # Writing the encrypted chunks to a file
        file = open('chiff.txt', 'w', encoding="utf-8")
        file.write('|'.join([i.message for i in message]))  # Writing encrypted messages separated by '|'
        print(round(time.time()-time1, 2), 'sec')  # Printing the time taken for encryption
        
    else:  # Decrypt
        time1 = time.time()
        # Splitting the message by '|' to get individual encrypted chunks
        message = message.split('|')
        
        # Decrypting each chunk of the message using the specified key and complexity settings
        for i in range(len(message)):
            message[i] = decrypt.Decrypt(KEY, message[i], comp)
        
        # Writing the decrypted chunks to a file
        file = open('dechi.txt', 'w', encoding="utf-8")
        file.write(''.join([i.message for i in message]))  # Writing decrypted messages
        print(round(time.time()-time1, 2), 'sec')  # Printing the time taken for decryption

if __name__ == '__main__':
    argument()