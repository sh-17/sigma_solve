import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'mydb'
username = 'postgres'
pwd = 'hetvi1723'
port = 5432
conn = None
cur = None

"""
--> connect will work as it will open our database  where we will be allowed to perform any databse 
    transaction like ddl,dml,dql but,
    
    in order to perform any of sql transaction or database transactions  we will need to open a cursor
    cursor means something that help us to perform any of the sql operations it kind of the stores the values
    that will be returned from those sql operations
"""

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port)

    """using with with clause ---- with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
     --> it will close cursor by own , if we not commit or close cursor then with clause will take care of it  but it will not 
         close the connect so we have to maintain the connection close , we also dont have to write default value inside 
         cur, conn """

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # this will tell the cursor is to return the data in the form of dictionary
    cur.execute('DROP TABLE IF EXISTS employee')

    """ CREATING DATABASE -- by using serial it will auto serialize the id's itself """

    create_script = ''' CREATE TABLE IF NOT EXISTS employee(
                            id      serial PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30))'''
    cur.execute(create_script)

    """ INSERTING THE VALUE INSIDE DATABASE """

    insert_script = '''INSERT INTO employee(name,salary,dept_id) VALUES(%s,%s,%s)'''
    insert_values = [('hetvi', 20000, 'a1'), ('sheth', 2000, 'a2'), ('hello', 50000, 'a3'), ('bye', 30000, 'a4')]
    for record in insert_values:
        cur.execute(insert_script, record)

    """ HOW WE CAN FETCH ALL DATA FROM DATABASE TABLE INTO PYTHON SCRIPT 
        --- to fetching all the data we use fetchall() method
        --- we can also fetch single value by using fetchone()
        --- if there are multiple data and you to fetch any single column you need to import
            import psycopg2.extras
    """

    """ UPDATE & DELETE """
    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)  # it will increase the salary 0.5

    delete_script = 'DELETE FROM employee WHERE name = %s'
    delete_record = ('sheth',)
    cur.execute(delete_script, delete_record)

    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record['name'], record['salary'])  # it will gives us output same but in dictionary form
        # print(record[1],record[2]) by using indexing it will show that first 2 column
        # print(record) it will show the date line to line
        # print(cur.fetchall()) it will print list of tuple which holds one record

    conn.commit()  # after committing this will show data into our db

except Exception as error:
    print(" There is some Error", error)
finally:
    if cur is not None:  # means if the cursor is open only then i have to close it
        cur.close()
    if conn is not None:
        conn.close()
