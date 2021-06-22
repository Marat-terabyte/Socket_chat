import socket 

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(('127.0.0.1' , 8000)) #localhost

server.listen()
print('Server listen')

while True:
	socket_user , addres = server.accept()

	socket_user.send('You are connected'.encode())

	print(f'User {socket_user} connected ' )

	data = socket_user.recv(2048).decode()

	print(data)