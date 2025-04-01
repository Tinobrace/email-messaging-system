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

    msg = MIMEText(f""" 
    Dear Val,

    DevOps engineering is a discipline that combines software development (Dev) and IT operations (Ops) 
    to enable faster, more efficient software delivery. It emphasizes automation, continuous integration, 
    and deployment (CI/CD) to streamline workflows and reduce human errors.

    DevOps engineers work with tools like Docker, Kubernetes, Jenkins, and Terraform to automate infrastructure 
    provisioning and manage scalable deployments. Their goal is to foster collaboration between development and 
    operations teams, breaking down silos to improve software reliability.

    Security is also a key aspect, with DevSecOps ensuring that security practices are embedded in every stage 
    of development. By using monitoring and observability tools, teams can quickly identify and fix issues, 
    ensuring high availability and performance.

    DevOps is not just about tools—it’s a culture of continuous improvement, collaboration, and efficiency.
    """)
    msg['Subject'] = 'Understanding DevOps Engineering!'
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
