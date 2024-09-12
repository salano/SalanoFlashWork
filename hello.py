from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Salano'

@app.route('/home')
def home():
    return render_template('hello.html')


# Hello parameter route
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name


if __name__ == '__main__':
    app.debug = True
    app.run()
