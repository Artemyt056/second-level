import sqlite3

with sqlite3.connect('part_data_1.db3') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS "data"(
                         id INTEGER PRIMARY KEY UNIQUE,
                         contract_code NUMBER,
                         Client code TEXT UNIQUE,
                         credit_code NOT NULL,
                         date_of_issue NOT NULL, 
                         sum NOT NULL) ''')
