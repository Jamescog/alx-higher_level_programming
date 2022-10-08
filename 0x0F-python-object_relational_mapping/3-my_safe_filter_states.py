#!/usr/bin/python3
"""
Making query that is safe from sql injection
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb


    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s;", (argv[4],))
    result = cursor.fetchall()

    for row in result:
        print(row)
