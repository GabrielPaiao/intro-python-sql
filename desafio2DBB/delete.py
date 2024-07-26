from init_db import get_connection

def delete_people():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pessoas ORDER BY id DESC LIMIT 10")
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    delete_people()