
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
            if from_client[2] != 'programador':
	    	salario=float(from_client[3]) * 0.20 + float(from_client[3])
            	conn.send(str(salario))
 	    else:
		salario=float(from_client[3]) * 0.18 + float(from_client[3])
            	conn.send(str(salario))
        
    conn.close()
    print ('Cliente desconectado')
