import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = 'ohmlotusphoenix@gmail.com'
email_password = 'qppo avrp uulc kvdw'

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_address, email_password)

print("Script executed successfully!")