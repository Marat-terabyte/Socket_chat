import socket
import threading


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect((input(str('Введите IP адрес хоста:')) , 8000))

def listen_server():
	while True:
		data = client.recv(2048).decode()
		#print(data)



def start_client():
	listen_thread = threading.Thread(target = listen_server)
	listen_thread.start()

	while True:
		client.send(input('::::').encode())


if __name__ == '__main__':
	start_client()