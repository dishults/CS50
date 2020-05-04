#!/usr/bin/env python3
"""
Program that imports data from a CSV spreadsheet
"""
import sys, csv, sqlite3
from sqlite3 import Error

def create_student(conn, student):
    """
    Create a new student
    """
        
    sql = ''' INSERT INTO students(first,middle,last,house,birth)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()

    name = student[0].split()
    if len(name) == 3:
        cur.execute(sql, [name[0], name[1], name[2], student[1], student[2]])
    elif len(name) == 2:
        cur.execute(sql, [name[0], "NULL", name[1], student[1], student[2]])
    return cur.lastrowid

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        with open(sys.argv[1]) as file:
            csv = csv.reader(file)
            database = "students.db"
            conn = sqlite3.connect(database)
            next(csv)
            with conn:
                for student in csv:
                    create_student(conn, student)
    except AssertionError:
        print("Usage: python3 import.py characters.csv")
    except Error as e:
        print(e)