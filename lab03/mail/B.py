import socket


def send_email_smtp_socket(smtp_server, sender_email, receiver_email, subject, message_body):
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

    s.send(f"From: {sender_email}\r\nTo: {receiver_email}\r\nSubject: {subject}\r\n\r\n{message_body}\r\n.\r\n".encode())
    print(s.recv(1024).decode())

    s.send(b"QUIT\r\n")
    print(s.recv(1024).decode())

    s.close()


send_email_smtp_socket("mail.spbu.ru", "ilon@spacex.ru", "matros@citata30.ru",
                       "SpaceX invite", "Let's go to mars!")

"""
220 mail.spbu.ru ESMTP CommuniGate Pro 6.3.20 is glad to see you!

250 mail.spbu.ru your name is not citata30.ru

250 ilon@spacex.ru sender accepted

250 matros@citata30.ru accepting mail from a client address

354 Enter mail, end with "." on a line by itself

250 12654454 message accepted for delivery
"""
