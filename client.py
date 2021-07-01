from socket import * 
import socket

serverName = 'Localhost'
serverport = 12456
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'IP Alvo: ', serverName
print 'Porta Alvo:', serverport
print '\n'


num1 = raw_input ('Digite o primeiro numero: ')
num2 = raw_input ('Digite o segundo numero: ')
operador = raw_input ('Selecione um operador: (+ / * -) ')



clientSocket.sendto(num1.encode(),(serverName,serverport))
clientSocket.sendto(num2.encode(),(serverName,serverport))
clientSocket.sendto(operador.encode(),(serverName,serverport))


num3,serverAddress = clientSocket.recvfrom(2048)
print 'Sent back number 3: ', num3
num4,serverAddress = clientSocket.recvfrom(2048)
print 'Number4  send back: ', num4
answer,serverAddress = clientSocket.recvfrom(2048)
print 'RESULTADO: ', resposta

clientSocket.close()