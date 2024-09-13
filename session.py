from flask import Flask, session, redirect, url_for, render_template, request
app = Flask(__name__)
app.secret_key ="ANY_STRING_VALUE"


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+ username + ' </br>' + \
        "<b> <a href='/logout'>Click here to log out </a> </b>"
    return 'Your are not logged in  </br>' + \
        "<b> <a href='/login'>Click here to log in </a> </b>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()