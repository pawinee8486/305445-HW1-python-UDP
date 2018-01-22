import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5011
##MESSAGE = "Hello, World!"
NUMBER = "5"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", NUMBER

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(NUMBER, (UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "factorial:", data
