import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), 25661))
print('Waiting for connection...')
while True:
        data, sender_addr = server.recvfrom(1024)
        data =data.decode('ascii')
        print ("6488185: server recieved from:",sender_addr ,"with data" ,data)
        x= int(data[0])
        y= int(data[2])
        sum =x+y
        server.sendto(repr(sum).encode('ascii'),(sender_addr))
        #server.close
