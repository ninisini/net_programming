from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("sned mboxId message" or "receive mboxId"): ')    
    if msg == "quit":
        sock.sendto(msg.encode(), ('localhost', port))
        break
    
    sock.sendto(msg.encode(), ('localhost', port))

    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

sock.close()

