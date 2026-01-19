from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ✅ create table if not exists (IMPORTANT)
def init_db():
    conn = db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

@app.route("/post", methods=["GET", "POST"])
def post_job():
    if request.method == "POST":
        title = request.form["title"]
        company = request.form["company"]
        location = request.form["location"]
        description = request.form["description"]

        conn = db_connection()
        conn.execute(
            "INSERT INTO jobs (title, company, location, description) VALUES (?, ?, ?, ?)",
            (title, company, location, description)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("post_job.html")

if __name__ == "__main__":
    init_db()        # ✅ ensure DB + table exist
    app.run(debug=True)


