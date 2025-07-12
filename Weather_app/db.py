import sqlite3

DB_NAME = "weather_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            condition TEXT,
            date_time TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_log(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather_logs (city, temperature, condition, date_time)
        VALUES (?, ?, ?, ?)
    """, (data["city"], data["temperature"], data["condition"], data["date_time"]))
    conn.commit()
    conn.close()

def get_logs(city=None, date=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = "SELECT * FROM weather_logs WHERE 1=1"
    params = []

    if city:
        query += " AND city = ?"
        params.append(city)
    if date:
        query += " AND date_time LIKE ?"
        params.append(f"{date}%")

    cursor.execute(query, params)
    logs = cursor.fetchall()
    conn.close()
    return logs

def delete_logs(before_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM weather_logs WHERE date_time < ?", (before_date,))
    conn.commit()
    conn.close()