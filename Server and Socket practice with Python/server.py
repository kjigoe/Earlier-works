####Written by Kevin Igoe####

#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('10.114.173.204', 8765))
serverSocket.listen(1)

while True:
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    print 'connected from', addr
    try:
        message = connectionSocket.recv(1024)
        filename = message.split() [1]
        print filename
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print 'File Received'
    except IOError:
        print 'IOError'
        connectionSocket.send('Error 404: Not Found')
        connectionSocket.close()
serverSocket.close()
    
