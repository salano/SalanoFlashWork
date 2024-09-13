from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)
app.secret_key = 'RANDOM_STRING'


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' or \
            request.form['password'] == 'admin':
            error = 'Invalid username or Password. Please try again'
        else:
            flash('You were successfully logged in.')
            flash('Log out before login in  again.')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=error)


if __name__ == '__main__':
    app.debug = True
    app.run()