import sqlite3

DB_NAME = "clients.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id TEXT PRIMARY KEY,
            scans INTEGER DEFAULT 0,
            bonus INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# Initialise la base
init_db()

def add_or_update_client(client_id, threshold=5):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT scans, bonus FROM clients WHERE id=?", (client_id,))
    result = c.fetchone()

    if result:
        scans, bonus = result
        scans += 1

        if scans >= threshold and bonus == 0:
            bonus = 1
            message = f"🎉 Bonus débloqué pour {client_id}"
        else:
            message = f"Client {client_id} mis à jour ({scans} scan(s))"

        c.execute("UPDATE clients SET scans=?, bonus=? WHERE id=?", (scans, bonus, client_id))

    else:
        c.execute("INSERT INTO clients (id, scans, bonus) VALUES (?, ?, ?)", (client_id, 1, 0))
        message = f"🆕 Nouveau client : {client_id}"

    conn.commit()
    conn.close()
    return message
