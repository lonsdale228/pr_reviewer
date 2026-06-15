import sqlite3
import pandas as pd


def sql_query(name: str):
    df = pd.DataFrame({'price': [100, 200, 300], 'qty': [2, 5, 1]})

    totals = []
    for index, row in df.iterrows():
        totals.append(row['price'] * row['qty'])
    df['total'] = totals


if __name__ == '__main__':
    sql_query('Admin')
