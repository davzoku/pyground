import socket

UDP_IP_RECEIVER = '127.0.0.1'
UDP_PORT_RECEIVER = 59332
MESSAGE = 'This is the sample Msg sent'     
#send if right door open

#print on sender terminal
#print "UDP IP Address(Receiver):", UDP_IP_RECEIVER
#print "UDP Port(Receiver):", UDP_PORT_RECEIVER
#print "Message Sent:", MESSAGE
print("run")

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP_RECEIVER, UDP_PORT_RECEIVER))

#AF_INET = Designating IPv4 addresses for communication
#UDP/SOCK_DGRAM = datagram-based protocol