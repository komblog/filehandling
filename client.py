import socket

PORT = 4000
BUFF = 1000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', PORT))

command = raw_input("Command : ")
c.send(command)
reply = c.recv(BUFF)
print "Status : ",reply
c.close()