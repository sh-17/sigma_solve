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

    cursor.execute("SELECT workshop, SUM(fees) as total_fees FROM mycraftyarea GROUP BY workshop")
    theme_data = cursor.fetchall()
    print("Total fees per workshop: ")
    for row in theme_data:
        category, total_fees = row
        print(f"{category}: {total_fees}")

    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error while connecting to PostgreSQL: ", error)
