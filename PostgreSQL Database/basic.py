import psycopg2 as pg

hostname = 'localhost',
port_id = 5432,
database = 'mydb'
username = 'postgres',
pwd = 'hetvi1723'

try:
    conn = pg.connect(
        host='hostname',
        user='username',
        dbname='database',
        passwprd='pwd',
        port='port_id'
    )
    cursor = conn.cursor()

    # define sql query
    # after than execute the query
    conn.execute('query_name')
    # after that you need to commit query for showing data inside datbase
    conn.commit()
    print('it will print the data written or created indside the data ')

    # after that you need to close cursor an connection
    cursor.close()
    conn.close()
except Exception as error:
    print("Error while connection to PostgreSQL: ", error)
