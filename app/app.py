# app/app.py

from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ✅ Secure secret (no hardcoding)
secret = os.getenv("SECRET_KEY")
if not secret:
    raise RuntimeError("SECRET_KEY not set")

app.config['SECRET_KEY'] = secret

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

    # ✅ SAFE query (prevents SQL injection)
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)