"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the DB_Email_Names table"""
    conn = sqlite3.connect("DB_Email_Names.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM DB_Email_Names.db")
    Name_Results = cursor.fetchall()
    
    print("Top number of observations DB_Email_Names table:")
    print(cursor.fetchall())
    conn.close()
    return Name_Results


