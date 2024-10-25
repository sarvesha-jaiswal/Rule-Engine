import sqlite3

def get_db():
    conn = sqlite3.connect('rules.db')
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_text TEXT,
            ast_structure TEXT
        )
    ''')
    conn.commit()
    conn.close()
