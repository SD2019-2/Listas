
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
            if from_client[2] != 'masculino':
	    	if 21 < int(from_client[3]):
            		conn.send('maior de idade')
		else:
            		conn.send('menor de idade')
 	    else:
		
	    	if 18 < int(from_client[3]):
            		conn.send('maior de idade')
		else:
            		conn.send('menor de idade')
        
    conn.close()
    print ('Cliente desconectado')


