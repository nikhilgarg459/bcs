#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide client side access to application.
"""
import socket               
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5008
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
sock.connect((TCP_IP, TCP_PORT))
try:
    print sock.recv(1024)     #Welcome to bcs
    recvd = sock.recv(1024)
    sock.send(raw_input(recvd))    #Username nikhil  #From emp.txt
    time.sleep(1)
    recvd = sock.recv(1024)
    sock.send(raw_input(recvd))    #Password nikhil   #From emp.txt  
    time.sleep(1)
    print sock.recv(1024)
    recvd = sock.recv(1024)
    if recvd == '1':                    #Login Successful   
        while True:
            recvd = sock.recv(1024)     #Get choices
            sock.send(raw_input(recvd)) #Select Choice
            time.sleep(1)
            recvd = sock.recv(1024)
            if recvd == '4':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd)) #Create Userid:
                time.sleep(1)
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd)) #Create Password: 
                time.sleep(1)
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Intial money: Rs
                time.sleep(1)
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Intial money: Rs
                time.sleep(1)
                print sock.recv(1024)        #Account added successfully! # Added in custom.txt
            elif recvd == '2':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Userid #Any Userid from custom.txt      
                time.sleep(1)
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))   #New Password: 
                time.sleep(1)
                print sock.recv(1024)         #Password change successfully! || No user with username #in custom.txt
            elif recvd == '1':
                recvd = sock.recv(1024)
                sock.send(raw_input(recvd))  #Userid to be deleted: # from custom.txt  #Enter amount:
                time.sleep(1)
                print sock.recv(1024)        #Account deleted successfully!" || User not found in custom.txt
            elif recvd == '6':
                print sock.recv(1024)         #Logout Successful  #Check Balance
                break
            else:
                print sock.recv(1024)         #Wrong Choice!
    
except Exception, e:
    print e.args                        
finally:    
    sock.close()
