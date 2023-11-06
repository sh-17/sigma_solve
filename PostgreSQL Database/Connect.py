import psycopg2

# Replacing the values with your PostgreSQL database configuration
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

    # Define the CREATE TABLE SQL query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS mycraftyarea (
        id serial PRIMARY KEY,
        name VARCHAR(250),
        age int
    )
    """

    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)

    # Commit the changes to the database
    connection.commit()

    print("Table Created successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Showing an while connection to PostgreSQL database", error)