# -*- coding: utf-8 -*-
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
mensagem = input('Informe o endereço: ')
client.send('2 '+mensagem)
recebe = client.recv(4096)
client.close()
cont2 = 2
if recebe != 'Email não localizado!':
    recebe = recebe.split()
    client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest =(recebe[0], int(recebe[1]))
    mensagem2 = input('Informe a mensagem a ser enviada:')
    client2.sendto(mensagem2,dest)
    client2.close()
else:
    print(recebe)
