from flask import Flask, request, render_template, redirect, url_for, session, Response
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'thesecretsecretkey'
app.config['SESSION_COOKIE_NAME'] = 'sessionID'

def init_db():
    db_path = os.path.join(os.getcwd(), 'database.db')
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')

        cursor.executemany('''
            INSERT INTO users (username, password) VALUES (?, ?);
        ''', [
            ('admin', 'aJ@#!'),
        ])

        conn.commit()
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            query = f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            conn.close()

            if user:
                session['username'] = username
                return redirect(url_for('welcome'))
            else:
                error = "Invalid username or password. Please try again."
        except:
            error = "A database error occurred. Please try again."

    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/robots.txt')
def robots():
    content = render_template('robots.txt')
    return Response(content, mimetype='text/plain')

@app.route('/adminOnly')
def admins_only():
    if 'username' in session and session['username'] == 'admin':
        with open('flag.txt', 'r') as flag_file:
            flag_content = flag_file.read()
        return render_template('admin_only.html', flag_content=flag_content)
    else:
        return "Access denied! admin only!", 403

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0')
