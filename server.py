#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide server side access to application.
"""
from employee import Employee
import socket               

sock = socket.socket()         
host = socket.gethostname() 
port = 12344               
sock.bind((host, port))        

sock.listen(5)                
client, addr = sock.accept()     # Establish connection with client.
print 'Got connection from', addr
client.send('Welcome to bcs')
client.send('Username: ') #nikhil
user = client.recv(1024)
client.send('Password: ')	#nikhil
passw = client.recv(1024)
with open ("emp.txt", "r") as myfile:
	data = myfile.read()
	attribs = data.split(' ')
	if(user == attribs[0] and passw == attribs[1]):
		client.send('Login successful!')
		client.send('1')
		empl = Employee(user,passw)
		while True:
			client.send('1 Add new Account\n2 Delete Account\n3 Change Password\n4 Logout\nPlease enter ypur choice: ')
			choice = client.recv(1024)
			if choice == '1':
				client.send('3')
				client.send('Create Userid: ')
				username = client.recv(1024)
				client.send("Create Password: ")
				password = client.recv(1024)
				client.send("Intial money: Rs")
				money = client.recv(1024)
				client.send(empl.add_Account(username,password,money))
			elif choice == '2':
				client.send('1')
				client.send('Userid to be deleted: ')
				username = client.recv(1024)
				client.send(empl.delete_Account(username))
			elif choice == '3':
				client.send('2')
				client.send('Userid: ')
				username = client.recv(1024)
				client.send("New Password: ")
				password = client.recv(1024)
				client.send(empl.change_Password(username,password))
			elif choice =='4':
				client.send('4')
				client.send('Logout Successful')
				break
			else:
				client.send('5')
				client.send("Wrong Choice!")				
	else:	
		client.send('Wrong username or password!')
		client.send('0')
client.close()    
sock.close()
  