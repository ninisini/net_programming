from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    # 웹 서버 코드 작성
    reqa = req[0]
    reqb = reqa.split( )
    print(reqb)
    reqc = reqb[1]
    filename = reqc.replace("/","")
    print(filename)
    
    if filename == "index.html":
        f = open(filename,'r', encoding='utf-8')
        mimeType = 'text/html'

        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data.encode('euc-kr'))
        
    elif filename == "iot.png":
        f = open(filename, 'rb')
        mimeType = 'image/png'
    
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data)
    
    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
    
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data)

    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())
        
    # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
    c.close()