#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide server side access to application.
"""
from bank import Bank
from bank import Account
from config import DB_FILE
import socket
import thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5010

def start(client, addr):
    print "Accepted connection from: ", addr
    try:
        while True:
            response = client.recv(1024)
            msg, parameters = response.split(":")
            obj = Bank(DB_FILE)
            email = None

            if msg == "authenticate":
                email, msg = login(client, obj, parameters)
                if msg != "Login Successful":
                    break
            
            elif msg == "addAccount":
                addAccount(client, obj, parameters)
            
            elif msg =="deleteAccount":
                deleteAccount(client, obj, parameters)    
            
            elif msg == "changePassword":
                changePassword(client, obj, parameters)            
            
            elif msg == "withdraw":
                withdraw(client, obj, parameters)

            elif msg == "deposit":
                withdraw(withdraw, obj, parameters)    
           
            elif msg == "logout":  
                logout(client)
                break

    except Exception,e:
        print e.args
    finally:
        client.close()

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(3)
    while 1:
        client, addr = sock.accept()     # Establish connection with client.
        thread.start_new_thread(start, (client, addr))
    sock.close()


def login(client, obj, parameters):
    email, passw = parameters.split(',')    
    msg, typ = obj.login(email, passw)
    respond(client, str(msg + "," + typ))
    return email, msg
    
def addAccount(client, obj, parameters):
    name, email, password, typ = parameters.split(',')
    msg = obj.addAccount(Account(name, email, password, typ)) 
    respond(client, msg)

def deleteAccount(client, obj, email):
    msg = obj.deleteAccount(email)
    respond(client, msg)

def changePassword(client, obj, parameters):
    email, password = parameters.split(',')
    msg = obj.changePassword(email, password) 
    respond(client, msg)
    

def logout(client):
    respond('Logout Successful')

def deposit(client, obj, email, amoount):
    msg = obj.deposit(email, amount)
    respond(client, msg)

def withdraw(client, obj, email, amoount):
    msg = obj.withDraw(email, amount)
    respond(client, msg)

def respond(client, msg):
    client.send(msg)

connect()
