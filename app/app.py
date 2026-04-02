from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ✅ Secure: No hardcoded fallback
# secret = os.getenv("SECRET_KEY")
# if not secret:
#     raise RuntimeError("SECRET_KEY environment variable not set")

# app.config['SECRET_KEY'] = secret

# Connect to DB
def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return """
    <h1>Secure DevOps Project</h1>

    <a href="/dashboard" target="_blank">
        <button>Open Dashboard</button>
    </a>
    """


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # ✅ Input validation
    if not username.isalnum() or not password.isalnum():
        return "Invalid input"

    conn = get_db()
    cursor = conn.cursor()

    # ✅ Parameterized query (prevents SQL Injection)
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()


@app.route("/dashboard")
def dashboard():
    return """
    <h1>Security Dashboard</h1>
    <button onclick="loadData()">Load Reports</button>

    <pre id="output"></pre>

    <script>
    async function loadData() {
        const data = await fetch('/api/sast').then(r => r.json());
        document.getElementById('output').innerText =
            JSON.stringify(data, null, 2);
    }
    </script>
    """


    if user:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=False)