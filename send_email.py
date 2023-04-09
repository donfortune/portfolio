import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'xxxxxxxx@gmail.com'
    password = 'xxxxxxx'
    receiver_email = 'xxxxxxxxxx@gmail.com'

    context = ssl.create_default_context()  # secure context for sending emails securely
    with smtplib.SMTP_SSL(host, port, context=context) as file:
        file.login(username, password)
        file.sendmail(username, receiver_email, message)




