from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# إنشاء قاعدة البيانات عند البدء
def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, brand TEXT, imei TEXT, city TEXT, date TEXT, phone TEXT)')
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
        return "تم حفظ البلاغ بنجاح! <br> <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
