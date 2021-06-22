import socket

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(('127.0.0.1' , 8000))

while True:
	data = client.recv(2048)
	print(data.decode())
	
	client.send(input('...').encode())