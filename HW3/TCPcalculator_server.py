from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        a = (client.recv(1024).decode())
        if a in 'q':
            client.close()
            break
        
        b = a.split()        
        first = b[0]
        first = int(first) 
        op = b[1]
        second = b[2]
        second = int(second)

        if op == "+":
            rsp = first + second
        elif op == "-":
            rsp = first - second
        elif op == "*":
            rsp = first * second
        elif op == "/":
            rsp = first / second
            rsp = round(rsp, 1)

        rsp = str(rsp)
        client.send(rsp.encode())

    client.close()



