from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('jobs.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS jobs
                  (id INTEGER PRIMARY KEY, company TEXT,
                   role TEXT, status TEXT, date TEXT)''')
    db.commit()

@app.route('/')
def index():
    db = get_db()
    jobs = db.execute('SELECT * FROM jobs ORDER BY id DESC').fetchall()
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        db = get_db()
        db.execute('INSERT INTO jobs (company,role,status,date) VALUES (?,?,?,?)',
                   (request.form['company'], request.form['role'],
                    request.form['status'], request.form['date']))
        db.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        db = get_db()
        db.execute('UPDATE jobs SET status=? WHERE id=?',
                   (request.form['status'], id))
        db.commit()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=5000)