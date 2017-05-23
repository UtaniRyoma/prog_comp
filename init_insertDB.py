import sqlite3

def insertGroup(group_name, group_type):
    db = sqlite3.connect('prog_comp.db')
    cur = db.cursor()
    cur.execute('SELECT group_name FROM groups')
    counter = len(cur.fetchall())
    sql = "INSERT INTO groups VALUES(?, ?, ?)"
    # counter = cur.execute('SELECT count(group_name) FROM groups')

    cur.execute(sql, (group_name, group_type, 4100 + counter))
    db.commit()
    db.close()

def insertUser(user_name, password, address):
    db = sqlite3.connect('prog_comp.db')
    cur = db.cursor()
    sql = "INSERT INTO users VALUES(?, ?, ?)"

    cur.execute(sql, (user_name, password, address))
    db.commit()
    db.close()

#   Insert Groupe Datas
insertGroup('teamA', 'public')
insertGroup("樋口", "private")
insertGroup("渋谷先生", "public")

#   Insert User Datas
insertUser("樋口", "higuchi", "higuchi@hi.is.kit.ac.jp")
insertUser("吉川", "yoshikawa", "yoshikawa@hi.is.kit.ac.jp")
