import pandas as pd
import sqlite3
from sqlite3 import Error

conn_orders = sqlite3.connect("orders.db")
cur = conn_orders.cursor()

# sql_statement = "select * from customers;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orders;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from vendors;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from products;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orderitems;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from productnotes;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)


def ex1():
    # Write an SQL statement that SELECTs all rows from the `customers` table
    # output columns: cust_name, cust_email

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_name, cust_email FROM customers;"
    return sql_statement


def ex2():
    # Write an SQL statement that SELECTs all rows from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id FROM products;"
    return sql_statement


def ex3():
    # Write an SQL statement that SELECTs distinct rows for vend_id from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT DISTINCT vend_id FROM products;"
    return sql_statement


def ex4():
    # Write an SQL statement that SELECTs the first five rows from the `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products LIMIT 5;"
    return sql_statement


def ex5():
    # Write an SQL statement that SELECTs 4 rows starting from row 3 from `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products LIMIT 4 OFFSET 3;"
    return sql_statement


def ex6():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_name
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products ORDER BY prod_name;"
    return sql_statement


def ex7():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price ASC, prod_name ASC;"
    return sql_statement


def ex8():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price (descending order)
    # and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC, prod_name ASC;"
    return sql_statement


def ex9():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 2.50
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_price = 2.50"
    return sql_statement

def ex10():
    # Write an SQL statement that SELECTs all rows from `products` table where the name of product is Oil can
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name = 'Oil can'"
    return sql_statement


def ex11():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 
    # less than or equal to 10
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_price <= 10 " 
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex12():
    # Write an SQL statement that SELECTs all rows from `products` table where the vendor id is not equal to 1003
    # output columns: vend_id, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_name FROM products where vend_id != 1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex13():
    # Write an SQL statement that SELECTs all rows from `products` table where the product prices are between 5 and 10
    # output columns: prod_name, prod_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name, prod_price FROM products where prod_price BETWEEN 5 AND 10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex14():
    # Write an SQL statement that SELECTs all rows from the `customers` table where the customer email is empty
    # output columns: cust_id, cust_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_id, cust_name FROM customers where cust_email IS NULL"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex15():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1003 and
    # the price is less than or equal to 10. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id = 1003 AND prod_price <= 10 "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex16():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 and
    # the price is greater than or equal to 5. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where (vend_id = 1002 OR vend_id = 1003) AND prod_price >= 5"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex17():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 or 1005.
    # Use the IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement =  "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id IN (1002,1003,1005)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex18():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is NOT 1002 or 1003.
    # Use the NOT IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products where vend_id NOT IN (1002,1003) "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex19():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name starts with 'jet'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name like 'jet%'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex20():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name ends with 'anvil'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name like '%anvil'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex21():
    # Write an SQL statement that SELECTs all rows from the `vendors` table. Concatenate vendor name and vendor country
    # as vend_title. Order by vend_title. Leave space in between -- example `ACME (USA)`
    # output columns: vend_title

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_name || ' (' || vend_country || ')' AS vend_title FROM vendors ORDER BY vend_title;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex22():
    # Write an SQL statement that SELECTs all rows from the `orderitems` table where order number is 20005. 
    # Display an extra calculated column called `expanded_price` that is the result of quantity multiplied by item_price.
    # Round the value to two decimal places. 
    # output columns: prod_id, quantity, item_price, expanded_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, quantity, item_price, ROUND(quantity * item_price, 2) AS expanded_price FROM orderitems WHERE order_num = 20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex23():
    # Write an SQL statement that SELECTs all rows from the `orders` table where the order date is between 
    # 2005-09-13 and 2005-10-04
    # output columns: order_num, order_date
    # https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT order_num, order_date FROM orders WHERE order_date BETWEEN '2005-09-13' AND '2005-10-04';"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex24():
    # Write an SQL statement that calculates the average price of all rows in the `products` table. 
    # Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT SUM(prod_price)/COUNT(*) as avg_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex25():
    # Write an SQL statement that calculates the average price of all rows in the `products` table 
    # where the vendor id is 1003 . Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT SUM(prod_price)/COUNT(*) as avg_price FROM products Where vend_id = 1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement



