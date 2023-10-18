import pandas as pd
import psycopg2

filename = r'exemplo.xlsx'

if __name__ == '__main__':
    # postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

    conn = psycopg2.connect(
        'postgres://postgres:postgres@127.0.0.1:5432/postgres')
    cur = conn.cursor()

    sql = '''
        INSERT INTO imports (filename, cola, colb, colc, cold, created_at)
        VALUES (%(filename)s, %(cola)s, %(colb)s, %(colc)s, %(cold)s, NOW());
    '''

    df = pd.read_excel(filename)

    for line in df.values:
        values = {
            'filename': filename,
            'cola': line[0],
            'colb': line[1],
            'colc': line[2],
            'cold': line[3],
        }

        cur.execute(sql, values)

    cur.connection.commit()
    cur.close()
