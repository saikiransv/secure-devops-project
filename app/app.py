# app/app.py

from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ❌ Hardcoded secret (secret-scan FAIL)
app.config['SECRET_KEY'] = "ghp_abcd1234verylongsecrettokenxyz"

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

    # ❌ SQL Injection (SAST FAIL)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    if cursor.fetchone():
        return "Login Success"
    else:
        return "Login Failed"

@app.route("/cmd")
def cmd():
    user_input = request.args.get("cmd")

    # ❌ Command Injection (SAST FAIL)
    os.system(user_input)

    return "Command executed"

if __name__ == "__main__":
    # ❌ Debug ON (SAST FAIL)
    app.run(host="0.0.0.0", port=5000, debug=True)