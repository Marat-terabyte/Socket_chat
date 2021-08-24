import socket
import threading


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('127.0.0.1' , 7777))


def data_decode_and_print():
    while True:
        data = client.recv(2048)
        data = data.decode()

        print(data)


def send_data(message):
    client.send(message)


def main():
    while True:
        nickname = str(input('Input nickename:'))

        if nickname == '':
            return

        else:
            break


    thread_data_decode_and_print = threading.Thread(
    target = data_decode_and_print)

    thread_data_decode_and_print.start()

    while True:
        message = str(input('>>>'))

        if message == '':
            message = str(input('>>>'))

        text = f'{nickname}:{message}'.encode('utf-8')

        send_data(text)


if __name__ == '__main__':
    main()
