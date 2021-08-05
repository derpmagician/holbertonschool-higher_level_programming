#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(host="localhost",
                           user=argv[1],
                           port=3306,
                           passwd=argv[2],
                           db=argv[3])

    cursor = conn.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    conn.close()
