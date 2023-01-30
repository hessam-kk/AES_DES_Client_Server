import socket
import os
from Crypto.Cipher import AES
from conf import filename, key
from Encryptor import AES_Encryptor
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
    with open('rec_' + filename, 'wb') as f:
        while True:
            data = connection.recv(1024)
            if not data: break
            # write data to a file
            f.write(data)
        print('file recieved!')
        
    enc.decrypt_file('rec_' + filename)
    print('file decrypted!')
    elapsed_time = time.time() - start_time
    print("Time elapsed for AES to recieve and decrypt:", elapsed_time, "seconds")
    #================ AES ==================
    #=======================================
    #================ DES ==================
    


finally:
    # Clean up the connection
    print('Closing connection')  
    connection.close()