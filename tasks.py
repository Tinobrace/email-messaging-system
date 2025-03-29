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

    ## msg = MIMEText(f"Mr. Val, this is a Test email specially sent to you at {datetime.now()} for your perusal")
    msg = MIMEText(f"Dear Val,\n\n"
        "We hope this email finds you well.\n"
        "Thank you for being a valued part of our community.\n"
        "We wanted to share some exciting updates with you.\n"
        "Stay tuned for upcoming features and improvements.\n"
        "Your feedback helps us improve our services.\n"
        "Feel free to reach out with any suggestions.\n"
        "We appreciate your continued support.\n"
        "Have a great day!\n"
        "Best regards,\nSterling Bank Technology Team!\n\n {datetime.now()}")
    msg['Subject'] = 'Sterling Bank Cares!'
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
