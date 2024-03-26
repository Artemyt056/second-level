from sqlite3 import connect

with connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()

# cur.execute('''SELECT *
#                 FROM Customer
#                 ORDER BY LENGTH(Company) DESC
#                 LIMIT 1''')
#
# print(cur.fetchall())

# cur.execute('''SELECT COUNT(FirstName)
#                 FROM Customer
#                 WHERE Company IS NULL AND Fax IS NULL''')
#
#
# # print(cur.fetchall())
#
cur.execute('''SELECT 
    CASE 
        WHEN substr(Phone, 1, 2) = '+1' THEN 'Північна Америка'
        WHEN substr(Phone, 1, 2) = '+5' THEN 'Південна Америка'
        WHEN substr(Phone, 1, 2) = '+2' THEN 'Африка'
        WHEN substr(Phone, 1, 2) = '+6' THEN 'Австралія'
        WHEN substr(Phone, 1, 2) IN ('+3', '+4', '+7', '+8', '+9') THEN 'Євразія'
        ELSE 'Невідомий континент'
            END AS continent,
            COUNT(*) AS people_count
            FROM Customer
            GROUP BY continent''')


print(cur.fetchall())
