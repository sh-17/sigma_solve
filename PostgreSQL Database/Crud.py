import psycopg2 as pg

class DatabaseManager:
    def __init__(self, a):
        self.hostname = 'localhost'
        self.database = 'mydb'
        self.username = 'postgres'
        self.password = 'hetvi1723'
        self.port = 5432
        self.conn = None
        self.cursor = None
        self.a = a

        try:
            self.conn = pg.connect(database=self.database, user=self.username, password=self.password)
            self.cursor = self.conn.cursor()

            if self.a == 1:
                self.create_table()
            elif self.a == 2:
                self.insert_data()
            elif self.a == 3:
                self.update_records()
            elif self.a == 4:
                self.delete_records()
            elif self.a == 5:
                data = self.get_all_data()
                for row in data:
                    print(row)

        except pg.Error as e:
            print("Error:", e)
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def create_table(self):
        create_script = '''CREATE TABLE IF NOT EXISTS employee (
                                id serial PRIMARY KEY,
                                name varchar(40) NOT NULL,
                                salary int,
                                dept_id varchar(30))'''
        self.cursor.execute(create_script)
        self.conn.commit()

    def insert_data(self):
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        dept_id = input("Enter department ID: ")
        insert_script = '''INSERT INTO employee(name, salary, dept_id) VALUES (%s, %s, %s)'''
        self.cursor.execute(insert_script, (name, salary, dept_id))
        self.conn.commit()

    def update_records(self):
        update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
        self.cursor.execute(update_script)
        self.conn.commit()

    def delete_records(self):
        name = input("Enter name to delete records: ")
        delete_script = 'DELETE FROM employee WHERE name = %s'
        self.cursor.execute(delete_script, (name,))
        print(name, "named data is deleted")
        self.conn.commit()

    def get_all_data(self):
        self.cursor.execute("SELECT * FROM employee")
        result = self.cursor.fetchall()
        return result


if __name__ == "__main__":
    choice = int(input("Choose an option:\n1. Create Table\n2. Insert Data\n3. Update Records\n4. Delete Records\n5. "
                       "Show Data\n6. Exit\n"))

    if choice in [1, 2, 3, 4, 5]:
        db_manager = DatabaseManager(choice)
    elif choice == 6:
        print("Exiting the program.")
    else:
        print("Invalid choice. Please choose a valid option.")
