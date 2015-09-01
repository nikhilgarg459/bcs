#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide client side access to application.
"""
import socket               

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
sock.connect((TCP_IP, TCP_PORT))
try:
    print sock.recv(1024)     #Welcome to bcs
    recvd = sock.recv(1024)
    sock.send(raw_input(recvd))    #Username nikhil  #From emp.txt
    recvd = sock.recv(1024)
    sock.send(raw_input(recvd))    #Password nikhil   #From emp.txt  
    print sock.recv(1024)
    recvd=sock.recv(1024)
    if recvd == '1':                    #Login Successful   
        while True:
            recvd = sock.recv(1024)     #Get choices
            sock.send(raw_input(recvd)) #Select Choice
            recvd = sock.recv(1024)
            if recvd == '3':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd)) #Create Userid:
                recv = sock.recv(1024)
                sock.send(raw_input(recvd)) #Create Password: 
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Intial money: Rs
                print sock.recv(1024)        #Account added successfully! # Added in custom.txt
            elif recvd == '2':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Userid #Any Userid from custom.txt      
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))   #New Password: 
                print sock.recv(1024)         #Password change successfully! || No user with username #in custom.txt
            elif recvd == '1':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Userid to be deleted: # from custom.txt
                print sock.recv(1024)        #Account deleted successfully!" || User not found in custom.txt
            elif recvd == '4':
                print sock.recv(1024)         #Logout Successful  
                break
            else:
                print sock.recv(1024)         #Wrong Choice!
except Exception, e:
    print e.args                        
finally:    
    sock.close()