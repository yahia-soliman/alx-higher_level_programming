#!/usr/bin/python3
"""Usage: 0-select_states.py <mysql_user> <mysql_pass> <db_name>"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    state = argv[4].split(';')[0]
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states\
                WHERE name LIKE BINARY '{state}'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
