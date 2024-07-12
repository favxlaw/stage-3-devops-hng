import smtplib
import logging
from datetime import datetime

def send_email(email):
    try:
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "your_email@example.com"
        sender_password = "your_password"

        message = f"Subject: Test Email\n\nThis is a test email to {email}."

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
            print(f"Email sent to {email}")

    except Exception as e:
        print(f"Failed to send email: {e}")

def log_time():
    try:
        log_file = '/var/log/messaging_system.log'
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info(f"Current time: {datetime.now()}")
        print("Time logged")

    except Exception as e:
        print(f"Failed to log time: {e}")
