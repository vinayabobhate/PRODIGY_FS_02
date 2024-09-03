from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Database connection
con = mysql.connector.connect(
    host="localhost", user="root", password="Vedeeka17#", database="employee")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile("(0|91)?[7-9][0-9]{9}")


@app.route('/')
def index():
    if 'admin_logged_in' in session:
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # For simplicity, hardcoding admin credentials
        if username == 'admin' and password == 'admin@123':
            session['admin_logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')


@app.route('/admin_logout')
def admin_logout():
    # Add logout logic here, e.g., clearing session data
    return redirect(url_for('login'))

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        post = request.form['post']
        salary = request.form['salary']

        if re.fullmatch(regex, email) and pattern.match(phone):
            cursor = con.cursor()
            cursor.execute(
                'INSERT INTO empdata (Id, Name, Email_Id, Phone_no, Address, Post, Salary) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (id, name, email, phone, address, post, salary))
            con.commit()
            return redirect(url_for('index'))
        else:
            return "Invalid email or phone number. Please try again."
    return render_template('add_employee.html')


@app.route('/display_employees')
def display_employees():
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))

    cursor = con.cursor()
    cursor.execute('SELECT * FROM empdata')
    employees = cursor.fetchall()
    return render_template('display_employees.html', employees=employees)

@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    cursor = con.cursor()
    cursor.execute('DELETE FROM empdata WHERE Id = %s', (id,))
    con.commit()
    return redirect(url_for('display_employees'))

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    cursor = con.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        post = request.form['post']
        salary = request.form['salary']

        cursor.execute('UPDATE empdata SET Name=%s, Email_Id=%s, Phone_no=%s, Address=%s, Post=%s, Salary=%s WHERE Id=%s',
                       (name, email, phone, address, post, salary, id))
        con.commit()
        return redirect(url_for('display_employees'))
    cursor.execute('SELECT * FROM empdata WHERE Id = %s', (id,))
    employee = cursor.fetchone()
    return render_template('edit_employee.html', employee=employee)


if __name__ == '__main__':
    app.run(debug=True)
