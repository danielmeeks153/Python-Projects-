fileList = ['information.docx', 'Hello.txt','myImage.png','mymovie','World.txt','data,pdf','myPhotol.jpg']

import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_num1 TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment.db')

for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_assignment (col_num1) VALUES (?)", (x,))
            print(x)

conn.close()


    
