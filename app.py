from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات وهمية للتجربة (ستربطها لاحقاً بـ MySQL)
reports = []

@app.route('/', methods=['GET', 'POST'])
def index():
    search_result = None
    if request.method == 'POST' and 'search_imei' in request.form:
        imei = request.form.get('search_imei')
        # بحث بسيط في القائمة
        search_result = next((r for r in reports if r['imei'] == imei), "لم يتم العثور على الجهاز")
    
    return render_template('index.html', search_result=search_result)

@app.route('/add', methods=['POST'])
def add_phone():
    # استقبال بيانات البلاغ
    new_report = {
        'imei': request.form.get('imei'),
        'city': request.form.get('city'),
        'date': request.form.get('date'),
        'phone': request.form.get('phone')
    }
    reports.append(new_report)
    return "تم حفظ البلاغ بنجاح! <script>setTimeout(function(){window.location.href='/';}, 2000);</script>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
