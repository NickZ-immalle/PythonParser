import csv
import sqlite3
import os

db_filename = 'FakeAppsDatabase.sqlite3'

def parser():
        conn = sqlite3.connect(db_filename) 
        c = conn.cursor()

        c.execute("CREATE TABLE FakeApps (id integer primary key, name text, category text, downloads integer, price real)")


        with open('FakeApps.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                c.execute("INSERT INTO FakeApps VALUES (? , ?, ?, ?, ?)" , (row['id'], row['name'], row['category'], row['downloads'], row['price'] ))

        conn.commit()
        c.close()

if __name__ == "__main__":
    if os.path.isfile(db_filename):
        os.remove(db_filename)
    parser()
    