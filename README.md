## An example of TCP and UDP sockets
### When the client connects to the server, the server prints the IP address and port number of the client. 
1. The client accepts two integers x and y as  input from a user. 
1. The client sends x and y to the server.
1. The server prints an ID and the values x and y  it receives, and computes x + y
1. The server then sends the result back to the client.
1. Upon receiving the result, the client prints an ID, current date and time, and the result.
###TCP
**Server**
_Bind socket to a (IP, Port)
_Listen via `listen()`
_Wait to accept a connection from a client → `accept()`
_Close connection via `close()` 
**Client**
_Connect to server at (IP, Port) → `connect()`
_Send request →  `send()`
_Wait for response → `recv()`
###UDP
**Server**
_No `listen()`
_No `accept()`
_No need `close()`
**Client**
_No `connect()`
_Send request →  `sendto()`
_Wait for response → `recvfrom()`
_Close socket instead via `close()` 
