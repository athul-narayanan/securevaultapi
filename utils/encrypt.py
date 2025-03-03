"""
This python file contains methods to encrypt and decrypt files (AES encryption with 256 bit key)
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from django.conf import settings

key = settings.AES_KEY
blocksize = settings.AES_BLOCK_SIZE

def encrypt_file(data):
    """
    Encrypt the file using AES key
    """

   
    cipher = AES.new(key=key.encode('utf-8'), mode=AES.MODE_CBC)

    padded_data = pad(data, blocksize) # pad the data to match block size
    encrypted_data = cipher.encrypt(padded_data)
    
    return cipher.iv, encrypted_data

def decrypt_file(file_path):
    with open(file_path, 'rb') as file:
        iv = file.read(16)
        encrypted_data = file.read()
    
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(encrypted_data), blocksize) # decrypt the content
    return data
