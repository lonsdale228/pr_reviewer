import sqlite3


def sql_query(name: str):
    conn = sqlite3.connect('huge_db.db')
    cursor = conn.cursor()
    a = cursor.execute(f'SELECT * FROM users where name={name}')
    print(a.fetchall())
    conn.close()


if __name__ == '__main__':
    sql_query('Admin')
