from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    return render_template('index.html')

@app.route('/succcess')
def success():
    return 'Logged in successfully'


if __name__ == '__main__':
    app.debug = True
    app.run()