#client 
import socket
s=socket.socket()
port=12345
s.connect(('10.3.141.1',port))
print s.recv(1024)
s.close()
