from sqlite3 import connect

with connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()

#
# cur.execute('''SELECT *
#                     FROM Customer
#                     LIMIT 3''')
#
# print(cur.fetchall())
#
# cur.execute('''SELECT *
#                     FROM Invoice
#                     WHERE BillingCity == "Paris" ''')
#
# print(cur.fetchall())
#
# cur.execute(''' SELECT SUM(Total)
#                 FROM Invoice''')
#
# print(cur.fetchall())
#
# cur.execute(''' SELECT MIN(InvoiceDate)
#                     FROM Invoice''')
#
# print(cur.fetchall())
#
cur.execute('''SELECT MAX(InvoiceDate)
                FROM Invoice ''')

print(cur.fetchall())
