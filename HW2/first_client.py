import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send(b'SiEun Lee')
c = sock.recv(1024)
d = int.from_bytes(c, 'big')
print(d)

sock.close()