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

    # Creating a cursor to execute SQL queries
    cursor = connection.cursor()

    # INNER JOIN : Give the common data & Combines the two tables
    inner_query = """
   SELECT * FROM customer AS c 
   INNER JOIN mycraftyarea as m 
   ON c.customer_id = m.a_id """

    cursor.execute(inner_query)
    results = cursor.fetchall()

    for row in results:
        print("inner row: ",row)

    # Left Join : Returns all records from the left table and matched records from the right table
    left_query = """
       SELECT * FROM customer AS c 
       INNER JOIN mycraftyarea as m 
       ON c.customer_id = m.a_id """
    cursor.execute(left_query)
    results = cursor.fetchall()
    print()

    for row in results:
        print("left row: ",row)

    # Right Join : Returns all records from the right table, and matched records from the left table
    right_query = """
       SELECT * FROM customer AS c 
       INNER JOIN mycraftyarea as m 
       ON c.customer_id = m.a_id """
    cursor.execute(right_query)
    results = cursor.fetchall()
    print()

    for row in results:
        print("right row: ",row)

    # Full Join : Returns all records when there is match in either left or right table If the value is null then also it will combine the tables
    full_join = """
           SELECT * FROM customer AS c 
           INNER JOIN mycraftyarea as m 
           ON c.customer_id = m.a_id """
    cursor.execute(full_join)
    results = cursor.fetchall()
    print()

    for row in results:
        print("full row: ", row)

    cursor.close()
    connection.close()
except Exception as error:
    print("Error while connecting to postgresql: ",error)