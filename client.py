import socket   #for sockets
import sys  #for exit
 
argv=sys.argv[1:len(sys.argv)]
ipaddress = argv[1]
portno = argv[3]
logfile = argv[5]
myname = argv[7]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost'
port = 8888
 
continue_check = True 
while(continue_check) :
    msg = raw_input('Enter message to send : ')
     
    try :
        if (msg == 'quit'):
            print("client quit")
            sys.exit()

        #Set the whole string
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()