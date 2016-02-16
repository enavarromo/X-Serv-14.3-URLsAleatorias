#!/usr/bin/python
import socket
import random


# -------------- Port Set Up --------------
host = socket.gethostname()
port = 1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#mySocket.bind(('localhost', 1234))  # Socket LoopBack
mySocket.bind((host, port))  # Socket LoopBack Host
#mySocket.bind(('192.168.1.132', 1234))  # Socket wlan0 inet addr:192.168.1.132
mySocket.listen(2) # 5 TPC Cons cap


try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        # -------------- Plot Socket Info --------------
        print 'HTTP request received from: '+ str(address)
        print recvSocket.recv(1024)
        if address[0] == '127.0.0.1':
            print "Coming from Loopback"
            # -------------- HTTP to LoopBack --------------
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Hello World!</h1>" +
                            "You came from LoopBack at IP: " +
                            str(address[0]) + 
                            " and Port: " + str(address[1]) +
                            " Your random is: " + str(random.randint) +
                            "</body></html>\r\n")
        else:
            # -------------- HTTP to ext --------------
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Hello World!</h1>" +
                            "<p>You are at IP: " + str(address[0]) +
                            " and Port: " +  str(address[1]) + "</p>" +
                            "<a href=http://"+host+":"+str(port)+"/"+
                            str(random.randint(1, 1000))+">enlace</a>"
                            "</body></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
    print("\nExiting Ok")
    
    
    
    
    
