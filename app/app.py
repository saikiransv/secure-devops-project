from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ✅ Secure: NO hardcoded fallback
# Will crash if SECRET_KEY is not set (good security practice)
try:
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
except KeyError:
    raise RuntimeError("❌ SECRET_KEY environment variable not set!")

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "Secure App Running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # ✅ Input validation
    if not username.isalnum() or not password.isalnum():
        return "Invalid input", 400

    conn = get_db()
    cursor = conn.cursor()

    # ✅ Parameterized query (prevents SQL Injection)
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful", 200
    else:
        return "Invalid credentials", 401

if __name__ == "__main__":
    # ✅ Debug OFF in production
    app.run(host="0.0.0.0", port=5000, debug=False)