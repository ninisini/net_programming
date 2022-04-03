from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1234))
s.listen(150)

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        msg = (client.recv(1024).decode())
        Temp = random.randrange(0,41)
        Humid = random.randrange(0,101)
        Iilum = random.randrange(70,151)
        if msg in "quit":
            print('접속종료')
            client.close()
            break

        Temp = str(Temp)
        Humid = str(Humid)
        Iilum = str(Iilum)

        client.send(Temp.encode())
        client.send(Humid.encode())
        client.send(Iilum.encode())


    client.close()





