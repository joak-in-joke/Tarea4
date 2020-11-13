from phe import paillier
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

public_key, private_key = paillier.generate_paillier_keypair()

clientsocket.send(bytes(public_key))

encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
[private_key.decrypt(x) for x in encrypted_number_list]