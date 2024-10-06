from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import smtplib
from dotenv import load_dotenv 
import os

app = Flask(__name__)

app.secret_key = 'your-secret-key-5859'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587

app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your email password


app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    message = request.form['message']
    province = request.form['province']
    contact = request.form['contact']

    # Set a static sender email
    sender_email = 'nisho.org@gmail.com'  # Same email as configured above

    # Compose email
    msg = Message(f"New Message from {province}", sender=sender_email, recipients=['nisho.org@gmail.com'])
    msg.body = f"Contact: {contact}\n\nMessage:\n{message}\n\n{province}"


    try:
        mail.send(msg)
        flash('Message sent successfully!', 'success')

    except Exception as e:
        print(e)
        flash('Failed to send the message. Please try again.', 'error')

    return redirect('/' )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get port from environment or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)           
