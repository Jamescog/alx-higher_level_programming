#!/usr/bin/pyhton3
"""
    this script lists all cities from database hbtn_oe_4_usa
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         port=3306)
    cursor = db.cursor()
    query = """ SELECT cities.id, cities.name, states.name
                FROM cities JOIN states ON cities.state_id = states.id;
            """
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
