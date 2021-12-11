import socket
from socket import *

servername= 'www.khasaktivizm.com' #host that I used
serverport= 12000 #defined port of the server
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientsocket is used for allow the communication 
clientSocket.settimeout(1) #defined communication timeout start from 1

for i in range(10): #my range is max 10
    try: #try block used for if there is any error or not
        myMessagePing = 'PING () '.format(i+1)
        clientSocket.sendto(myMessagePing.encode (), (servername, serverport))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        #this code sample is shows how to do ping with UDP

        
    except:
            print (myMessagePing + ' TIMEOUT')

    else:
        print(ModifiedmyMessagePing.decode()) #encoded clientsocket is decoding here

clientSocket.close() #closing the communication


