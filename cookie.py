from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('setcookie.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        # Get an element from the form
        user = request.form['nm']
        response = make_response(render_template('readcookie.html'))
        response.set_cookie('userID', user)
        return response


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome %s </h1>' % name


if __name__ == '__main__':
    app.debug = True
    app.run()