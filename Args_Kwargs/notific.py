import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification(*args, **kwargs):
    to_email = kwargs.get('to_email')
    subject = kwargs.get('subject', 'Notification')
    body = kwargs.get('body', 'This is a test notification')
    smtp_server = kwargs.get('smtp_server', 'smtp.gmail.com')  
    smtp_port = kwargs.get('smtp_port', 587)
    smtp_user = kwargs.get('smtp_user')
    smtp_pass = kwargs.get('smtp_pass')

   
    if not all([to_email, smtp_user, smtp_pass]):
        raise ValueError("Missing required SMTP parameters: 'to_email', 'smtp_user' or 'smtp_pass'")

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Защищенное соединение
            server.login(smtp_user, smtp_pass)  # Вход в почтовый аккаунт
            text = msg.as_string()
            server.sendmail(smtp_user, to_email, text)  # Отправка письма
            print(f"Notification sent to {to_email}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_notification(to_email="recipient@example.com", subject="Test", body="This is a test message", smtp_user="you@example.com", smtp_pass="password")
