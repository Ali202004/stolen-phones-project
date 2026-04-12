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

@app.route('/search', methods=['POST'])
def search():
    imei = request.form.get('imei', '').strip()
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT brand, imei, city, date, phone FROM reports WHERE imei = %s', (imei,))
    report = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('index.html', report=report, imei=imei, searched=True)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        conn = get_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO reports (brand, imei, city, date, phone) VALUES (%s, %s, %s, %s, %s)',
                    (request.form['brand'], request.form['imei'], request.form['city'], request.form['date'], request.form['phone']))
        conn.commit()
        cur.close()
        conn.close()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()        conn.close()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
        conn.close()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()        return "تم حفظ البلاغ بنجاح! <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
