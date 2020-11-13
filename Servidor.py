from phe import paillier
import socket
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(4096)
    data_variable = pickle.loads(buf)
    if len(buf) > 0:
        print(data_variable)
        public_key = data_variable
        file1 = open('new_archivo_1', 'r') 
        Lines = file1.readlines() 

        file2 = open('cifrado_1', 'w') 

        for line in Lines: 
            file2.writelines(str(public_key.encrypt(line))+"\n")


        file2.close() 
    break