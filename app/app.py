from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ❌ Hardcoded secret (Secret Scan will detect)
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

    # ❌ SQL Injection (SAST)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    if cursor.fetchone():
        return "Login Success"
    else:
        return "Login Failed"

@app.route("/cmd")
def cmd():
    user_input = request.args.get("cmd")

    # ❌ Command Injection (SAST)
    os.system(user_input)

    return "Command executed"

if __name__ == "__main__":
    # ❌ Debug enabled (SAST)
    app.run(debug=True)