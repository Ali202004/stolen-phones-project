import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mazen_secret_key_2026' # مفتاح تشفير الجلسة

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

# بيانات الإدارة (التي طلبتها)
ADMIN_USERNAME = "Mazen"
ADMIN_PASSWORD = "202004"

@app.route('/')
def index():
    return render_template('index.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('reports'))
        else:
            return "خطأ في اسم المستخدم أو كلمة المرور! <a href='/login'>حاول مجدداً</a>"
    return render_template('login.html')

# تسجيل الخروج
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

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
            return "تم الحفظ بنجاح! <br><a href='/' class='btn btn-primary'>العودة للرئيسية</a>"
        except Exception as e:
            return f"خطأ في الحفظ: {str(e)}"
    return render_template('add.html')

@app.route('/reports')
def reports():
    # التحقق هل المستخدم مسجل دخول أم لا
    is_admin = session.get('logged_in')
    
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM reports ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reports.html', reports=rows, is_admin=is_admin)

@app.route('/delete/<int:report_id>', methods=['POST'])
def delete(report_id):
    if not session.get('logged_in'):
        return "غير مسموح لك بالدخول!", 403
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM reports WHERE id = %s", (report_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('reports'))

if __name__ == "__main__":
    app.run()
