#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide server side access to application.
"""
from bank import Bank
from bank import Account
import socket
import thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5010

def start(client, addr):
    print "Accepted connection from: ", addr
    try:
        email = None
        while True:
            response = client.recv(1024)
            msg, params = response.split(":")
            parameters = getParam(params)

            if msg == "authenticate":
                email, msg = login(client, parameters)
                if msg != "Login Successful":
                    break
            
            elif msg == "addAccount":
                addAccount(client, parameters)
            
            elif msg =="deleteAccount":
                deleteAccount(client, parameters)    
            
            elif msg == "changePassword":
                changePassword(client, parameters)            
            
            elif msg == "withdraw":
                withdraw(client, email, parameters)

            elif msg == "deposit":
                deposit(client, email, parameters)    
           
            elif msg == "logout":  
                logout(client)
                break

    except Exception,e:
        print e.args
    finally:
        client.close()

def getParam(params):
    parameters = dict()
    if params != "":
        paramArray = params.split(',')
        for param in paramArray:
            key, value = param.split('=')
            parameters[key] = value
        return parameters

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(3)
    while 1:
        client, addr = sock.accept()     # Establish connection with client.
        thread.start_new_thread(start, (client, addr))
    sock.close()


def login(client, parameters):    
    msg, typ = Bank().login(parameters['email'],parameters['password'])
    respond(client, msg, str("type=" + typ))
    return parameters['email'], msg
    
def addAccount(client, parameters):
    msg = Bank().addAccount(Account(parameters['name'], parameters['email'], parameters['password'], parameters['type'])) 
    respond(client, msg, "")

def deleteAccount(client, parameters):
    msg = Bank().deleteAccount(parameters['email'])
    respond(client, msg, "")

def changePassword(client, parameters):
    msg = Bank().changePassword(parameters['email'], parameters['password']) 
    respond(client, msg, "")
    

def logout(client):
    respond(client, "Logout Successful", "")

def deposit(client, email, parameters):
    msg = Bank().deposit(email, parameters['amount'])
    respond(client, msg, "")

def withdraw(client, email, parameters):
    msg = Bank().withDraw(email, parameters['amount'])
    respond(client, msg, "")

def respond(client, msg, parameters):
    client.send(str(msg + ":" + parameters))

connect()
