from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'RANDOM_STRING'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id',db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    addr = db.Column(db.String(200))
    city = db.Column(db.String(50))
    pin = db.Column(db.String(10))

    def __init__(self, name, addr, city, pin):
        self.name = name
        self.addr = addr
        self.city = city
        self.pin = pin 


@app.route('/')
def show_all():
    return render_template('show_all.html', students=students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] \
            or not request.form['addr']:
            flash('Please enter all fields!', 'error')
        else:
            student = students(
                request.form['name'],
                request.form['addr'],
                request.form['city'],
                request.form['pin']
            )
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added.')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    app.debug = True
    with app.app_context():
        db.create_all()
    app.run()