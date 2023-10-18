import pandas as pd
import psycopg2
import argparse
from os import path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--File', help='Caminho do arquivo XLS para importação')
    args = parser.parse_args()

    filename = args.File
    if not path.isfile(filename):
        print('Arquivo de importação não encontrado!')
        exit()

    # postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

    conn = psycopg2.connect(
        'postgres://postgres:postgres@127.0.0.1:5432/postgres')
    cur = conn.cursor()

    SQL = '''
        INSERT INTO imports (filename, cola, colb, colc, cold, created_at)
        VALUES (%(filename)s, %(cola)s, %(colb)s, %(colc)s, %(cold)s, NOW());
    '''

    df = pd.read_excel(filename)

    filename_short = path.basename(filename)
    for line in df.values:
        values = {
            'filename': filename_short,
            'cola': line[0],
            'colb': line[1],
            'colc': line[2],
            'cold': line[3],
        }
        cur.execute(SQL, values)

    cur.connection.commit()
    cur.close()
