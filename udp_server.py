import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), 25661))
print('Waiting for connection...')
while True:
        x, sender_addr = server.recvfrom(1024)
        x =x.decode('ascii')
        print ("6488185: server recieved from:",sender_addr ,"with data" ,x)
        sum =int(x[0])+int(x[2])
        server.sendto(repr(sum).encode('ascii'),(socket.gethostname(),25661))
        server.close()
server.close()

