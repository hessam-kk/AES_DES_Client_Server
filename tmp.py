from Crypto.Cipher import AES
from conf import filename, key
 
text = b'Hello_World'

print(key, len(key))

cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce

c_t, tag = cipher.encrypt_and_digest(text)

cipher_de = AES.new(key, AES.MODE_EAX)

t = cipher_de.decrypt(c_t)

print(c_t)
print(t.decode('utf-8'))