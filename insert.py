# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
con = lite.connect('mes.db')
with con:
    cur = con.cursor()    
    cur.execute("INSERT INTO vote VALUES(%s,%s,%s,%s,%s,%s)"%(theme,username,choices,deadline,votedmember,owner))

con.close()