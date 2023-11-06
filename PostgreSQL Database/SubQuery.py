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
    """ ---> Find average value -- filter the customer data > avj value """
    avj_fees = """SELECT avg(fees) FROM mycraftyarea"""

    cursor.execute(avj_fees)

    results = cursor.fetchall()
    for row in results:
        print("avj_fees", row)

    # filtering the data using local operator and comparision operator
    # it will show avj fees which is greater than 1000
    filter_data = """SELECT * FROM mycraftyarea WHERE fees > (SELECT avg(fees) FROM mycraftyarea) """

    cursor.execute(filter_data)

    results = cursor.fetchall()
    for row in results:
        print("filter_data: ", row)

    #  using exists function its a one type of join
    #  The EXISTS operator is used to test for the existence of any record in a subquery.
    # The EXISTS operator returns TRUE if the subquery returns one or more records.

    exists_query = ''' SELECT stu_name, workshop
                       FROM mycraftyarea m
                       WHERE EXISTS(SELECT name, manager_id
                                    FROM employee as e
                                    WHERE m.stu_name = e.name
                                    AND salary > 2000 )'''

    cursor.execute(exists_query)
    results = cursor.fetchall()
    for row in results:
        print(exists_query)

    cursor.close()
    connection.close()
except Exception as error:
    print("Error while connecting to Postgresql: ", error)
