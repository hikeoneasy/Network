from socket import *
from datetime import datetime
import os.path
import time

IP = '1.248.223.228'
server_name = 'Easyboan Local PC'
serverPort = 80
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((IP,serverPort))
serverSocket.listen(1)
#연결의 최대 수 
print('The sever is ready to receive!!')



connectionSocket, addr = serverSocket.accept()
while True:
    
    sentence = connectionSocket.recv(1024).decode()
    if not sentence:
        break
    sentence_data = sentence.split()
    if(len(sentence_data) < 4):
        response_data = "{0} 400 Bad Request\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format("HTTP/1.0",  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
        connectionSocket.send(response_data.encode())
        break
    
    request_method = sentence_data[0]
    url = sentence_data[1]
    version = sentence_data[2]
    host = sentence_data[4]
    if(len(sentence_data) > 5):
        data = sentence_data[5]
     
    
    print("I receved ", addr, sentence)
    print("This is method:", request_method)
    print("This is url:", url)
    print("This is version:",version)
    print("This is host:",host)

    file = "C:/Users/easyboan/Desktop/Network_middle"+url
    
   
    if(request_method == 'GET' or request_method == 'HEAD'):
        
        if(os.path.exists(file)):
            atime = time.ctime(os.path.getatime(file))
            if(request_method == 'HEAD'):
                response_data = "{0} 200 OK\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
            else:      
                f = open(file, 'r')
                fileTYPE = os.path.splitext(file)[1]
                lines = f.readlines()
                response_data = "{0} 200 OK\r\nDate: {1}\r\nServer: {2}\r\nLast-Modified: {3}\r\nContent-Type: text/{4}\r\n\r\ndata: {5}".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name, atime, fileTYPE[1:], lines)
                f.close()
        else:
            response_data = "{0} 404 Not Found\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
    elif(request_method == 'POST'):
        if(host == "www.easy.com"):
            if(os.path.exists(file)):
                atime = time.ctime(os.path.getatime(file))
                f = open(file, 'a')
                f.write(data)
                fileTYPE = os.path.splitext(file)[1]
                response_data = "{0} 200 OK\r\nDate: {1}\r\nServer: {2}\r\nLast-Modified: {3}\r\nContent-Type: text/{4}\r\n\r\n ".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name,atime,fileTYPE[1:])
                f.close()
            else:
                f = open(file, 'w')
                f.write(data)
                fileTYPE = os.path.splitext(file)[1]
                atime = time.ctime(os.path.getatime(file))
                response_data = "{0} 200 OK\r\nDate: {1}\r\nServer: {2}\r\nLast-Modified: {3}\r\nContent-Type: text/{4}\r\n\r\n ".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name,atime,fileTYPE[1:])
                f.close()
        else:
            response_data = "{0} 401 Authorization Required\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
    elif(request_method == 'PUT'):
        if(host == "www.easy.com"):
            f = open(file, 'w')
            f.write(data)
            fileTYPE = os.path.splitext(file)[1]
            atime = time.ctime(os.path.getatime(file))
            response_data = "{0} 200 OK\r\nDate: {1}\r\nServer: {2}\r\nLast-Modified: {3}\r\nContent-Type: text{4}\r\n\r\n ".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name,atime,fileTYPE[1:])
            f.close()
        else:
            response_data = "{0} 401 Authorization Required\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
    else:
        response_data = "{0} 405 Method Not Allowed\r\nDate: {1}\r\nServer: {2}\r\n\r\n".format(version,  datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'),server_name)
        
    connectionSocket.send(response_data.encode())
    
    

connectionSocket.close()
serverSocket.close()

print('-end system-')