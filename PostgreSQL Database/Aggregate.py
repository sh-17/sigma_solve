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

    cursor.execute("SELECT COUNT(*) FROM mycraftyarea")
    theme = cursor.fetchone()[0]
    print(f"Total theme: {theme}")

    cursor.execute("SELECT SUM(a_id) FROM mycraftyarea")
    a_id = cursor.fetchone()[0]
    print(f"total Id: {a_id}")

    cursor.execute("SELECT MAX(fees) FROM mycraftyarea")
    fees = cursor.fetchone()[0]
    print(f"max-fees: {fees}")

    cursor.execute("SELECT MIN(fees) FROM mycraftyarea")
    fees = cursor.fetchone()[0]
    print(f"Lowest-fees: {fees}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL: ", error)