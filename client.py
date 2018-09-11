import socket   #for sockets
import sys  #for exit
 
argv=sys.argv[1:len(sys.argv)]
ipaddress = str(argv[1])
portnum = int(argv[3])
logfile = str(argv[5])
myname = argv[7]

if (argv == None):
    print("Input information in the form: client.py –s serverIP –p portno –l logfile –n myname")
    sys.exit()

#process logfile
outputFile = open(logfile, "w")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    outputFile.write("terminating client...")
    outputFile.close()
    sys.exit()
 
host = ipaddress
 
continue_check = True 
while(continue_check) :
    msg = raw_input('Enter message to send : ')
     
    try :
        if (msg == 'exit'):
            outputFile.write("terminating client...")
            outputFile.close()
            sys.exit()

        #Set the whole string
        s.sendto(msg, (host, portnum))
        outputFile.write("connecting to the server " + host + " at port " + portnum)
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        outputFile.write("terminating client...")
        outputFile.close()
        sys.exit()