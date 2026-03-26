from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ✅ Secure secret
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_key")

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
        return "Invalid input"

    conn = get_db()
    cursor = conn.cursor()

    # ✅ Safe query
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
    app.run(debug=False)