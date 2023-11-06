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

    #Using CONCAT() to concatenate strings
    cursor.execute("SELECT CONCAT('Hello', ' ', 'World')")
    concatenated_string = cursor.fetchone()[0]
    print(f"Concatenated String: {concatenated_string}")

    #Using LENGTH() to get the length of a string
    cursor.execute("SELECT LENGTH('PostgreSQL')")
    string_length = cursor.fetchone()[0]
    print(f"String Length: {string_length}")

    #Using UPPER() to convert a string into uppercase
    cursor.execute("SELECT UPPER('postgresql')")
    uppercase_string = cursor.fetchone()[0]
    print(f"Uppercase String: {uppercase_string}")

    #Using LOWER() to convert a string into lowercase
    cursor.execute("SELECT LOWER('POSTGRESQL')")
    lowercase_string = cursor.fetchone()[0]
    print(f"Lowercase String: {lowercase_string}")

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error while connecting to PostgreSQL:", error)