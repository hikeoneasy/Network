
from socket import *

serverName = '1.248.223.228'
severPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName ,severPort))



clientSocket.sendall('DELETE /1.txt HTTP/1.0\r\nHost: www.easy.com\r\nI_WANA_APPLE\r\n\r\n'.encode())



#clientSocket.sendall('POST /2.txt HTTP/1.0\r\nHost: www.easy.com\r\nILOVESAMSUNG\r\n\r\n'.encode())
#clientSocket.sendall('HEAD /1.txt HTTP/1.0\r\nHost: www.easy.com\r\n\r\n'.encode())
#clientSocket.sendall('GET /4.txt HTTP/1.0\r\nHost: www.easy.com\r\n\r\n'.encode())
#clientSocket.sendall('POST /5.txt HTTP/1.0\r\nHost: www.easy.com\r\nI_WANA_APPLE\r\n\r\n'.encode())
#clientSocket.sendall('PUT /1.txt HTTP/1.0\r\nHost: www.hard.com\r\nI_WANA_APPLE\r\n\r\n'.encode())


#clientSocket.sendall('\r\n\r\n'.encode())

modifiedSentence = clientSocket.recv(1024)


print(modifiedSentence.decode())

clientSocket.close()

