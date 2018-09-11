import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
argv=sys.argv[1:len(sys.argv)]
portnum = int(argv[1])
logfile = str(argv[3])
handnum = argv[5]

#process logfile
outputFile = open(logfile, "w+")

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    outputFile.write("terminating server...")
    outputFile.close()
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    outputFile.write("terminating server...")
    outputFile.close()
    sys.exit()
     
print 'Socket bind complete'
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    outputFile.write(addr + " registered from host") 
    reply = 'OK...' + data
     
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()