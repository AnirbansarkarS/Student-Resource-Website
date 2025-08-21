from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="password",  # your MySQL password
    database="college_db" # your database name
)
cursor = db.cursor()

# Home route
@app.route('/')
def home():
    return render_template('index.html')   # frontend HTML

# Example route for syllabus page
@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html')

# Example route for notes page
@app.route('/notes')
def notes():
    return render_template('notes.html')

# Example route for PYQ page
@app.route('/pyq')
def pyq():
    return render_template('pyq.html')

# Example: Saving feedback form data into MySQL
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        query = "INSERT INTO feedback (name, message) VALUES (%s, %s)"
        values = (name, message)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('home'))
    
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
