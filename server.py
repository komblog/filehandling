import socket, os

PORT = 4000
BUFF = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(10)

def create(conn):
    fo = open(namafile,'w')
    mes = "OK"
    fo.close()
    return mes

def delete(conn):
    os.remove(namafile)
    mes = "OK"
    return mes

def read(conn):
    fo = open(namafile,'r')
    text = fo.read(BUFF)
    return text

print "menunggu koneksi..."
while True:
    conn, addr = s.accept()
    print "Terhubung dengan ",addr

    data = conn.recv(BUFF)
    command = data.split()
    namafile = command[1]
    balas = ""
    if command[0] == "new":
        reply = create(conn)
    elif command[0] == "del":
        reply = delete(conn)
    elif command[0] == "read":
        reply = read(conn)
    balas+=reply
    conn.send(reply)