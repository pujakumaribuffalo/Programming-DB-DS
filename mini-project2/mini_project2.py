### Utility Functions
import pandas as pd
import sqlite3
from sqlite3 import Error

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


def create_table(conn, create_table_sql, drop_table_name=None):
    
    if drop_table_name: # You can optionally pass drop_table_name to drop the table. 
        try:
            c = conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" % (drop_table_name))
        except Error as e:
            print(e)
    
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

def step1_create_region_table(data_filename, normalized_database_filename):
    conn = create_connection(normalized_database_filename)

    # Create Region table
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS Region (
            RegionID INTEGER PRIMARY KEY NOT NULL,
            Region TEXT NOT NULL
        );
    """
    create_table(conn, create_table_sql, "Region")

    # Read the data
    with open(data_filename, 'r') as f:
        header = f.readline()
        regions = set()
        for line in f:
            values = line.strip().split("\t")
            if len(values) < 4:
                continue
            regions.add(values[4])

    # Insert the data
    for i, region in enumerate(sorted(regions)):
        sql = f"""
            INSERT INTO Region (RegionID, Region)
            VALUES ({i+1}, '{region}');
        """
        execute_sql_statement(sql, conn)

    conn.commit()
    conn.close()


    ### END SOLUTION

def step2_create_region_to_regionid_dictionary(normalized_database_filename):
    conn = create_connection(normalized_database_filename)
    sql_statement = '''
        SELECT RegionID, Region FROM Region
    '''
    rows = execute_sql_statement(sql_statement, conn)
    conn.close()

    region_to_regionid = {}
    for row in rows:
        region_to_regionid[row[1]] = row[0]

    return region_to_regionid


def step3_create_country_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    # create the connection and cursor to the normalized database
    with sqlite3.connect(normalized_database_filename) as conn:
        cur = conn.cursor()
        region_to_regionid_dict = step2_create_region_to_regionid_dictionary(normalized_database_filename)
        
        # create the country table
        cur.execute('''CREATE TABLE IF NOT EXISTS Country
                     ([CountryID] INTEGER PRIMARY KEY,
                     [Country] TEXT NOT NULL,
                     [RegionID] INTEGER NOT NULL,
                     FOREIGN KEY(RegionID) REFERENCES Region(RegionID));''')
        
        # read the data file and insert the data into the country table
        country_region_combo = set()
        with open(data_filename, 'r') as file:
            next(file)  # skip the header row
            for line in file:
                fields = line.strip().split('\t')
                country_name, region_name = fields[3], fields[4]
                country_region_combo.add((country_name,region_name))
              
            for i, combo in enumerate(sorted(country_region_combo)):
                country_id = i+1
                country = combo[0]
                region_id = region_to_regionid_dict[combo[1]]
                cur.execute('''INSERT INTO Country (CountryID, Country, RegionID)
                           VALUES (?, ?, ?)''', (country_id, country, region_id))
        # commit the changes to the database
        conn.commit()




def step4_create_country_to_countryid_dictionary(normalized_database_filename):
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    sql_statement = '''
        SELECT CountryID, Country FROM Country
    '''
    rows = execute_sql_statement(sql_statement, conn)
    conn.close()

    country_to_countryid = {}
    for row in rows:
        country_to_countryid[row[1]] = row[0]

    return country_to_countryid 


    ### END SOLUTION
        


def step5_create_customer_table(data_filename, normalized_database_filename):
    # Create the Customer table in the normalized database
    with sqlite3.connect(normalized_database_filename) as conn:
        cursor = conn.cursor()

        # Create the Country to CountryID dictionary
        country_to_countryid_dict  = step4_create_country_to_countryid_dictionary(normalized_database_filename)

        # Create the Customer table
        cursor.execute("""
            CREATE TABLE Customer (
                CustomerID INTEGER PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Address TEXT NOT NULL,
                City TEXT NOT NULL,
                CountryID INTEGER NOT NULL,
                FOREIGN KEY (CountryID) REFERENCES Country (CountryID)
            )
        """)
        data = []
        # Populate the Customer table with data from the customer file
        with open(data_filename, "r") as f:
            next(f)  # skip the header row
            # data = [line.strip().split(',') for line in f]
            # data.sort(key=lambda x: (x[0]))
            # Insert the customer data into the Customer table
            for line in f:
                fields = line.strip().split('\t')
                # Parse customer information
                name_parts = fields[0].split()
                first_name = name_parts[0]
                last_name = " ".join(name_parts[1:]) if len(name_parts) > 2 else name_parts[1]
                address = fields[1]
                city = fields[2]
                country_name = fields[3]

                # Look up the country ID for the current customer
                country_id = country_to_countryid_dict[country_name]
                data.append([first_name, last_name, address, city, country_id])
        data.sort(key=lambda x: (x[0], x[1]))
        for row in data:
             cursor.execute("""
                    INSERT INTO Customer (FirstName, LastName, Address, City, CountryID)
                    VALUES (?, ?, ?, ?, ?)
                """, (row[0], row[1], row[2], row[3], row[4]))
        conn.commit()



def step6_create_customer_to_customerid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    sql_statement = '''
        SELECT CustomerID, FirstName, LastName FROM Customer
    '''
    rows = execute_sql_statement(sql_statement, conn)
    conn.close()

    customer_to_customerid = {}
    for row in rows:
        customer_to_customerid[row[1]+ " " + row[2]] = row[0]

    return customer_to_customerid

    ### END SOLUTION
        
import sqlite3

def step7_create_productcategory_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    # Connect to the normalized database
    conn = sqlite3.connect(normalized_database_filename)
    cursor = conn.cursor()

    # Find the distinct product categories
    with open(data_filename, 'r') as f:
        # Skip the header row
        next(f)
        categories = set()
        for line in f:
            line_items = line.strip().split('\t')
            category_description = line_items[7].split(';')
            category = line_items[6].split(';')
            categories.update(zip(category, category_description))
           
        

    # Create the product category table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProductCategory (
            ProductCategoryID INTEGER PRIMARY KEY,
            ProductCategory TEXT NOT NULL,
            ProductCategoryDescription TEXT NOT NULL
        )
    """)

    # Populate the product category table with the distinct product categories
    for i, (category, category_description) in enumerate(sorted(categories)):
        cursor.execute("""
            INSERT INTO ProductCategory (ProductCategoryID, ProductCategory, ProductCategoryDescription)
            VALUES (?, ?, ?)
        """, (i+1, category, category_description ))

    conn.commit()
    conn.close()



