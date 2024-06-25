import socket
import os
import sys


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <port>")
    sys.exit(1)

PORT = int(sys.argv[1])
BUFFER_SIZE = 1024


def handle_client(client_socket):
    request = client_socket.recv(BUFFER_SIZE)
    filename = request.decode().split(' ')[1][1:]
    if not os.path.isfile(filename):
        response = b'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'
    else:
        with open(filename, 'rb') as file:
            a = file.read()
            response = b'HTTP/1.1 200 OK\n\n' + a
    print(len(response))
    client_socket.send(response)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", PORT))
    server.listen(5)
    print(f"Listening on port {PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connection from: {addr[0]}:{addr[1]}")
        handle_client(client)


start_server()
