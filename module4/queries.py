"""A BREAKDOWN OF QUERIES REQUIRED FOR SPRINT CHALLENGE"""

create_table = """CREATE TABLE IF NOT EXISTS {} (
                s text,
                x integer,
                y integer)

                """

insert_data = """INSERT INTO {} (s,x,y)
                VALUES ('{}',{},{});
            """

row_count = """SELECT COUNT(*) FROM {}"""

xy_at_least_5 = """SELECT COUNT(*) FROM {} WHERE x >= 5 and y >= 5"""

unique_y = """SELECT COUNT(DISTINCT y) as 'Unique_Y' FROM {}"""

select_table_names = """SELECT name FROM sqlite_master WHERE type='table'
                        ORDER BY name;"""

show_specific_table = """SELECT sql FROM sqlite_master WHERE name='{}';"""

ten_most_expensive = """SELECT ProductName from Product ORDER BY
                        UnitPrice DESC LIMIT 10;"""

average_age = """SELECT AVG(DateDiff) from (SELECT (HireDate - BirthDate)
                 AS DateDiff from Employee)"""

average_age_by_city = """SELECT City, AVG(DateDiff) from (SELECT City,
                         (HireDate - BirthDate) AS DateDiff from Employee)
                         GROUP BY City;"""

ten_most_expensive_suppliers = """SELECT ProductName, CompanyName from
                                  Product JOIN Supplier on
                                  Product.SupplierId = Supplier.Id
                                  ORDER BY UnitPrice DESC LIMIT 10;"""

largest_category = """SELECT max(UniqueProductCount), CategoryName FROM
                      (SELECT CategoryName, CategoryId, UniqueProductCount
                      FROM Category join (SELECT COUNT(Id) as
                      UniqueProductCount, CategoryId from Product
                      GROUP BY CategoryId)
                      catJoin ON Category.Id = catJoin.CategoryId)"""

most_territories = """SELECT Id, FirstName, Count(TerritoryId) As TerritoryCount
                      FROM (SELECT * FROM (SELECT Id, FirstName
                      from Employee) Employee1 JOIN (SELECT EmployeeId,
                      TerritoryId FROM EmployeeTerritory) EmpTerritory
                      ON Employee1.Id = EmpTerritory.EmployeeId)
                      GROUP BY Id ORDER BY TerritoryCount DESC LIMIT 1;"""
