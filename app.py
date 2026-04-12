from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_phone():
    if request.method == 'POST':
        # استقبال البيانات من النموذج
        imei = request.form.get('imei')
        city = request.form.get('city')
        date = request.form.get('date')
        
        # هنا ستضع لاحقاً كود الحفظ في قاعدة البيانات
        return f"تم استلام بيانات الجهاز {imei} في {city} بتاريخ {date}. تم الحفظ بنجاح!"
    return render_template('add.html')

@app.route('/search', methods=['GET'])
def search():
    brand = request.args.get('brand')
    return f"جاري البحث عن الجهاز في قاعدة البيانات: {brand}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
