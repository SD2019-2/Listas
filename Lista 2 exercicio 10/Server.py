# -*- coding: utf-8 -*-
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
dict = {}
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client = data.split()
        if from_client[0] == '1':
            dict={from_client[1]:[from_client[2],from_client[3]]}
            conn.send('Dados registrados com sucesso!!')
        else:
            if from_client[1] in dict:
                resp = dict[from_client[1]]
                conn.send(resp[0]+ ' ' +resp[1])
                break
            else:
                conn.send('Email não localizado!')
    conn.close()
    print ('Cliente desconectado')
