#!/usr/bin/env python3
"""
Program that prints a list of students for a given house in alphabetical order
"""

import sys, sqlite3
from sqlite3 import Error

def select_hogwarts_house(conn, house):
    """
    Print students
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE house=? ORDER BY last ASC, first ASC", (house,))
 
    for row in cur.fetchall():
        print(row[1], end=" ")
        if row[2] != "NULL":
            print(row[2], end=" ")
        print(row[3] + ", born", row[5])

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        database = "students.db"
        conn = sqlite3.connect(database)
        with conn:
            select_hogwarts_house(conn, sys.argv[1])
    except AssertionError:
        print("Usage: python3 roster.py Gryffindor")
    except Error as e:
        print(e)