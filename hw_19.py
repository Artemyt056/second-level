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
cur.execute('''SELECT Country, COUNT(*) AS NumberOfCustomers
                FROM Customer
                GROUP BY Country''')

print(cur.fetchall())
