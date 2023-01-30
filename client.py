import socket
import json
from Crypto.Cipher import AES
import time
from conf import filename, key
from Encryptor import AES_Encryptor

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    #================ AES ==================
    print('Running AES...')
    start_time = time.time()
    # Encrypt file
    enc = AES_Encryptor()
    enc_file_name = enc.encrypt_file(filename)
    
    # Send encrypted data to server
    sock.sendall(open(enc_file_name, 'rb').read())
    print('Sent encrypted file')
    
    elapsed_time = time.time() - start_time
    print("Time elapsed for AES to encrypt and send:", elapsed_time, "seconds")
    #================ AES ==================
    #=======================================
    #================ DES ==================
    


finally:  
    print('Closing connection')  
    sock.close()