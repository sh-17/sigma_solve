import psycopg2

def get_data_from_postgresql():
    hostname = 'localhost'
    database = 'mydb'
    username = 'postgres'
    pwd = 'hetvi1723'
    port = 5432

    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port)

        # Create a cursor to execute SQL statements
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve data
        cursor.execute("SELECT * FROM mycraftyarea")
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return result

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Call the function to get data from the database
data_from_db = get_data_from_postgresql()

# Process the retrieved data
if data_from_db is not None:
    for row in data_from_db:
        # You can access the data in each row by index
        # For example, row[0] is the first column in the result
        # Insert your processing logic here
        print(row)
