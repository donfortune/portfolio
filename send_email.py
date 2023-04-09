import smtplib
import ssl

host = "smtp.gmail.com"
port = 465



username = 'xxxxxxx@gmail.com'
password = '12345678'

receiver_email = 'xxxxxxxx@gmail.com'
message = """\
Subject:Letter! 
hello world
"""

context = ssl.create_default_context()  #secure context for sending emails securely

with smtplib.SMTP_SSL(host, port, context=context) as file:
    file.login(username, password)
    file.sendmail(username, receiver_email, message)
