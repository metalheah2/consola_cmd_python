#Autor    : Marco Jhoel Churata Torres.
#Archivo  : Servidor_socket
#Fecha    : 12/07/2022

import socket
import os
 
my_socket=socket.socket()
my_socket.bind(('192.168.0.16',8000))
my_socket.listen(5)
 
while True:
	conexion,addr=my_socket.accept()
	print("Conectado ¡¡")
	opcion=input('Iniciar consola ? y/n ')
	while(opcion=='y'):
		comando_recv=conexion.recv(1024)
		comando_deco=comando_recv.decode('UTF-8')
		comando=str(comando_deco)
		os.system(comando)
conexion.close()
