#!/usr/bin/python3
import MySQLdb

from sys import argv


if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                           db=argv[3], port=3306)
    cursor = mydb.cursor()

    query = 'select * from states order by states.id asc'

    cursor.execute(query)

    data_rows = cursor.fetchall()

    for row in data_rows:
        print(row)
