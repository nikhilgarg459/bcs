#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide server side access to application.
"""
from employee import Employee
import socket    
import time
import thread           
	
def start(client, addr):
    print "Accepted connection from: ", addr
    try:
		client.send('Welcome to bcs')
		time.sleep(1)
		client.send('Username: ') #nikhil
		time.sleep(1)
		user = client.recv(1024)
		client.send('Password: ')	#nikhil
		time.sleep(1)
		passw = client.recv(1024)
		with open ("emp.txt", "r") as myfile:
			data = myfile.read()
			attribs = data.split(' ')
			if(user == attribs[0] and passw == attribs[1]):
				client.send('Login successful!')
				time.sleep(1)
				client.send('1')
				time.sleep(1)
				empl = Employee(user, passw)
				while True:
					client.send('1 Add new Account\n2 Delete Account\n3 Change Password\n4 Logout\nPlease enter ypur choice: ')
					time.sleep(1)
					choice = client.recv(1024)
					if choice == '1':
						client.send('3')
						time.sleep(1)
						client.send('Create Userid: ')
						time.sleep(1)
						username = client.recv(1024)
						client.send("Create Password: ")
						time.sleep(1)
						password = client.recv(1024)
						client.send("Intial money: Rs")
						time.sleep(1)
						money = client.recv(1024)
						client.send(empl.add_Account(username, password, money))
						time.sleep(1)
					elif choice == '2':
						client.send('1')
						time.sleep(1)
						client.send('Userid to be deleted: ')
						time.sleep(1)
						username = client.recv(1024)
						client.send(empl.delete_Account(username))
						time.sleep(1)
					elif choice == '3':
						client.send('2')
						time.sleep(1)
						client.send('Userid: ')
						time.sleep(1)
						username = client.recv(1024)
						client.send("New Password: ")
						time.sleep(1)
						password = client.recv(1024)
						client.send(empl.change_Password(username, password))
						time.sleep(1)
					elif choice == '4':
						client.send('4')
						time.sleep(1)
						client.send('Logout Successful')
						time.sleep(1)
						break
					else:
						client.send('5')
						time.sleep(1)
						client.send("Wrong Choice!")
						time.sleep(1)				
			else:	
				client.send('Wrong username or password!')
				time.sleep(1)
				client.send('0')
				time.sleep(1)
    except Exception,e:
        print e.args 
    finally:			
        client.close()    

TCP_IP = '127.0.0.1'
TCP_PORT = 5006
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
sock.bind((TCP_IP, TCP_PORT))
sock.listen(3)

while 1:
	client, addr = sock.accept()     # Establish connection with client.
	thread.start_new_thread(start, (client, addr))
sock.close()
  