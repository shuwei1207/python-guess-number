# -*- coding: utf-8 -*-
import socket
import struct

if __name__ == '__main__' :
    low = 0
    high = 1001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('140.113.73.36', 8899))
    
    message = s.recv(1024)[2:].decode()
    
    while(message != "correct" and message != "fail"):
        if message == 'higher':
            low = int( (low + high) / 2 )
        elif message == 'lower':
            high = int( (low + high) / 2 )
        num = str(int( (low + high) / 2 )).encode()
        s.send(struct.pack("!H", len(num)))
        s.send(num)
        message = s.recv(1024)[2:].decode()
        print(num,low,high,message)
    
    s.close()