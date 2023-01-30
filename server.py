import socket
import os
from Crypto.Cipher import AES
from conf import filename, key
from Encryptor import AES_Encryptor, DES_Encryptor
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()

try:
    print('connection from', client_address)

    #================ AES ==================    
    start_time = time.time()

    enc = AES_Encryptor()
    # Receive the data in small chunks 
    with open('rec_' + filename+ '.AES.enc', 'wb') as f:
        while True:
            data = connection.recv(1024)
            if not data: break
            # write data to a file
            f.write(data)
        print('AES file recieved!')
        
    enc.decrypt_file('rec_' + filename + '.AES.enc')
    print('AES file decrypted!')
    elapsed_time = time.time() - start_time
    print("--- Time elapsed for AES to recieve and decrypt:", elapsed_time, "seconds")
    #================ AES ==================
    #=======================================
    # Get a new connection
    print('=' * 20)
    connection, client_address = sock.accept()
    print('=' * 20)
    #=======================================
    #================ DES ==================
    start_time = time.time()

    des_enc = DES_Encryptor()
    # Receive the data in small chunks 
    filename_to_dec = 'rec_' + filename + '.DES.enc'
    with open(filename_to_dec, 'wb') as f:
        while True:
            data = connection.recv(1024)
            if not data: break
            # write data to a file
            f.write(data)
        print('DES file recieved!')
    
    # print(filename_to_dec := 'rec_' + filename + '.DES.enc')
    des_enc.decrypt_file(filename_to_dec)
    print('DES file decrypted!')
    elapsed_time = time.time() - start_time
    print("--- Time elapsed for DES to recieve and decrypt:", elapsed_time, "seconds")
    #================ DES ==================
    
finally:
    # Clean up the connection
    print('Closing connection')  
    connection.close()