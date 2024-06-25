import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

sock.settimeout(1)

for i in range(10):
    try:
        message = f'Ping {i+1} {time.time()}'

        start = time.time()
        sent = sock.sendto(message.encode(), server_address)

        data, server = sock.recvfrom(4096)
        end = time.time()

        rtt = end - start
        print(f'Message: {data.decode()} RTT: {rtt} s')
    except socket.timeout:
        print('Request timed out')

sock.close()
