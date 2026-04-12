from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# نستخدم مساراً مطلقاً لقاعدة البيانات
DB_PATH = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    imei = request.form.get('imei', '').strip()
    conn = sqlite3.connect(DB_PATH)
    # استخدام الاستعلام للبحث بدقة
    report = conn.execute('SELECT brand, imei, city, date, phone FROM reports WHERE imei = ?', (imei,)).fetchone()
    conn.close()
    return render_template('index.html', report=report, imei=imei, searched=True)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute('INSERT INTO reports (brand, imei, city, date, phone) VALUES (?,?,?,?,?)',
                         (request.form['brand'], request.form['imei'].strip(), request.form['city'], request.form['date'], request.form['phone']))
            conn.commit()
            conn.close()
            return "تم حفظ البلاغ بنجاح! <br> <a href='/'>عودة للرئيسية</a>"
        except Exception as e:
            return f"حدث خطأ أثناء الحفظ: {e}"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run()
