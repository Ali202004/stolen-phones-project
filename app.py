from flask import Flask, render_template, request

# تعريف التطبيق
app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# صفحة إضافة بلاغ
@app.route('/add', methods=['GET', 'POST'])
def add_phone():
    if request.method == 'POST':
        # هنا ستضع لاحقاً كود حفظ البيانات في قاعدة البيانات
        return "تم حفظ البلاغ بنجاح! <br> <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# مسار البحث
@app.route('/search')
def search():
    brand = request.args.get('brand')
    return f"جاري البحث عن ماركة: {brand} <br> <a href='/'>العودة للرئيسية</a>"

# ملاحظة هامة:
# عند استخدام Gunicorn، لا نضع app.run() نهائياً في الكود.
# Gunicorn سيقوم بتشغيل 'app' الموجودة في 'app.py' تلقائياً.
