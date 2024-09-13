from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '*****************'
app.config['MAIL_PASSWORD'] = 'potatobus1981'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    message = Message('Hello', sender='salanosullivan@gmail.com', recipients=['salano_cs@hotmail.com'])
    message.body = "Hello Flask! This message is sent from Flask-Mail"
    mail.send(message)
    return 'Message Sent'


if __name__ == '__main__':
    app.debug = True
    app.run()