#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                "COLLATE utf8mb4_bin ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
