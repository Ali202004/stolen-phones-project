from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قاعدة بيانات وهمية (ستقوم بربطها بـ MySQL لاحقاً)
reports = []

# الصفحة الرئيسية (مخصصة للبحث فقط)
@app.route('/', methods=['GET', 'POST'])
def index():
    search_result = None
    if request.method == 'POST':
        imei = request.form.get('search_imei')
        result = next((r for r in reports if r.get('imei') == imei), None)
        search_result = f"الجهاز موجود: {result}" if result else "لم يتم العثور على الجهاز"
    return render_template('index.html', search_result=search_result)

# صفحة الإبلاغ (تفتح كصفحة منفصلة)
@app.route('/add', methods=['GET', 'POST'])
def add_phone():
    if request.method == 'POST':
        new_report = {
            'imei': request.form.get('imei'),
            'city': request.form.get('city'),
            'date': request.form.get('date'),
            'phone': request.form.get('phone')
        }
        reports.append(new_report)
        return "تم حفظ البلاغ بنجاح! <script>setTimeout(function(){window.location.href='/';}, 2000);</script>"
    return render_template('add.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
