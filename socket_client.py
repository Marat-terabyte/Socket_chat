import socket
import threading

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(('127.0.0.1' , 8000))


def listen_server():
	while True:
		data = client.recv(2048)
		print(data.decode())



def start_client():
	listen_thread = threading.Thread(target = listen_server)
	listen_thread.start()
	while True:
		client.send(input('...').encode())



if __name__ == '__main__':
	start_client()