"""
Test goes here

"""

from mylib.query import query

def test_query():
    assert query("SELECT COUNT(*) FROM DB_Email_Names.db") == 31
