import sqlite3


def dBConnection():
    # create a connection
    db_connection = sqlite3.connect("quiz.db")

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    cur = db_connection.cursor()
    
    return cur
