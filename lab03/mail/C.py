import socket
import base64


def send_email_smtp_socket(smtp_server, sender_email, receiver_email, subject, message_body, image_path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((smtp_server, 25))

    s.send(f"HELO citata30.ru\r\n".encode())
    print(s.recv(1024).decode())

    s.send(f"MAIL FROM:<{sender_email}>\r\n".encode())
    print(s.recv(1024).decode())

    s.send(f"RCPT TO:<{receiver_email}>\r\n".encode())
    print(s.recv(1024).decode())

    s.send(b"DATA\r\n")
    print(s.recv(1024).decode())

    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    s.send(f"From: {sender_email}\r\n".encode())
    s.send(f"To: {receiver_email}\r\n".encode())
    s.send(f"Subject: {subject}\r\n".encode())
    s.send(b"MIME-Version: 1.0\r\n")
    s.send(b"Content-Type: multipart/mixed; boundary=frontier\r\n\r\n")
    s.send(b"--frontier\r\n")
    s.send(b"Content-Type: text/plain\r\n\r\n")
    s.send(f"{message_body}\r\n".encode())
    s.send(b"--frontier\r\n")
    s.send(b"Content-Type: image/jpeg\r\n")
    s.send(b"Content-Transfer-Encoding: base64\r\n\r\n")
    s.send(f"{encoded_image}\r\n".encode())
    s.send(b"--frontier--\r\n.\r\n")
    print(s.recv(1024).decode())

    s.send(b"QUIT\r\n")
    print(s.recv(1024).decode())

    s.close()


send_email_smtp_socket("mail.spbu.ru", "ilon@spacex.ru", "matros@citata30.ru",
                       "Test Subject", "This is a test email.", "./../images/car-small.jpeg")
