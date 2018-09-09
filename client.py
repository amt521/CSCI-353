import socket
import sys
 
# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
host = 'localhost'
 
# define the communication port
portNum = raw_input("Enter Port Number: ")
print("You entered: ", portNum)
 
# Connect the socket to the port where the server is listening
server_address = ((host, portNum))
 
print("connecting")
 
stream_socket.connect(server_address)
print("client1# connected to server and registered")
 
# Send data
message = 'message'
stream_socket.sendall(message)
 
# response
data = stream_socket.recv(10)
print(data) 
 
print('socket closed')
stream_socket.close()