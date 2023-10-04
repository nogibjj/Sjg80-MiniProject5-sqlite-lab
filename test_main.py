"""
Test goes here
"""

from mylib.query import query

def test_query():
    assert query("SELECT maiden_name FROM NamesDB LIMIT 1") == [ ('Smith',)]
    pass

def test_extract():
    pass

def test_transform_load():
    pass
