import sqlite3

db = sqlite3.connect('prog_comp.db')

# Create Group Table
cur = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' and name = 'groups' ")
if cur.fetchone() == None:
    sql = "CREATE TABLE groups(group_name verchar(50), group_type verchar(10), port integer)"
    cur.execute(sql)
    db.commit()

# Create User Table
cur = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' and name = 'users' ")
if cur.fetchone() == None:
    sql = "CREATE TABLE users(user_name verchar(50), password verchar(20), address text)"
    cur.execute(sql)
    db.commit()

db.close()
