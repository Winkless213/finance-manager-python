from database import get_connection
from datetime import datetime

def add_record(rec_type, amount, category, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO records (date, type, amount, category, description)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d"),
        rec_type,
        amount,
        category,
        description
    ))

    conn.commit()
    conn.close()


def get_all_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records ORDER BY date DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_record(record_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
    conn.commit()
    conn.close()