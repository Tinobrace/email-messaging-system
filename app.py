from flask import Flask, request, send_file
import logging
from datetime import datetime
from tasks import send_mail_task

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='/var/log/messaging_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')
    
    if sendmail:
        send_mail_task.delay(sendmail)
        return "Email queued successfully!"
    
    if talktome:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.info(current_time)
        return "Time logged!"
    
    return "Usage: ?sendmail=email or ?talktome=1"

@app.route('/logs')
def show_logs():
    try:
        return send_file('/var/log/messaging_system.log')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
