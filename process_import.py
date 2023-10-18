import psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect(
        'postgres://postgres:postgres@127.0.0.1:5432/postgres')
    cur = conn.cursor()

    SQL = '''
        INSERT INTO stocks (fabrica, gramatura, formato, disponivel_em, created_at)
        SELECT cola, colb, colc, to_date(cold,'DD/MM/YYYY'), NOW() FROM imports WHERE updated_at IS NULL;
    '''
    cur.execute(SQL, {})
    cur.execute('UPDATE stocks SET updated_at = NOW() WHERE updated_at IS NULL;', {})
    cur.connection.commit()
    cur.close()
