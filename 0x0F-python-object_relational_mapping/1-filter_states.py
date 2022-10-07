#!/usr/bin/python3
"""
Execute sql query "SELECT * FROM states WHERE name LIKE 'N%'"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    result = cursor.fetchall()

    for row in result:
        print(row)
