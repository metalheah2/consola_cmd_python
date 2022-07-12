#Autor    : Marco Jhoel Churata Torres
#Archivo  : Cliente_socket
#Fecha    : 12/07/1999

import socket

my_socket=socket.socket()
my_socket.connect(('192.168.0.16',8000))

while(1):
	comando=input("Comando : ")
	my_socket.send(comando.encode('UTF-8'))
my_socket.close()
