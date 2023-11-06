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

    # select_query = "SELECT ROUND(AVG(fees)) FROM mycraftyrea"
    select_query = "SELECT COUNT(fees) FROM mycraftyarea"
    # select_query = "SELECT MIN(fees) FROM mycraftyarea"
    # select_query = "SELECT MAX(fees) FROM mycraftyarea"
    # select_query = "SELECT SUM(fees) FROM mycraftyarea"


    cursor.execute(select_query)
    # fees = cursor.fetchall()
    fees= cursor.fetchone()[0]
    print(f"Average No of Fees: {fees}")
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error while connecting to PostgreSQL:", error)