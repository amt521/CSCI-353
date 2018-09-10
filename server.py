import socket
import sys

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

continueCheck = True
while (continueCheck):
    commandInput = raw_input("")

    # Generate random number in the range of 0 to 10
    #rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 4, we consider the packet lost and do notrespond
    #if rand < 4:
        #serverSocket.sendto(message, address)

    if(commandInput == "exit"):
        print("terminating server…")
