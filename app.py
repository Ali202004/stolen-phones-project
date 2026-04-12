from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_phone():
    if request.method == 'POST':
        # هنا سيتم لاحقاً إضافة كود الربط مع قاعدة البيانات MySQL
        return "تم حفظ البلاغ بنجاح! <br> <a href='/'>العودة للرئيسية</a>"
    return render_template('add.html')

@app.route('/search')
def search():
    brand = request.args.get('brand')
    return f"جاري البحث عن أجهزة ماركة: {brand} <br> <a href='/'>العودة للرئيسية</a>"

if __name__ == '__main__':
    app.run(debug=True)
