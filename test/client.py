import socket
sock = socket.socket()
host = socket.gethostname()
port = 1112

sock.connect((host,port))
print sock.recv(1024)
sock.close
raw_input('name')
