import socket
import sys
 
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

continueInput = True

while (continueInput):
    initialInput = raw_input("").join(sys.argv[1:])
    if (len(initialInput.len) > 4 and "client" in initialInput):
        serverIP = initialInput[initialInput.find("-s") +3 : initialInput.find("-p") -2]
        portno = initialInput[initialInput.find("-p") +3 : initialInput.find("-p") +7]
        logfile = initialInput[initialInput.find("-l") +3 : initialInput.find(".txt") + 4]
        log_file = open(logfile, "w")
        myname = initialInput[initialInput.find("-h") +3]
    
    #if client is terminated
    if ("exit" in initialInput) :
        client_socket.close()
        log_file.write("terminating client…")
        log_file.close()
        continueInput = False

    
    # Define variables
    host = raw_input("#Enter Host Number: ")
    print("#You entered: ", host)

    message = raw_input("#Enter Message: ")
    print("#You entered: ", message)
    
    # Connect the socket to the port where the server is listening
    server_address = ((host, portno))
    
    print("#connecting")
    
    client_socket.connect(server_address)
    print("#client1# connected to server and registered")
    
    # Send data
    client_socket.sendall(message)
    
    # response
    data = client_socket.recv(10)
    
    print('socket closed')
    client_socket.close()