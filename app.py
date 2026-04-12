from flask import Flask, render_template, request

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# صفحة إضافة بلاغ (تعمل عند الزيارة و عند الإرسال)
@app.route('/add', methods=['GET', 'POST'])
def add_phone():
    if request.method == 'POST':
        # هنا ستضع كود حفظ البيانات في قاعدة البيانات مستقبلاً
        return "تم حفظ البلاغ بنجاح! <br> <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

# مسار البحث (يتم استدعاؤه عند الضغط على زر البحث)
@app.route('/search')
def search():
    brand = request.args.get('brand')
    return f"جاري البحث في قاعدة البيانات عن ماركة: {brand} <br> <a href='/'>العودة للرئيسية</a>"

if __name__ == '__main__':
    # Render سيستخدم المتغير PORT تلقائياً
    app.run()
