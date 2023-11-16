import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), 20231))
print('Waiting for connection...')
server.listen(5)

while True:
        client, addr = server.accept()
        print('Received a connection from %s' % str(addr))
        data = client.recv(1024)
        x,y = data.decode('ascii')
        print ("6488185: server recieved:",x,y)
        sum =int(x)+int(y)
        client.send(repr(sum).encode('ascii'))
        client.close()
server.close()
