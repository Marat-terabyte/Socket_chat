import socket       #It's module for create a socket
import threading    #It's module for create flow


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((str(input('Input IP addres of server:')), 7777))


def data_decode_and_print():
    '''It's function for decode of get data and print'''
    while True:
        data = client.recv(4096)
        data = data.decode()

        print(data)


def send_data(message):
    '''It's function for send data'''
    message = message.encode('utf-8')
    client.send(message)


def main():
    '''It's function for connect to a server'''
    while True:
        nickname = str(input('Input nickename:'))

        if nickname == '':
            continue
        else:
            break

    thread_data_decode_and_print = threading.Thread(target=data_decode_and_print)
    thread_data_decode_and_print.start()

    while True:
        message = str(input('>>>'))

        if message == '':
            continue
        else:
            text = f'{nickname}:{message}'
            send_data(text)


if __name__ == '__main__':
    main()
