from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_FILE = "notatka.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    conn.commit()
    conn.close()

@app.route("/api/notes", methods=["GET"])
def get_notes():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, content FROM notes")
    notes = [{"id": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    
    return jsonify(notes)

@app.route("/api/notes", methods=["POST"])
def add_note():
    content = request.json.get("content")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Note added"}), 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
ZSI-12: poprawka notatki
