from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def readKey():
    with open('key.txt', 'rb') as f:
        key = f.readlines()[0]
    # print(key)
    return key

readKey()

def enc_AES(data: bytes):
    key = str(readKey()).replace('//', '/')
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    print(ciphertext)
    return ciphertext

# def dec_AES(data: bytes())