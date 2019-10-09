
# -*- coding: utf-8 -*-
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
mensagem = input('Nome Sexo e idade: ')
client.send('1 '+mensagem)
recebe = client.recv(4096)
client.close()
print recebe

