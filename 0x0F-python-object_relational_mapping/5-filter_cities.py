#!/usr/bin/python3
"""Takes in the name of a state as an argument
   and lists all cities of that state, using the database hbtn_0e_4_usa
   """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE "
                "state_id = (SELECT id FROM states WHERE name = %s)"
                " ORDER BY id ASC", [sys.argv[4]])

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()
