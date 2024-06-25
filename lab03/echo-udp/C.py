import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

sock.settimeout(1)

rtts = []
lost_packets = 0
total_packets = 10

for i in range(total_packets):
    try:
        message = f'Ping {i+1} {time.time()}'

        start = time.time()
        sent = sock.sendto(message.encode(), server_address)

        data, server = sock.recvfrom(4096)
        end = time.time()

        rtt = end - start
        rtts.append(rtt)
        print(f'Message: {data.decode()} RTT: {rtt} s')
    except socket.timeout:
        print('Request timed out')
        lost_packets += 1


if rtts:
    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts) / len(rtts)
    loss_rate = (lost_packets / total_packets) * 100

    print(f'\n--- ping statistics ---')
    print(f'{total_packets} packets transmitted, {total_packets - lost_packets} received, {loss_rate}% packet loss')
    print(f'rtt min/avg/max = {min_rtt:.3f}/{avg_rtt:.3f}/{max_rtt:.3f} ms')

sock.close()
