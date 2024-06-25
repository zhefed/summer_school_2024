import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_address, subject, body, format='plain'):
    message = MIMEMultipart()
    message['From'] = 'ilon@tesla.ru'
    message['To'] = receiver_address
    message['Subject'] = subject

    message.attach(MIMEText(body, format))

    try:
        mailer = smtplib.SMTP('mail.spbu.ru', 25)
        mailer.sendmail('ilon@tesla.ru', receiver_address, message.as_string())
        print("Mail Sent")
    except Exception as e:
       raise e


send_email('matros@citata30.ru', 'Car takeaway', 'Hey! Grab red tesla car from space!')
send_email('matros@citata30.ru', 'Car takeaway with img', '<h1>Hey! Grab red tesla car from space!</h1><img src="https://i.pinimg.com/originals/70/59/2d/70592df26a776b7d229be670b58c80b3.jpg"></img>', 'html')
