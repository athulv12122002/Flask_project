from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def validate_login(email, password):
    connection = sqlite3.connect("user_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    connection.close()
    return user is not None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if validate_login(email, password):
            return render_template('home.html')  # Redirect to home or dashboard after successful login
        else:
            return 'Invalid credentials, please try again.'

    return render_template('login.html')

@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Connect to the database and insert new user
        with sqlite3.connect('user_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, email, password) VALUES (?, ?, ?)
            ''', (name, email, password))
            conn.commit()

            return redirect(url_for('login'))

    return render_template('create_account.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')  # Ensure you have a home.html template

if __name__ == '__main__':
    app.run(debug=True)
