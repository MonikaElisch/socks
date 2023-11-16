import time
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
port =25661
x  =input("Enter two numbers: ")
client.sendto(x.encode('ascii'), (socket.gethostname(),port))
data = client.recvfrom(1024).decode('ascii')
print ("6488185: ", time.asctime()," ",data.decode('ascii'))
client.close()
