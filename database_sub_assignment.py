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

with conn:
    cur = conn.cursor()#1
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('information.docx'))
    conn.commit()
    cur = conn.cursor()#2
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('Hello.txt'))
    conn.commit()
    cur = conn.cursor()#3
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('myImage.png'))
    conn.commit()
    cur = conn.cursor()#4
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('myMovie.mpg'))
    conn.commit()
    cur = conn.cursor()#5
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('World.txt'))
    conn.commit()
    cur = conn.cursor()#6
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('data.pdf'))
    conn.commit()
    cur = conn.cursor()#7
    cur.execute("insert into tbl_assignment(col_num1) values (?)", \
                ('myPhoto.jpg'))
    conn.commit()
con.close()


    
