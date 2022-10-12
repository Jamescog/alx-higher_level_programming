#!/usr/bin/python3
"""
    this script make query based on user input
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    query = """
                SELECT cities.id, cities.name, states.name
                FROM cities JOIN states ON cities.state_id = states.id
                WHERE states.name = '{}'
            """.format(argv[4])
    cursor.execute(query)
    result = cursor.fetchall()

    print(", ".join([state[1] for state in result]))
