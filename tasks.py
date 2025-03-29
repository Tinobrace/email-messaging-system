from celery import Celery
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_mail_task(email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'valen.uchenna@gmail.com'
    smtp_pass = 'iflu vqen naad dlba'  # Use an app-specific password

    msg = MIMEText(f"Test email sent at {datetime.now()}")
    msg['Subject'] = 'Test Email For You, Val!'
    msg['From'] = smtp_user
    msg['To'] = email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        return f"Email sent to {email}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