def ex26():
    # Write an SQL statement that counts the number of customers in the `customers` table 
    # Call the count column num_cust
    # output columns: num_cust

    ### BEGIN SOLUTION
    sql_statement = "SELECT COUNT(*) as num_cust FROM customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex27():
    # Write an SQL statement that calculates the max price in the `products` table 
    # Call the max column max_price. Round the value to two decimal places. 
    # output columns: max_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT ROUND(MAX(prod_price), 2) AS max_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex28():
    # Write an SQL statement that calculates the min price in the `products` table 
    # Call the min column min_price. Round the value to two decimal places. 
    # output columns: min_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT ROUND(MIN(prod_price), 2) AS min_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex29():
    # Write an SQL statement that sums the quantity in the `orderitems` table where order number is 20005. 
    # Call the sum column items_ordered
    # output columns: items_ordered

    ### BEGIN SOLUTION
    sql_statement = "SELECT SUM(quantity) AS items_ordered FROM orderitems WHERE order_num = 20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


#---------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------------------------#

# You cannot use Pandas! I will deduct points after manual check if you use Pandas. You CANNOT use the 'csv' module to read the file

# Hint: Ensure to strip all strings so there is no space in them

# DO NOT use StudentID from the non_normalized table. Let the normalized table automatically handle StudentID. 


def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

# conn_non_normalized = create_connection('non_normalized.db')
# sql_statement = "select * from Students;"
# df = pd.read_sql_query(sql_statement, conn_non_normalized)
# display(df)

def normalize_database(non_normalized_db_filename):

    # create connection to the non_normalized database and execute the SELECT statement
    conn_non_normalized = create_connection(non_normalized_db_filename)
    sql_statement = "SELECT * FROM Students;"
    rows = execute_sql_statement(sql_statement, conn_non_normalized)
  

    # create connection to the normalized database and create the Degrees table
    conn_normalized = create_connection('normalized.db', True)
    create_table_sql = '''CREATE TABLE Degrees
                        (Degree text PRIMARY KEY)'''
    create_table(conn_normalized, create_table_sql)

    # insert values into Degrees table
    for row in rows:
        insert_degrees(conn_normalized, (row[2].strip(),))

    # create the Exams table
    create_table_sql = '''CREATE TABLE Exams
                        (Exam text,
                        Year integer,
                        PRIMARY KEY (Exam))'''
    create_table(conn_normalized, create_table_sql)

    # insert values into Exams table
    for row in rows:
        exam_names = [name.strip() for name in row[3].split(',')]
        exam_dict = {}
        for exam_name in exam_names:
            exam_number = exam_name.split()[0]
            year = int(exam_name.split()[-1].strip('()'))
            exam_dict[exam_number] = year
        insert_exams(conn_normalized,exam_dict)   


    # create the Students table
    create_table_sql = '''CREATE TABLE Students
                        (StudentID integer PRIMARY KEY,
                        First_Name text,
                        Last_Name text,
                        Degree text,
                        FOREIGN KEY (Degree) REFERENCES Degrees(Degree))'''
    create_table(conn_normalized, create_table_sql)

    # # insert values into Students table
    for row in rows:
        degree = row[2].strip()
        first_name, last_name = [name.strip() for name in row[1].strip().split(',')]
        insert_students(conn_normalized, (first_name, last_name, degree))

    # create the StudentExamScores table
    create_table_sql = '''CREATE TABLE StudentExamScores
                        (PK integer PRIMARY KEY,
                        StudentID integer,
                        Exam text,
                        Score integer,
                        FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
                        FOREIGN KEY (Exam) REFERENCES Exams(Exam))'''
    create_table(conn_normalized, create_table_sql)

    # insert values into StudentExamScores table
    for row in rows:
        student_id = row[0]
        degree = row[3].split(',')[0].split()[1].strip()
        print(degree)
        exam_names = [name.strip() for name in row[3].split(',')]
        for j in range(len(exam_names)):
            exam_num = exam_names[j].split()[0]
            score = int(row[4].split(',')[j])
            insert_student_exam_scores(conn_normalized, (student_id, exam_num, score))

    conn_non_normalized.close()
    conn_normalized.close()


