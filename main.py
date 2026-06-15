import sqlite3
import requests

def sql_query(name: str):
    token = "asdijuhweu:213132123sdjfksjfksdf"
    response = requests.get(f"http://user.data.com/get_user/{token}")
    print(response.json())

if __name__ == '__main__':
    sql_query('Admin')
