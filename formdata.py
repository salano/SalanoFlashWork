from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def student():
    return render_template('student.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        # Get all the data from the form
        result = request.form
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()