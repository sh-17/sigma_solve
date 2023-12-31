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

    create_script = ''' CREATE TABLE IF NOT EXISTS test_data(
                                new_id     bigint,
                                new_cat    varchar(200) NOT NULL);'''
    cursor.execute(create_script)
    print("Table Created successfully")


    insert_script = '''INSERT INTO test_data(new_id, new_cat) VALUES(%s, %s)'''
    insert_values = [(100, 'agni'), (200, 'agni'), (200, 'vayu'), (300, 'vayu'), (500, 'vayu'), (500, 'dharti'), (700, 'dharti')]
    for record in insert_values:
        cursor.execute(insert_script, record)
    # cursor.execute(insert_script)
    print("values are inserted")

    #  USING AGGREGATE FUNCTIONS
    window_func = '''SELECT new_id, new_cat,
                     SUM(new_id) OVER(ORDER BY new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "Total",
                     AVG(new_id) OVER(ORDER BY new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "Average",
                     COUNT(new_id) OVER(ORDER BY new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "Count",
                     MIN(new_id) OVER(ORDER BY new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "Min",
                     MAX(new_id) OVER(ORDER BY new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "Max"
                     FROM test_data;
                    '''
    cursor.execute(window_func)
    print("execute the function: ")

    # USING RANKING FUNCTION
    ranking_func = '''SELECT new_id,
                      ROW_NUMBER() OVER(ORDER BY new_id) AS "ROW_NUMBER",
                      RANK() OVER(ORDER BY new_id) AS "RANK",
                      DENSE_RANK() OVER(ORDER BY new_id) AS "DENSE_RANK",
                      PERCENT_RANK() OVER(ORDER BY new_id) AS "PERCENT_RANK"
                      FROM test_data
                   '''
    record = cursor.fetchall()
    print("Total fees per workshop: ")
    for row in record:
        print("Ranking Function: ",row)

    cursor.execute(ranking_func)

    connection.commit()

    cursor.close()

    connection.close()
except Exception as error:
    print("Error while connecting to Postgresql: ",error)