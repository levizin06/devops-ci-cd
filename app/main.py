import os
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_conn():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

@app.route("/")
def index():
    return "API rodando! Meu projeto DevOps."

@app.route("/db")
def db():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT NOW()")
        agora = cur.fetchone()[0]
        conn.close()
        return jsonify(status="ok", mysql_time=str(agora))
    except Exception as e:
        return jsonify(status="erro", detalhe=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)