from flask import Flask, url_for, redirect, request
app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome(name):
    return 'Hello %s ' % name


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get['nm']
        return redirect(url_for('welcome', name=user))


if __name__ == '__main__':
    app.debug = True
    app.run()