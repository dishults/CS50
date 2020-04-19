#!/usr/bin/env python3
"""
Program that imports data from a CSV spreadsheet into PostgreSQL database
"""
import os, sys, csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")
    try:
        assert len(sys.argv) == 2
        with open(sys.argv[1]) as file:
            books = csv.reader(file)
            engine = create_engine(os.getenv("DATABASE_URL"))
            db = scoped_session(sessionmaker(bind=engine))
            next(books)
            for isbn, title, author, year in books:
                db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
            db.commit()
                
    except AssertionError:
        print("Usage: python3 import.py books.csv")

if __name__ == "__main__":
    main()