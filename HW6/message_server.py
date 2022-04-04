from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

dic = {}

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    msg = msg.split(maxsplit=2)

    if msg[0] == "send":
        if msg[1] not in dic.keys(): 
            dic[msg[1]] = []
        dic[msg[1]].append(msg[2])
        
        rsp = str('OK')
        sock.sendto(rsp.encode(), addr)

    elif msg[0] == "receive":
        if msg[1] not in dic.keys() or not dic[msg[1]]:
            sock.sendto("No messages".encode(),addr)
        else:
            sock.sendto(dic[msg[1]].pop(0).encode(),addr)

    elif msg[0] == "quit":
        break
        
sock.close()