def step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    sql_statement = '''
        SELECT ProductCategoryID, ProductCategory FROM ProductCategory
    '''
    rows = execute_sql_statement(sql_statement, conn)
    conn.close()

    productcategory_to_productcategoryid = {}
    for row in rows:
        productcategory_to_productcategoryid[row[1]] = row[0]

    return productcategory_to_productcategoryid

    ### END SOLUTION
 

def step9_create_product_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

        
    # Create the Country to CountryID dictionary
    productcategory_to_productcategoryid_dict  = step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename)
    # print(type(productcategory_to_productcategoryid_dict))
    # print(productcategory_to_productcategoryid_dict)
    # Connect to the normalized database
    conn = sqlite3.connect(normalized_database_filename)
    cursor = conn.cursor()

    # Create the product category table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product (
            ProductID INTEGER PRIMARY KEY,
            ProductName TEXT NOT NULL,
            ProductUnitPrice REAL NOT NULL,
            ProductCategoryID INTEGER NOT NULL,
            FOREIGN KEY (ProductCategoryID) REFERENCES ProductCateogry (ProductCategoryID)
        )
    """)
    count = 0
    #print("*" * 60)
    # Find the distinct products
    with open(data_filename, 'r') as f:
        # Skip the header row
        next(f)
        products = set()
        for line in f:
            # if count >= 1 : break
            # count = count + 1
            line_items = line.strip().split('\t')
            #print("ProductName: ", line_items[5])
            ProductName = line_items[5].split(';')
            ProductUnitPrice = line_items[8].split(';')
            #print("ProductUnitPrice: ", line_items[8])
            ProductCategory = line_items[6].split(';')
            products.update(zip(ProductName, ProductUnitPrice, ProductCategory))

   #print("*" * 60)    

    # Populate the product table with the distinct product
    for i, (ProductName, ProductUnitPrice, ProductCategory) in enumerate(sorted(products)):
        cursor.execute("""
            INSERT INTO Product (ProductID, ProductName, ProductUnitPrice, ProductCategoryID)
            VALUES (?, ?, ?, ?)
        """, (i+1, ProductName, ProductUnitPrice, productcategory_to_productcategoryid_dict[ProductCategory]))

    conn.commit()
    conn.close()




def step10_create_product_to_productid_dictionary(normalized_database_filename):
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    sql_statement = '''
        SELECT * FROM Product
    '''
    rows = execute_sql_statement(sql_statement, conn)
    conn.close()

    product_to_productid = {}
    for row in rows:
        product_to_productid[row[1]] = row[0]

    return product_to_productid

    ### END SOLUTION
        

def step11_create_orderdetail_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    from datetime import datetime

    # Create the Country to CountryID dictionary
    product_to_productid_dict  = step10_create_product_to_productid_dictionary(normalized_database_filename)
    customer_to_customerid_dict = step6_create_customer_to_customerid_dictionary(normalized_database_filename)

    # Connect to the normalized database
    conn = sqlite3.connect(normalized_database_filename)
    cursor = conn.cursor()

    # Create the OrderDetail table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS OrderDetail (
            OrderID INTEGER PRIMARY KEY,
            CustomerID INTEGER NOT NULL,
            ProductID INTEGER NOT NULL,
            OrderDate INTEGER NOT NULL,
            QuantityOrdered INTEGER NOT NULL,
            FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID),
            FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
        )
    """)

    # figure out the orders
    with open(data_filename, 'r') as f:
        # Skip the header row
        next(f)
        orders = []
        # Just for debugging
        entries_count = 0
        for line in f:
            cust_id = []
            ProductName = []
            # Just for debugging
            entries_count = entries_count + 1
            line_items = line.strip().split('\t')
    
            full_name = line_items[0].split(';') # derive CustomerId from name_parts using dict
            cust_id.append(customer_to_customerid_dict[full_name[0]])
            
            # print("Iter: {} full_namepK: {} cust_id: {}\n".format(entries_count, full_name, cust_id))
            ProductName = line_items[5].split(',')[0].split(';') # derive ProductId with the help of dict
            # print("Iter {} ProductNameRK count: {}\n".format(entries_count, len(ProductName)))


            OrderDate = line_items[10].split(';')
            # print("Iter {} OrderDatepK count: {}\n".format(entries_count, len(OrderDate),))
            formatted_OrderDate = []
            for order_date in OrderDate:
                formatted_OrderDate.append(datetime.strptime(order_date, '%Y%m%d').strftime('%Y-%m-%d'))
            #print("iter {} count {} formatted_OrderDatepK: {}\n".format(entries_count, len(formatted_OrderDate), formatted_OrderDate))

            QuantityOrderded = line_items[9].split(';')
            # print("iter {} QuantityOrderdedpK count {}\n".format(entries_count, len(QuantityOrderded)))

            cust_id = cust_id * len(ProductName)
            orders.append(zip(cust_id, ProductName, formatted_OrderDate, QuantityOrderded))

    # print("*" * 60)
    # print("entries_count : ", entries_count)    

    # Populate the OrderDetail table
    #for i, (cust_id, ProductName, formatted_OrderDate, QuantityOrderded) in enumerate(sorted(orders, key = lambda x: x[0])):
    idx = 1
    for order in orders:
        for cust_id, ProductName, formatted_OrderDate, QuantityOrderded in order:
            cursor.execute("""
                INSERT INTO OrderDetail (OrderID, CustomerID, ProductID, OrderDate, QuantityOrdered)
                VALUES (?, ?, ?, ?,?)
            """, (idx, cust_id, product_to_productid_dict[ProductName], formatted_OrderDate, int(QuantityOrderded)))
            idx = idx + 1

    conn.commit()
    conn.close()

    ### END SOLUTION


