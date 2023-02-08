import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')


def execute_query(connection, query):
    curs = conn.cursor()
    curs.execute(query)
    print(curs.fetchall())
    return curs.fetchall()


expensive_items = '''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''

avg_hire_age = '''
SELECT AVG(HireDate - BirthDate) AS avg_age
FROM Employee;
'''
ten_most_expensive = '''
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN  Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
'''

largest_category = '''
SELECT Category.CategoryName, count(Product.ProductName) as num_prod
FROM Category
JOIN Product
ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY num_prod DESC
LIMIT 1;
'''
queries_list = [expensive_items, avg_hire_age,
                ten_most_expensive, largest_category]

for q in queries_list:
    execute_query(conn, q)
