#!/usr/bin/python3
"""
filter all states from the database
with name starting from N
"""
from sys import argv
import MySQLdb

"""
Connection set up
"""
if __name__ == '__main__':
	connect = MySQLdb.connect(
		host='localhost',
		port=3306, user=argv[1],
		passwd=argv[2],
		db=argv[3],
		charset="utf8"
	)
	cur = connect.cursor()
	cur.execute("SELECT * FROM states WHERE name IS NOT " +
				"NULL AND LEFT(CAST(name AS BINARY), 1) = 'N' ORDER BY id ASC;")
	rows = cur.fetchall()

	for row in rows:
		print(row)

	cur.close()
	connect.close()
