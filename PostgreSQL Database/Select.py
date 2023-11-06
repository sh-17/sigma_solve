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

    # Define your SELECT query
    select_query = "SELECT * FROM mycraftyarea"

    # Execute the query
    cursor.execute(select_query)

    # Fetch the results
    results = cursor.fetchall()
    # Process and print the results
    for row in results:
        c1_value = row[0]
        c2_value = row[1]
        c3_value = row[2]
        print(f"ID : {c1_value}, Name : {c2_value}, workshop : {c3_value}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)