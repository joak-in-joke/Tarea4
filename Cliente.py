from phe import paillier
import socket
import pickle

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

public_key, private_key = paillier.generate_paillier_keypair()

data_string = pickle.dumps(public_key)

clientsocket.send(data_string)
