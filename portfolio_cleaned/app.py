from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key')

# Flask-Mail configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME', 'himansirajgor11@gmail.com'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD', 'wdfv mmzf ouls vdiy'),  # Gmail App Password
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_USERNAME', 'himansirajgor11@gmail.com')
)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            try:
                msg = Message(
                    subject='New Contact Form Submission',
                    recipients=[app.config['MAIL_USERNAME']],
                    body=f'''
New message received:

From: {name} <{email}>
Message: {message}
Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    '''
                )
                mail.send(msg)
                flash('Thank you for your message!', 'success')
            except Exception as e:
                flash(f'Failed to send message: {str(e)}', 'error')

            return redirect(url_for('contact'))
        else:
            flash('Please fill out all fields.', 'error')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
