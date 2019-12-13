# part two: northwind database
import sqlite3

# making connection
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# most expensive items
def most_ex():
    A = """
    SELECT ProductName, UnitPrice, SupplierId
    FROM Product
    ORDER BY UnitPrice desc
    LIMIT 10
    """
    curs.execute(A)
    return curs.fetchall()

most_ex()

# part three: sailing northwind
# avg hire age
def avg_age():
    A1 = """
    SELECT AVG(HireDate - BirthDate)
    FROM Employee
    """
    curs.execute(A1)
    return curs.fetchall()

avg_age()

# add supplier to top prods
def suppl_name():
    B = """
    SELECT
    Product.ProductName AS "ProductName",
    Product.UnitPrice AS Price,
    Supplier.CompanyName AS "SupplierName"
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
    curs.execute(B)
    return curs.fetchall()

suppl_name()

def lg_categ():
    B2= """
    SELECT CategoryName
    FROM Category
    WHERE Id = (
    SELECT Product.CategoryId
    FROM Product
    GROUP BY Product.CategoryId
    ORDER BY COUNT (Product.ProductName) DESC
    LIMIT 1)
    """
    curs.execute(B2)
    return curs.fetchall()

lg_categ()

# part four: questions
# 01. the relationship between 'employee' and 'territory'
# is a one-to-many relation. There is one employee to many territories.
# 02. mongodb is useful when you evolve your data overtime.
# It's useful for storing data that is not relational and tabular.
# It is good for transactional store when the performance is
# starting to become a concern.
# 03. Newsql is a class of relational database management systems
# that seek to provide the scalability of Nosql systems for online
# transaction processing workloads while maintaining acid guarantees
# of a traditional database system.
# the 'best of both worlds' per say - it wants to be able to have acid
# guarantees and the ability to still use sql and have horizontal
# scaling which adds relational neccessities to non relational systems.
