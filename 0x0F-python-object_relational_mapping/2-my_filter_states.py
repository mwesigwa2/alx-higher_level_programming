#!/usr/bin/python3
"""
    script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' \
            ORDER BY id ASC".format(argv[4]))
    state_rows = cursor.fetchall()
    for row in state_rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
