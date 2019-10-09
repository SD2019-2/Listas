# -*- coding: utf-8 -*-
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
mensagem = input('Informe o endereço, o ip  e a porta: ')
client.send('1 '+mensagem)
recebe = client.recv(4096)
client.close()
print recebe

host = '127.0.0.1'
port = 7000
addr = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(addr)
conn, addr = client.recvfrom(1024)
print ("aguardando mensagem")
print ('Mensagem recebida: '+ conn)
client.close()