def insert_degrees(conn, values):
    sql_statement = f'''
        INSERT OR IGNORE INTO Degrees (Degree) VALUES(?) 
    '''
    cur = conn.cursor()
    cur.execute(sql_statement, values)
    conn.commit()
    
    
def insert_exams(conn, values):
    sql_statement = '''
        INSERT INTO Exams (Exam, Year) VALUES(:exam, :year)
    '''
    cur = conn.cursor()
    for exam, year in values.items():
        try:
            cur.execute(sql_statement, {'exam': exam, 'year': year})
        except sqlite3.IntegrityError:
            print(f"Error: Exam {exam} for year {year} already exists in the database.")
    conn.commit()

    
    
def insert_students(conn, values):
    sql_statement = '''
        INSERT INTO Students (First_Name, Last_Name, Degree) VALUES(?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql_statement, values)
    conn.commit()
    
    
def insert_student_exam_scores(conn, values):
   sql_statement = '''
       INSERT INTO StudentExamScores(StudentID, Exam, Score) VALUES(?, ?, ?)
    '''
   cur = conn.cursor()
   cur.execute(sql_statement, values)
   conn.commit()
   
 



# conn_normalized = create_connection('normalized.db')


def ex30(conn):
    # Write an SQL statement that SELECTs all rows from the `Exams` table and sort the exams by Year
    # output columns: exam, year
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Exam, Year FROM Exams ORDER BY Year, Exam;"
   
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
    return sql_statement




def ex31(conn):
    # Write an SQL statement that SELECTs all rows from the `Degrees` table and sort the degrees by name
    # output columns: degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Degree FROM Degrees ORDER BY Degree;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex32(conn):
    # Write an SQL statement that counts the numbers of gradate and undergraduate students
    # output columns: degree, count_degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Degree, COUNT(Degree) AS count_degree FROM Students GROUP BY Degree;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex33(conn):
    # Write an SQL statement that calculates the exam averages for exams; sort by average in descending order.
    # output columns: exam, year, average
    # round to two decimal places
    
    
    ### BEGIN SOLUTION
    # sql_statement = " Select Exams.Exam, Exams.year, round(avg(StudentExamScores.score),2) as average from Exams inner join StudentExamScores on Exams.Exam = StudentExamScores.Exam group by Exams.Exam order by average desc;"
    sql_statement = "Select exams.exam, exams.year, round(avg(StudentExamScores.score),2) as average from exams inner join studentExamScores on exams.exam = StudentExamScores.exam group by exams.exam order by average desc"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex34(conn):
    # Write an SQL statement that calculates the exam averages for degrees; sort by average in descending order.
    # output columns: degree, average 
    # round to two decimal places
    
    ### BEGIN SOLUTION
    sql_statement = " SELECT Students.Degree as Degree,round(avg(StudentExamScores.score),2) as average From studentExamScores inner join students on studentExamScores.studentId = students.studentId group by degree order by average desc;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement

def ex35(conn):
    # Write an SQL statement that calculates the exam averages for students; sort by average in descending order. Show only top 10 students
    # output columns: first_name, last_name, degree, average
    # round to two decimal places
    # Order by average in descending order
    # Warning two of the students have the same average!!!
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Students.Last_name as First_Name, Students.First_name as Last_Name, Students.Degree, round(avg(StudentExamScores.score),2) as average From StudentExamScores inner join Students on StudentExamScores.StudentID = Students.StudentID group by Students.StudentID order by average desc Limit 10"
    ### END SOLUTION 
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement
