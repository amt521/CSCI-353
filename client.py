import socket
import sys
 
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define variables
host = 'localhost'
# define the communication port
portNum = raw_input("Enter Port Number: ")
print("You entered: ", portNum)

message = raw_input("Enter Message: ")
 
# Connect the socket to the port where the server is listening
server_address = ((host, portNum))
 
print("connecting")
 
client_socket.connect(server_address)
print("client1# connected to server and registered")
 
# Send data
client_socket.sendall(message)
 
# response
data = client_socket.recv(10)
print(data) 
 
print('socket closed')
client_socket.close()