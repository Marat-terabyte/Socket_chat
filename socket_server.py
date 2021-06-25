import socket 
import threading

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


server.bind( (input(str('Введите свой IP адрес:')) , 8000) )

server.listen()
print('Server listen...')

users = []


def send_all(data):
	for user in users:
		user.send(data)


def listen_user(user):
	while True:
		data = user.recv(2048)
		print(f'User {data}')

		send_all(data)


def start_server():
	while True:
		socket_user , addres = server.accept()

		socket_user.send('Conect...'.encode('utf-8'))
		socket_user.send('You are connected...'.encode('utf-8'))

		print(f'User {addres[0]} connected ')

		users.append(socket_user)

		listen_accept_user = threading.Thread(
			target = listen_user , 
			args = (socket_user,)
			)

		listen_accept_user.start()


if __name__ == '__main__':
	start_server()

#поток Main