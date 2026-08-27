# CANARY FILE — vedi nota sopra.
import sqlite3
import sys


def get_user(username: str):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # Atteso: SQL Injection (CWE-89) — severity High.
    # Concatenazione di input non fidato nella query.
    cur.execute("SELECT * FROM users WHERE name = '" + username + "'")
    return cur.fetchall()


if __name__ == "__main__":
    print(get_user(sys.argv[1]))