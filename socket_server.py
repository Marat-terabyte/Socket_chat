import socket       #It's module for create a socket
import threading    #It's module for create flow


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(('', 7777))
SERVER.listen()

USERS = []


def user_send(data):
    '''It's function for send data for users'''
    for user in USERS:
        user.send(data)


def get_data(conn):
    '''It's function for get data'''
    while True:
        data = conn.recv(2048)
        user_send(data)


def socket_connect():
    '''It's function for connect users to a server and create for them a flow'''
    while True:
        socket_user, addres = SERVER.accept()

        print(f'Connected:{addres}')

        USERS.append(socket_user)

        socket_user.send('Wait...'.encode())
        socket_user.send('Connect...'.encode())

        thread_get_data = threading.Thread(target=get_data, args={socket_user,})
        thread_get_data.start()


if __name__ == '__main__':
    socket_connect()
