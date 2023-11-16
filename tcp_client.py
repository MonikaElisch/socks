import time
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect((socket.gethostname(), 20231))
x, y =input("Enter two numbers: ").split()
client.send(x.encode('ascii'))
client.send(y.encode('ascii'))
data = client.recv(1024)
print ("6488185: ", time.asctime()," ",data.decode('ascii'))
client.close()
