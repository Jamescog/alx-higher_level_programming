"""
LIST EVERY THING FROM DATABASE ON THE TABELE "states"
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection= MySQLdb.connect(user=argv[0], passwd=argv[1], db=argv[2], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for row in result:
        print(i)
    
