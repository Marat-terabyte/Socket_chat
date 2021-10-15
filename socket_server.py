import time         #It's mudule for work with time
import socket       #It's module for create a socket
import threading    #It's module for create flow

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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

        local_time_on_server = time.localtime()

        print(f'Connected:{addres}')
        USERS.append(socket_user)

        socket_user.send(f'Connect...\nTime:{time.ctime()}'.encode())

        username = socket_user.recv(4096)
        user_send(f'\n[{local_time_on_server.tm_hour}:{local_time_on_server.tm_min}:{local_time_on_server.tm_sec}] SERVER:Join {username}'.encode())

        thread_get_data = threading.Thread(target=get_data, args={socket_user,})
        thread_get_data.start()


if __name__ == '__main__':
    socket_connect()
