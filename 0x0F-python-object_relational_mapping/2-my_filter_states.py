#!/usr/bin/python3
"""
Query made by user input
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name='{}';".format(argv[4])
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
