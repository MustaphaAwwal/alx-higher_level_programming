#!/usr/bin/python3
"""
Lists all states with name starting with
N (upper N) from the database
"""
from sys import argv
import MySQLdb

"""
Connection set up
"""
if __name__ == '__main__':
    connection = MySQLdb.connect(
            host="localhost",
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
    )
    db = connection.cursor()
    db.execute("SELECT * FROM states WHERE name IS NOT " +
               "NULL AND LEFT(CAST(name AS BINARY), 1) = 'N' ORDER BY id ASC;")
    query_rows = db.fetchall()

    for row in query_rows:
        print(row)

    db.close()
    connection.close()
