import csv

import psycopg2

# Establish a database connection
mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="hetvi1723",
    port=5432,
    database="mydb"
)
mc = mydb.cursor()

if mc:
    print("----- DATABASE CONNECTED -----")
else:
    print(" !!! DATABASE NOT CONNECTED !!! ")
csv_file = 'my_data.csv'
try:
    with open(csv_file,'r')as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # skip the header row if it exists

        # Assuming you want to SELECT data from the "student" table
        for row in csv_reader:
            sql = "INSERT INTO student(s_id,s_name,s_std,s_div) VALUES(%s, %s, %s, %s)"
            mc.execute(sql,(row[0],row[1],row[2],row[3]))

    mydb.commit()
    mc.close()
    mydb.close()
    print("Data retrieved successfully.")

except (Exception, psycopg2.Error) as error:
    print("Error retrieving data:", error)
