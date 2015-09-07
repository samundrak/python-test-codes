import socket

sock =  socket.socket()
host =  socket.gethostname()
port = 1112
sock.bind((host,port))

sock.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thankyou for your connection')
    c.close()
