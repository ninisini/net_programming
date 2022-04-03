from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 5678))
sock.listen(150)

while True:
    client, addr = sock.accept()
    print('connection from ', addr)
    while True:
        msg = (client.recv(1024).decode())
        Heartbeat = random.randrange(40,141)
        Steps = random.randrange(2000,6001)
        Cal = random.randrange(1000,4001)
        if msg in "quit":
            print('접속종료')
            client.close()
            break

        Heartbeat = str(Heartbeat)
        Steps = str(Steps)
        Cal = str(Cal)

        client.send(Heartbeat.encode())
        client.send(Steps.encode())
        client.send(Cal.encode())


    client.close()
