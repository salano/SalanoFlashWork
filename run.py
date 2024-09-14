from flask import Flask, render_template, request, flash
import sqlite3 as sql


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new')
def newStudent():
    return render_template('student1.html')

@app.route('/addstudent', methods=['GET', 'POST'])
def addStudent():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS students (name text, addr TEXT, city TEXT, pin TEXT)")
                cur.execute("insert into students (name, addr, city, pin) \
                             values(?,?,?,?)", (nm, addr, city, pin))
                conn.commit()
                message = "Record added successfully"
        except sql.Error:
            conn.rollback()
            message = "Error in insert operation"
        finally:
            conn.close()
            return render_template('result1.html', message=message)
        
@app.route('/list')
def list():
    try:
        with sql.connect('database.db') as conn:
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute("Select * from students")
            rows = cur.fetchall()
    except sql.Error as e:
        flash("Database error %s :" % e)
    finally:
        conn.close()
        return render_template('list.html', rows=rows)

            
if __name__ == '__main__':
    app.debug = True
    app.run()

