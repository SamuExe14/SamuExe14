# CANARY FILE — codice deliberatamente vulnerabile per validare Snyk Code.
# NON deve essere mai mergiato su branch protetti. Rimuovere dopo il test.
import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    # Atteso: Command Injection (CWE-78) — High.
    # Taint: request.args (source remota) -> os.system (sink), no sanitizzazione.
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    return "ok"


@app.route("/exec")
def run_cmd():
    # Atteso: Command Injection (CWE-78) — High.
    # shell=True con input remoto concatenato.
    cmd = request.args.get("cmd")
    subprocess.run("ls " + cmd, shell=True)
    return "ok"


@app.route("/user")
def get_user():
    # Atteso: SQL Injection (CWE-89) — High.
    name = request.args.get("name")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return str(cur.fetchall())


@app.route("/read")
def read_file():
    # Atteso: Path Traversal (CWE-23/CWE-22) — High.
    path = request.args.get("path")
    with open("/var/data/" + path) as fh:
        return fh.read()