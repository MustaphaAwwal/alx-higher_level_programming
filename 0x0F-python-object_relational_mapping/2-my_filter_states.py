#!/usr/bin/python3
"""
filter all states from from the database
and serach
"""
from sys import argv
import MySQLdb

"""
Connection set up
using MySQLdb
"""
if __name__ == '__main__':
    connect = MySQLdb.connect(
            host='localhost',
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connect.close()
