import socket
import sys


def get_file(server_host, server_port, filename):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_host, server_port))
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    s.sendall(request.encode())
    response = s.recv(4096 * 32)
    l = len(b'HTTP/1.1 200 OK\n\n')
    with open('uploaded/' + filename, 'wb') as file:
        file.write(response[l:])
    print(f"Uploaded {len(response[l:])} bytes to /uploaded/{filename}")
    s.close()


if __name__ == "__main__":
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    get_file(server_host, server_port, filename)
