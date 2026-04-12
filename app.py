from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        # هنا ستضع لاحقاً كود حفظ البيانات في MySQL
        return "تم استلام طلب الإضافة!"
    return render_template('add.html')

@app.route('/search')
def search():
    # هنا ستضع كود البحث في قاعدة البيانات
    brand = request.args.get('brand')
    return f"جاري البحث عن ماركة: {brand}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
