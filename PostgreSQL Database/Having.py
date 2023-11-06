import psycopg2

# Replace these values with your PostgreSQL database configuration
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

    # Define the SQL query with a HAVING clause
    query = """
    SELECT a_id, SUM(fees) AS total_amount
    FROM mycraftyarea
    GROUP BY a_id
    HAVING SUM(fees) > 1000;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("a_id with total order fees > 1000:")
    for row in results:
        a_id, total_fees = row
        print(f"Artist ID: {a_id}, Total fees: {total_fees}")

    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error while connecting to PostgreSQL: ", error)
