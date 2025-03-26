from flask import Flask, render_template_string, request
import hashlib

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Хешування пароля</title>
    <style>
        body { font-family: Arial; padding: 20px; background-color: #f4f4f4; }
        .container { background: white; padding: 20px; border-radius: 8px; width: 400px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input[type="password"], input[type="submit"] { width: 100%; padding: 10px; margin-top: 10px; }
        .message { margin-top: 20px; font-weight: bold; }
        .hash { word-break: break-all; color: green; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Хешування пароля (SHA-256)</h2>
        <form method="POST">
            <input type="password" name="password" placeholder="Пароль" required>
            <input type="password" name="confirmPassword" placeholder="Підтвердіть пароль" required>
            <input type="submit" value="Хешувати">
        </form>
        {% if message %}
            <div class="message">{{ message }}</div>
            {% if hashed %}
                <div class="hash">{{ hashed }}</div>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    hashed = ''
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirmPassword')

        if password == confirm:
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            message = 'Пароль підтверджено. Ось SHA-256 хеш:'
        else:
            message = 'Паролі не співпадають. Спробуйте ще раз.'

    return render_template_string(HTML_FORM, message=message, hashed=hashed)

if __name__ == '__main__':
    app.run(debug=True)
