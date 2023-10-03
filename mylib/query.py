"""Query the database"""

import sqlite3


def query(query):
    """Query the database for the top 5 rows of the DB_Email_Names table"""
    conn = sqlite3.connect("NamesDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.execute("SELECT COUNT(*) FROM NamesDB.db")
    Name_Results = cursor.fetchall()
    
    print("Top number of observations NamesDB table:")
    print(cursor.fetchall())
    conn.close()
    return Name_Results


