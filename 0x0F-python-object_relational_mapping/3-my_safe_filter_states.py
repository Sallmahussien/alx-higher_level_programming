#!/usr/bin/python3
"""Takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                [sys.argv[4]])

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
