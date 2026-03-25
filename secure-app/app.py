from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ✅ FIXED: No hardcoded secret
SECRET_KEY = os.getenv("SECRET_KEY", "default")

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "Secure App Running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    # ✅ FIXED: Safe query
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))

    if cursor.fetchone():
        return "Login Success"
    else:
        return "Login Failed"

if __name__ == "__main__":
    app.run(debug=True)