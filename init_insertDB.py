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

def insertMember(group_name, user_name):
    db = sqlite3.connect('prog_comp.db')
    cur = db.cursor()
    sql = "INSERT INTO members VALUES(?, ?)"

    cur.execute(sql, (group_name, user_name))
    db.commit()
    db.close()

#   Insert Groupe Datas
insertGroup('teamA', 'private')
insertGroup("藤田", "private")
insertGroup("渋谷先生", "public")
insertGroup("M2", "public")

#   Insert User Datas
insertUser("樋口", "higuchi", "higuchi@hi.is.kit.ac.jp")
insertUser("吉川", "yoshikawa", "yoshikawa@hi.is.kit.ac.jp")
insertUser("宇谷", "utani", "utani@hi.is.kit.ac.jp")
insertUser("藤田", "fujita", "fujita@hi.is.kit.ac.jp")
insertUser("渋谷先生", "shibuya", "shibuya@hi.is.kit.ac.jp")
insertUser("安井", "yasui", "yasui@hi.is.kit.ac.jp")
insertUser("茂松", "shigematsu", "shigematsu@hi.is.kit.ac.jp")

#   Insert Groupe Datas
insertMember('teamA', "樋口")
insertMember('teamA', "吉川")
insertMember('teamA', "宇谷")
insertMember('teamA', "藤田")
insertMember('藤田', "樋口")
insertMember('藤田', "藤田")
insertMember('渋谷先生', "樋口")
insertMember('渋谷先生', "渋谷先生")
insertMember('M2', "樋口")
insertMember('M2', "安井")
insertMember('M2', "茂松")
