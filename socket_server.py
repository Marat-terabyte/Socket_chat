import socket
import threading


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('' , 7777))
server.listen()

users = []


def user_send(data , conn):
    for user in users:
        user.send(data)

        print(user)
        print('\n')
        print(users)


def get_data(conn):
    while True:
        data = conn.recv(2048)

        user_send(data , conn)


def socket_connect(server):
    while True:
        socket_user , addres = server.accept()

        print(f'Connected:{addres}')

        users.append(socket_user)

        socket_user.send('Wait...'.encode())
        socket_user.send('Connect...'.encode())

        thread_get_data = threading.Thread(
        target = get_data ,
        args = {socket_user,})

        thread_get_data.start()


if __name__ == '__main__':
    socket_connect(server)
