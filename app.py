from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "موقع مشروع الهواتف المسروقة يعمل بنجاح!"

if __name__ == '__main__':
    # Render يحدد المنفذ تلقائياً، وإذا لم يجد، يستخدم 10000
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
