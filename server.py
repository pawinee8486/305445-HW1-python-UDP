import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5010
Sum = 1
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "factorial:", factorial(int(data))
    f = str (factorial(int(data)))
    sock.sendto(f,addr)
    
