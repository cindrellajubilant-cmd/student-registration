from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page
@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted"
    return render_template('index.html')

# Register student
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    regno = request.form['regno']
    course = request.form['course']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            regno TEXT,
            course TEXT
        )
    ''')

    cursor.execute('INSERT INTO students (name, regno, course) VALUES (?, ?, ?)',
                   (name, regno, course))

    conn.commit()
    conn.close()

    return "Student Registered Successfully!"

if __name__ == '__main__':
    app.run(debug=True)