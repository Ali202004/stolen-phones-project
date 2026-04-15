import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# مفتاح سري للجلسة (مهم لعمل لوحة التحكم)
app.secret_key = 'mazen_secret_key_2026'

# الاتصال بقاعدة البيانات
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    imei = request.args.get('imei')
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM reports WHERE imei = %s", (imei,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reports.html', reports=results, is_admin=session.get('logged_in'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO reports (brand, imei, city, date, phone) VALUES (%s, %s, %s, %s, %s)",
                        (request.form['brand'], request.form['imei'], request.form['city'], request.form['date'], request.form['phone']))
            conn.commit()
            cur.close()
            conn.close()
            return "تم الحفظ بنجاح! <br><br> <a href='/' class='btn btn-primary'>العودة للرئيسية</a>"
        except Exception as e:
            return f"خطأ في الحفظ: {str(e)}"
    return render_template('add.html')

@app.route('/reports')
def reports():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM reports ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reports.html', reports=rows, is_admin=session.get('logged_in'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "Mazen" and request.form['password'] == "202004":
            session['logged_in'] = True
            return redirect('/reports')
        else:
            return "اسم المستخدم أو كلمة المرور خطأ! <a href='/login'>حاول مجدداً</a>"
    return render_template('login.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if session.get('logged_in'):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM reports WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect('/reports')

if __name__ == "__main__":
    app.run()
