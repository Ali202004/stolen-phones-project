from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'Mazen_202004'

def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS reports 
                    (id INTEGER PRIMARY KEY, brand TEXT, imei TEXT, city TEXT, date TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    imei = request.form.get('imei')
    conn = sqlite3.connect('data.db')
    report = conn.execute('SELECT brand, imei, city, date, phone FROM reports WHERE imei = ?', (imei,)).fetchone()
    conn.close()
    return render_template('index.html', report=report, imei=imei)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        conn = sqlite3.connect('data.db')
        conn.execute('INSERT INTO reports (brand, imei, city, date, phone) VALUES (?,?,?,?,?)',
                     (request.form['brand'], request.form['imei'], request.form['city'], request.form['date'], request.form['phone']))
        conn.commit()
        conn.close()
        return "تم حفظ البلاغ بنجاح! <script>setTimeout(function(){window.location.href='/';}, 2000);</script>"
    return render_template('add.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST' and request.form['username'] == 'Mazen' and request.form['password'] == '202004':
        session['admin'] = True
        return redirect(url_for('dashboard'))
    return render_template('admin_login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('admin'): return redirect(url_for('admin'))
    conn = sqlite3.connect('data.db')
    reports = conn.execute('SELECT * FROM reports').fetchall()
    conn.close()
    return render_template('dashboard.html', reports=reports)

if __name__ == "__main__":
    app.run(debug=True)
    return render_template('add.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['username'] == 'Mazen' and request.form['password'] == '202004':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('admin_login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'): return redirect(url_for('admin'))
    conn = sqlite3.connect('data.db')
    reports = conn.execute('SELECT * FROM reports').fetchall()
    conn.close()
    return render_template('dashboard.html', reports=reports)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('data.db')
    conn.execute('DELETE FROM reports WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
