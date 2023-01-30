from Crypto import Random
from Crypto.Cipher import AES, DES
import os
import os.path


class AES_Encryptor:
    def __init__(self,
                key=b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".AES.enc", 'wb') as fo:
            fo.write(enc)
        return file_name + '.AES.enc'
        # os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open("dec_AES_" + file_name[:-8], 'wb') as fo:
            fo.write(dec)
        # os.remove(file_name)

class DES_Encryptor():
    def __init__(self,
                key=b'S\xa4\xa6eP\xbe\xed\r'):
        self.key = key
    
    def pad(self, s):
        return s + b"\0" * (DES.block_size - len(s) % DES.block_size)
    
    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(DES.block_size)
        cipher = DES.new(key, DES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".DES.enc", 'wb') as fo:
            fo.write(enc)
        return file_name + '.DES.enc'
        # os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:DES.block_size]
        cipher = DES.new(key, DES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[DES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open("dec_DES_" + file_name[:-8], 'wb') as fo:
            fo.write(dec)
        # os.remove(file_name)

    

# enc = DES_Encryptor()
# print(key := Random.get_random_bytes(8))
# x = enc.encrypt(b"HellooooWorld", key)
# print("enc: ", x)

# print(enc.decrypt(x, key))
# enc.encrypt_file('1.jpg')
# enc.decrypt_file('1.jpg.DES.enc')

# enc = AES_Encryptor()
# enc.encrypt_file('1.jpg')
# enc.decrypt_file('1.jpg.AES.enc')


