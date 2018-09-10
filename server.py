import socket
import sys

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
initalInput = raw_input("").join(sys.argv[1:])


# Assign IP address and port number to socket
server_socket.bind(('', 12000))

continueCheck = True
while (continueCheck):
    initialInput = raw_input("").join(sys.argv[1:])
    if (len(initialInput.len) > 4 and "client" in initialInput):
        portno = initialInput[initialInput.find("-p") +3 : initialInput.find("-p") +7]
        logfile = initialInput[initialInput.find("-l") +3 : initialInput.find(".txt") + 4]
        log_file = open(logfile, "w")
        myname = initialInput[initialInput.find("-h") +3] 
    
    #if client is terminated
    if ("exit" in initialInput) :
        server_socket.close()
        log_file.write("terminating server…")
        log_file.close()
        continueInput = False

    # Generate random number in the range of 0 to 10
    #rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = server_socket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 4, we consider the packet lost and do notrespond
    #if rand < 4:
        #server_socket.sendto(message, address)
