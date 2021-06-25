import socket
import threading


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect((input(str('Введите IP адрес хоста:')) , 8000))
print(str('Введите ник'))
nickname = input('...')
print(f'Добро пожаловать , {nickname}')


def listen_server():
	while True:
		data = client.recv(2048)
		print(data.decode('utf-8'))



def start_client():
	listen_thread = threading.Thread(target = listen_server)
	listen_thread.start()
	while True:
		client.send(input(nickname + ':').encode('utf-8'))



if __name__ == '__main__':
	start_client()