def ex1(conn, CustomerName):
    
    # Simply, you are fetching all the rows for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # ProductName
    # OrderDate
    # ProductUnitPrice
    # QuantityOrdered
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement = f"""
    SELECT c.FirstName || ' ' || c.LastName AS Name, 
       p.ProductName,
       od.OrderDate,
       p.ProductUnitPrice,
       od.QuantityOrdered,
       ROUND(od.QuantityOrdered * p.ProductUnitPrice, 2) AS Total
    FROM OrderDetail AS od
    INNER JOIN Product AS p ON p.ProductID = od.ProductID
    INNER JOIN Customer AS c ON c.CustomerID = od.CustomerID
    WHERE c.FirstName || ' ' || c.LastName = '{CustomerName}'
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement



    

def ex2(conn, CustomerName):
    
    # Simply, you are summing the total for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement = f"""
    SELECT c.FirstName || ' ' || c.LastName AS Name, 
       ROUND(SUM(od.QuantityOrdered * p.ProductUnitPrice), 2) AS Total
    FROM OrderDetail AS od
    JOIN Product AS p ON p.ProductID = od.ProductID
    JOIN Customer AS c ON c.CustomerID = od.CustomerID
    WHERE c.FirstName || ' ' || c.LastName = '{CustomerName}'
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex3(conn):
    
    # Simply, find the total for all the customers
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION
    sql_statement = f"""
    SELECT c.FirstName || ' ' || c.LastName AS Name, 
       ROUND(SUM(od.QuantityOrdered * p.ProductUnitPrice), 2) AS Total
    FROM OrderDetail AS od
    JOIN Product AS p ON p.ProductID = od.ProductID
    JOIN Customer AS c ON c.CustomerID = od.CustomerID
    GROUP BY c.FirstName, c.LastName
    ORDER BY Total DESC;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex4(conn):
    
    # Simply, find the total for all the region
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, Country, and 
    # Region tables.
    # Pull out the following columns. 
    # Region
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """
    SELECT r.Region,
       ROUND(SUM(od.QuantityOrdered * p.ProductUnitPrice), 2) AS Total
    FROM OrderDetail AS od
    JOIN Product AS p ON p.ProductID = od.ProductID
    JOIN Customer AS c ON c.CustomerID = od.CustomerID
    JOIN Country AS cn ON cn.CountryID = c.CountryID
    JOIN Region AS r ON r.RegionID = cn.RegionID
    GROUP BY r.Region
    ORDER BY Total DESC
    """
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex5(conn):
    
    # Simply, find the total for all the countries
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, and Country table.
    # Pull out the following columns. 
    # Country
    # CountryTotal -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """
    SELECT cn.Country,
       ROUND(SUM(p.ProductUnitPrice * od.QuantityOrdered)) AS CountryTotal
    FROM OrderDetail AS od
    JOIN Product AS p ON p.ProductID = od.ProductID
    JOIN Customer AS c ON c.CustomerID = od.CustomerID
    JOIN Country AS cn ON cn.CountryID = c.CountryID
    GROUP BY cn.Country
    ORDER BY CountryTotal DESC
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement


