# app/app.py

from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

<<<<<<< HEAD
# ❌ REALISTIC SECRET (WILL BE DETECTED)
app.config['SECRET_KEY'] = "ghp_abcd1234abcd1234abcd1234abcd1234abcd"

=======
# ✅ Secure: No hardcoded fallback
# secret = os.getenv("SECRET_KEY")
# if not secret:
#     raise RuntimeError("SECRET_KEY environment variable not set")

# app.config['SECRET_KEY'] = secret

# Connect to DB
>>>>>>> 88a8d36441f1b2ec6c47c8514ffb6b6aad657c20
def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
<<<<<<< HEAD
    return "Vulnerable App Running"
=======
    return """
    <h1>Secure DevOps Project</h1>

    <a href="/dashboard" target="_blank">
        <button>Open Dashboard</button>
    </a>
    """

>>>>>>> 88a8d36441f1b2ec6c47c8514ffb6b6aad657c20

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    # ❌ SQL Injection
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)

<<<<<<< HEAD
    if cursor.fetchone():
        return "Login Success"
=======
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
>>>>>>> 88a8d36441f1b2ec6c47c8514ffb6b6aad657c20
    else:
        return "Login Failed"

@app.route("/cmd")
def cmd():
    user_input = request.args.get("cmd")

    # ❌ Command Injection
    os.system(user_input)

    return "Command executed"

if __name__ == "__main__":
    # ❌ Debug ON
    app.run(host="0.0.0.0", port=5000, debug=True)