#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3],
                           port=3306)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    mydb.close()
