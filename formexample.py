from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = "ANY_STRING_VALUE"


@app.route('/contact', methods=['GET', 'POST'])
def login():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() is False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