def ex6(conn):
    
    # Rank the countries within a region based on order total
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    ### BEGIN SOLUTION

    sql_statement = """
    SELECT r.Region, c.Country, ROUND(SUM(od.QuantityOrdered * p.ProductUnitPrice)) AS CountryTotal, 
       RANK() OVER (PARTITION BY r.Region ORDER BY SUM(od.QuantityOrdered * p.ProductUnitPrice) DESC) AS CountryRegionalRank
    FROM OrderDetail AS od
    JOIN Product AS p ON p.ProductID = od.ProductID
    JOIN Customer AS cus ON cus.CustomerID = od.CustomerID
    JOIN Country AS c ON c.CountryID = cus.CountryID
    JOIN Region AS r ON r.RegionID = c.RegionID
    GROUP BY r.Region, c.Country
    ORDER BY r.Region ASC
    """
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement



def ex7(conn):
    
   # Rank the countries within a region based on order total, BUT only select the TOP country, meaning rank = 1!
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    # HINT: Use "WITH"
    ### BEGIN SOLUTION

    sql_statement = """
        WITH cte AS (
            SELECT 
                R.region AS Region, 
                C.Country AS Country, 
                ROUND(SUM(P.ProductUnitPrice * OD.QuantityOrdered)) AS CountryTotal,
                RANK() OVER (PARTITION BY R.Region ORDER BY SUM(P.ProductUnitPrice * OD.QuantityOrdered) DESC) AS CountryRegionalRank
            FROM OrderDetail AS OD
            JOIN Product AS P ON OD.ProductID = P.ProductID
            JOIN Customer AS CM ON OD.CustomerID = CM.CustomerID
            JOIN Country AS C ON CM.CountryID = C.CountryID
            JOIN Region AS R ON C.RegionID = R.RegionID
            GROUP BY R.Region, C.Country
        )
        SELECT 
            Region,
            Country,
            CountryTotal,
            CountryRegionalRank
        FROM cte
        WHERE CountryRegionalRank = 1
        ORDER BY Region ASC;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex8(conn):
    
    # Sum customer sales by Quarter and year
    # Output Columns: Quarter,Year,CustomerID,Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    ### BEGIN SOLUTION

    sql_statement = """
        WITH customer_sales AS (
            SELECT 
                CustomerID,
                CAST(strftime('%Y', OrderDate) AS INTEGER) AS Year,
                CASE 
                   WHEN strftime('%m', OrderDate) IN ('01', '02', '03') THEN 'Q1' 
                   WHEN strftime('%m', OrderDate) IN ('04', '05', '06') THEN 'Q2' 
                   WHEN strftime('%m', OrderDate) IN ('07', '08', '09') THEN 'Q3' 
                   ELSE 'Q4' 
                END AS Quarter,
                ROUND(SUM(P.ProductUnitPrice * OD.QuantityOrdered)) AS Total
            FROM OrderDetail AS OD
            JOIN Product AS P ON OD.ProductID = P.ProductID
            GROUP BY CustomerID, Year, Quarter
        )
        SELECT 
            Quarter,
            Year,
            CustomerID,
            ROUND(Total) AS Total
        FROM customer_sales
        ORDER BY Year, Quarter, CustomerID
    """
    
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement







def ex9(conn):
    
    # Rank the customer sales by Quarter and year, but only select the top 5 customers!
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    # HINT: You can have multiple CTE tables;
    # WITH table1 AS (), table2 AS ()
    ### BEGIN SOLUTION

    sql_statement = """
        WITH customer_sales AS (
            SELECT 
                CustomerID,
                CAST(strftime('%Y', OrderDate) AS INTEGER) AS Year,
                CASE 
                   WHEN strftime('%m', OrderDate) IN ('01', '02', '03') THEN 'Q1' 
                   WHEN strftime('%m', OrderDate) IN ('04', '05', '06') THEN 'Q2' 
                   WHEN strftime('%m', OrderDate) IN ('07', '08', '09') THEN 'Q3' 
                   ELSE 'Q4' 
                END AS Quarter,
                ROUND(SUM(P.ProductUnitPrice * OD.QuantityOrdered)) AS Total
            FROM OrderDetail AS OD
            JOIN Product AS P ON OD.ProductID = P.ProductID
            GROUP BY CustomerID, Year, Quarter
        ),
        customer_sales_ranked AS (
            SELECT 
                Quarter,
                Year,
                CustomerID,
                ROUND(Total) AS Total,
                RANK() OVER (PARTITION BY Quarter, Year ORDER BY Total DESC) AS CustomerRank
            FROM customer_sales
        )
        SELECT 
            Quarter,
            Year,
            CustomerID,
            Total,
            CustomerRank
        FROM customer_sales_ranked
        WHERE CustomerRank <= 5
        ORDER BY Year, Quarter, CustomerRank
    """
    
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex10(conn):
    
    # Rank the monthly sales
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    ### BEGIN SOLUTION

    sql_statement = """
        WITH monthly_sales AS (
            SELECT 
                strftime('%m', OrderDate) AS MonthNum,
                SUM(ROUND(P.ProductUnitPrice * OD.QuantityOrdered)) AS Total
            FROM OrderDetail AS OD
            JOIN Product AS P ON OD.ProductID = P.ProductID
            GROUP BY MonthNum
        ),
        monthly_sales_ranked AS (
            SELECT 
                Month,
                Total,
                RANK() OVER (ORDER BY Total DESC) AS TotalRank
            FROM (
                SELECT 
                    MonthNum,
                    Total,
                    CASE 
                        WHEN MonthNum = '01' THEN 'January' 
                        WHEN MonthNum = '02' THEN 'February' 
                        WHEN MonthNum = '03' THEN 'March' 
                        WHEN MonthNum = '04' THEN 'April' 
                        WHEN MonthNum = '05' THEN 'May' 
                        WHEN MonthNum = '06' THEN 'June' 
                        WHEN MonthNum = '07' THEN 'July' 
                        WHEN MonthNum = '08' THEN 'August' 
                        WHEN MonthNum = '09' THEN 'September' 
                        WHEN MonthNum = '10' THEN 'October' 
                        WHEN MonthNum = '11' THEN 'November' 
                        ELSE 'December' 
                    END AS Month
                FROM monthly_sales
            )
        )
        SELECT 
            Month,
            Total,
            TotalRank
        FROM monthly_sales_ranked
        ORDER BY TotalRank
    """
    
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex11(conn):
    
    # Find the MaxDaysWithoutOrder for each customer 
    # Output Columns: 
    # CustomerID,
    # FirstName,
    # LastName,
    # Country,
    # OrderDate, 
    # PreviousOrderDate,
    # MaxDaysWithoutOrder
    # order by MaxDaysWithoutOrder desc
    # HINT: Use "WITH"; I created two CTE tables
    # HINT: Use Lag

    ### BEGIN SOLUTION


    sql_statement = """
        WITH customer_orders AS (
            SELECT
                O.CustomerID,
                C.FirstName,
                C.LastName,
                CM.Country,
                O.OrderDate,
                LAG(O.OrderDate) OVER (PARTITION BY O.CustomerID ORDER BY O.OrderDate) AS PreviousOrderDate
            FROM OrderDetail AS O
            JOIN Customer AS C ON O.CustomerID = C.CustomerID
            JOIN Country AS CM ON CM.CountryID = C.CountryID
        ),
        customer_order_gaps AS (
            SELECT
                CustomerID,
                FirstName,
                LastName,
                Country,
                OrderDate,
                PreviousOrderDate,
                JULIANDAY(OrderDate) - JULIANDAY(PreviousOrderDate) AS DaysWithoutOrder
            FROM
                customer_orders
        )
        SELECT
            CustomerID,
            FirstName,
            LastName,
            Country,
            OrderDate,
            PreviousOrderDate,
            Max(DaysWithoutOrder) AS MaxDaysWithoutOrder
        FROM
            customer_order_gaps
        GROUP BY
            CustomerID
        ORDER BY
            MaxDaysWithoutOrder DESC
    """
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement
