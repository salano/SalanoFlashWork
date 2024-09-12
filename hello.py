from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Salano'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name


if __name__ == '__main__':
    app.debug = True
    app.run()
