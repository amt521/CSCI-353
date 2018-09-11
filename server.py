import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces

argv=sys.argv[1:len(sys.argv)]
portnum = int(argv[1])
logfile = str(argv[3])
handnum = int(argv[5])

#process logfile
outputFile = open(logfile, "w+")

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print '<DEBUG> Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    outputFile.write("terminating server...")
    outputFile.close()
    sys.exit()
 
# Bind socket to local host and port
try:
    s.bind((HOST, portnum))

    if (argv[1] == ""):
        print("Input information in the form: server.py –p portno –l logfile -h handler")
        outputFile.write("terminating server...")
        outputFile.close()
        sys.exit()
except socket.error , msg:
    print '<DEBUG> Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    outputFile.write("terminating server...")
    outputFile.close()
    sys.exit()
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    sender = d[1].decode('utf8')
    dest = d[2].decode('utf8')
    addr = d[3]
     
    if not data: 
        break

    outputFile.write(sender + " registered from host") 
    reply = '<DEBUG> OK...' + data
     
    s.sendto(reply , addr)
    print '<DEBUG> Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()