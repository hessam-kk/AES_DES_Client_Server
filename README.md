# AES_DES_Client_Server
A project to compare AES &amp; DES encrypting and decypting performance for various file sizes, in both client &amp; server

## Config & run
First of all, you need to change the `conf.py` file and put the desired file name in the variable. Please note that file should be in the
root folder of the project or you need to put the exact address for it. Also, you may want to change the key, which is accessible from file `Encryptor.py`.

After editing the configs, then you need to run the server by `python server.py` in Windows, or `python3 server.py` in Linux. then if it started succesfully,
you can start the client to start encrypting and transfering file, which needs to run `python `client.py` in Windows or `python3 client.py` in Linux.

After running both files, the file will begin to encrypt by client, while it's done, it would be transfered by the socket and port where have opened before.
The server will recieve the encrypted file, save it and then start to decrypt it. while its decryption is finished, it will save the raw file in the root folder.

## Requirements
* Python3
* Crypto Package: `pip install pycryptodome`
