# Vulnerable Flask Application

from flask import Flask, request
import sqlite3

app = Flask(__name__)

# ❌ Hardcoded secret (vulnerability)
SECRET_KEY = "supersecret123"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "Vulnerable App Running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    if cursor.fetchone():
        return "Login Success"
    else:
        return "Login Failed"

if __name__ == "__main__":
    app.run(debug=True)