
"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,
ingred_FPro,avg_FPro_products,avg_distance_root,
ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

# Load the csv file and insert into a new sqlite3 database
def load(dataset="../Sjg80-MiniProject5-sqlite-lab/data/DataSet_withNames.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

     # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(
        open(dataset, newline="", encoding="iso-8859-1"), delimiter=","
    )
    conn = sqlite3.connect("NamesDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS NamesDB")
    c.execute(
        """CREATE TABLE NamesDB 
        (Rank,Name, Platform, Publisher, Developer, 
        Critic_Score, User_Score, Total_Shipped, Year)"""
    )
    # insert
    c.executemany("INSERT INTO NamesDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "NamesDB.db"
