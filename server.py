from socket import *
import socket

serverName = 'Localhost' #ip
serverPort = 12456 #porta
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('localhost',12456)) #(ip, porta)
print ('-----O SERVIDOR FOI CONECTADO!-----')
while 1:

	num1, clientAddress = serverSocket.recvfrom(2048)
	print 'NUMERO 1 RECEBIDO:', num1

	num2, clientAddress = serverSocket.recvfrom(2048)
	print 'NUMERO 2 RECEBIDO:', num2
	
	num3 = int(num1.decode())*2
	num3 = str(num3)
	serverSocket.sendto(num3.encode(),clientAddress)
	num4 = int(num2.decode())*3
	num4 = str(num4)
	serverSocket.sendto(num4.encode(),clientAddress)
	
	operator, clientAddress = serverSocket.recvfrom(2048)
	print 'OPERADOR RECEBIDO!', operador
	print 'CALCULANDO...'

if str(operador) == '+':
	resposta = int(num1.decode()) + int(num2.decode())
	resposta = str(resposta)
	serverSocket.sendto(resposta.encode(),clientAddress)
elif str(operador) == '-':
	resposta = int(num1.decode()) - int(num2.decode())
	resposta = str(resposta)
	serverSocket.sendto(resposta.encode(),clientAddress)
elif str(operador) == '/':
	resposta = int(num1.decode()) / int(num2.decode())
	resposta = str(resposta)
	serverSocket.sendto(resposta.encode(),clientAddress)
elif str(operador) == '*':
	resposta = int(num1.decode()) * int(num2.decode())
	resposta = str(resposta)
	sererSocket.sendto(resposta.encode(),clientAddress)

serverSocket.close()