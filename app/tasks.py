from celery import Celery
from datetime import datetime
from celeryconfig import broker_url, result_backend
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os 

# Configure RabbitMQ and Celery
app = Celery('tasks', broker=broker_url, backend=result_backend)
load_dotenv()

@app.task
def send_email_task(email): 
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    sender_email = os.getenv('GMAIL')
    sender_password = os.getenv('PASSWORD')
    msg = MIMEText("This is the email body")
    msg["Subject"] = "Test Email"
    msg["From"] = sender_email
    msg["To"] = email
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            # server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.send_message(msg)
            # server.sendmail(sender_email, [email], msg.as_string())
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Error sending email to {email}: {e}")

@app.task
def log_time_task():
    with open(os.getenv('FILE-PATH'), "a") as log_file:
        log_file.write(f"Logged time: {datetime.now()}\n") 