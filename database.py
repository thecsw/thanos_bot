import sqlite3

def init_database(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Universe (Name TEXT, Comment TEXT, State INTEGER DEFAULT 1);")
    conn.commit()
    c.close()
    print("Create table.")
    
def is_logged(conn, username):
    c = conn.cursor()
    args = c.execute("SELECT COUNT(1) FROM Universe WHERE Name = ?;", (str(username),))
    result = list(args.fetchone())[0]
    c.close()
    print("Found? {}".format(result))
    return result

def add_user(conn, username, comment):
    c = conn.cursor()
    c.execute("INSERT INTO Universe (Name, Comment) VALUES (?, ?);", (str(username), str(comment),))
    conn.commit()
    c.close()
    print("Added new user - {}".format(str(username)))

def get_all(conn):
    c = conn.cursor()
    args = c.execute("SELECT Name FROM Universe;")
    result = [x[0] for x in args.fetchall()]
    c.close()
    return result
