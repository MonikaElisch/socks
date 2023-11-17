## An example of TCP and UDP sockets
### When the client connects to the server, the server prints the IP address and port number of the client. 
1. The client accepts two integers x and y as  input from a user. 
1. The client sends x and y to the server.
1. The server prints an ID and the values x and y  it receives, and computes x + y
1. The server then sends the result back to the client.
1. Upon receiving the result, the client prints an ID, current date and time, and the result.
### TCP
**Server**
+ Bind socket to a (IP, Port)
+ Listen via `listen()`
+ Wait to accept a connection from a client → `accept()`
+ Close connection via `close()`

**Client**
+ Connect to server at (IP, Port) → `connect()`
+ Send request →  `send()`
+ Wait for response → `recv()`
### UDP
**Server**
+ No `listen()`
+ No `accept()`
+ No need `close()`

**Client**
+ No `connect()`
+ Send request →  `sendto()`
+ Wait for response → `recvfrom()`
+ Close socket instead via `close()` 
