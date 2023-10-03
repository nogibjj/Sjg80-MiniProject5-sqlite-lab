import sqlite3
import csv
import os

# Load the csv file and insert into a new sqlite3 database
def load(dataset="data/DataSet_withNames.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("DB_Email_Names.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS DB_Email_Names")
    c.execute(
        """CREATE TABLE DB_Email_Names (
            id,
            gender,
            birthdate,
            maiden_name,
            lname,
            fname,
            address,
            city,
            state,
            zip,
            phone,
            email,
            cc_type,
            cc_number,
            cc_cvc,
            cc_expiredate
        )"""
    )
    # insert
    c.executemany(
        """INSERT INTO DB_Email_Names VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "DB_Email_Names.db"

