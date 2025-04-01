# RabbitMQ/Celery Messaging System

A Python application with Flask, RabbitMQ, and Celery for asynchronous email sending and logging, deployed behind Nginx.

## Features

- 📧 **Email Queueing**: Send emails asynchronously via Celery/RabbitMQ
- ⏱ **Time Logging**: Log current timestamp to a file
- 📜 **Log Viewer**: Access application logs via web endpoint
- 🚀 **Nginx Integration**: Served behind a production-ready web server
- 🌐 **Public Access**: Exposed via tunneling (Ngrok/serveo)

## Prerequisites

- Python 3.8+
- RabbitMQ server
- Nginx
- SMTP credentials (for email functionality)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/RabbitMQ-Messaging-System.git
   cd RabbitMQ-Messaging-System

2. Set up virtual environment:
   ```bash
python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate    # Windowspython -m venv venv

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Configurations

1. Set up environment variables in .env:
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   SMTP_USERNAME=your_email@example.com
   SMTP_PASSWORD=your_password

2. RabbitMQ Setup
   ```bash
   sudo systemctl start rabbitmq-server

## Running The Application

1. Start Celery Worker:
   ```bash
   celery -A tasks worker --loglevel=info

2. Start Flask Application:
   ```bash
   python app.py

3. Configure Nginx (sample config in nginx/ directory)
   ```bash
   ngrok http 5000

## Project Structure

   .
   ├── app.py                     	# Flask application
   ├── tasks.py                   	# Celery tasks
   ├── requirements.txt           	# Dependencies
   ├── nginx/                	  	# Nginx configuration
   │   └── messaging_system.conf
   ├── .env.example          	  	# Environment variables template
   └── /var/log/messaging_system.log    # Generated log file

## Troubleshooting

.  RabbitMQ Not Running:
   ```bash
   sudo systemctl status rabbitmq-server

.  Permission denied for log file:
   ```bash

.  Celery worker not connecting:
   Verify RabbitMQ is running and check broker URL in tasks.py
