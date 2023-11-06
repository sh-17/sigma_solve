import psycopg2

hostname = "localhost"
username = "postgres"
pwd = "hetvi1723"
database = "mydb"

try:
    connection = psycopg2.connect(
        host=hostname,
        user=username,
        password=pwd,
        dbname=database
    )

    cursor = connection.cursor()

    # A regular join that joins a table itself Self-joins are very useful to query hierarchical data or to compare
    # rows within the same table.
    self_query = '''
    SELECT t1.name AS empname, t2.name AS manager_name 
    FROM employee AS t1
    JOIN employee AS t2
    ON t2.id = t1.manager_id; '''

    cursor.execute(self_query)
    results = cursor.fetchall()
    print()
    for row in results:
        print("self row:", row)

    #  UNION : UNION : A SQL union clause/operator is used to combine/ concatenate the results of two or more
    #  SELECT statements without returning any duplicate rows and keeps unique records

    union_query = """
    SELECT manager_id FROM employee
    UNION  
    SELECT a_id FROM mycraftyarea"""

    cursor.execute(union_query)
    results = cursor.fetchall()
    print()
    for row in results:
        print("union row: ",row)

    # UNION ALL : nothing but combine two or more table but keep all records , including duplicate records
    union_all_query = """
       SELECT id FROM employee
       UNION ALL
       SELECT a_id FROM mycraftyarea"""

    cursor.execute(union_all_query)
    results = cursor.fetchall()
    print()
    for row in results:
        print("union all row: ", row)

    cursor.close()
    connection.close()

except Exception as error:
    print("Error while connecting to Postgresql: ", error)
