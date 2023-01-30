import socket
import os
from Crypto.Cipher import AES
from conf import filename, key
from Encryptor import Encryptor


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
  enc = Encryptor()
  
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

finally:
    # Clean up the connection
    print('Closing connection')  
    connection.close()