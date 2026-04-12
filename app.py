import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            conn = get_db()
            cur = conn.cursor()
            query = "INSERT INTO reports (brand, imei, city, date, phone) VALUES (%s, %s, %s, %s, %s)"
            data = (request.form['brand'], request.form['imei'], request.form['city'], request.form['date'], request.form['phone'])
            cur.execute(query, data)
            conn.commit()
            cur.close()
            conn.close()
            return "تم الحفظ بنجاح! <a href='/'>العودة</a>"
        except Exception as e:
            # هنا سيظهر الخطأ الحقيقي في الـ Logs في Render
            return f"خطأ في قاعدة البيانات: {str(e)}"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
