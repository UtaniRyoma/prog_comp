import sqlite3

class User:
    """Deal users with db"""
    def __init__(self, user_name, password):
        db = sqlite3.connect('prog_comp.db')
        cur = db.cursor()
        cur.execute("SELECT user_name FROM users WHERE user_name = ? ", user_name)

        if cur.fetchone() == None:
            print ("None such users")
        else:
            cur.execute("SELECT password FROM users WHERE password = ? ", password)
            if cur.fetchone() == None:
                print ("incorrect password")
            else:
                self.name = user_name
                cur.execute("SELECT address FROM users WHERE user_name =  ? ", user_name)
                address = cur.fetchone()
                if address != None:
                    self.address = address[0]
        db.close()

    def getName(self):
        return self.name

    def getAdd(self):
        if self.address == None:
            return ''
        else:
            self.address


def getPort(group_name, user_name = None):
        db = sqlite3.connect('prog_comp.db')
        cur = db.cursor()
        confirmFlag = 1
        if user_name != None:
            # Confirm that the user belongs to the group
            cur.execute("SELECT group_type FROM groups WHERE  group_name = ?", (group_name, ))
            group_type = cur.fetchone()
            if group_type[0] == 'private':
                confirmFlag = 0
                cur.execute("SELECT group_name FROM members WHERE  user_name = ?", (user_name, ))
                for group in cur.fetchall():
                    if group_name == group[0]:
                        confirmFlag = 1
                        break
                if confirmFlag == 0:
                    print ("No such group to which the user belongs ")

        # Extract port-number from "groups" table
        cur.execute("SELECT port FROM groups WHERE group_name = ? ", (group_name, ))
        port = cur.fetchone()
        if confirmFlag == 1:
            if port != None:
                db.close()
                return port[0]
        db.close()
        return None
