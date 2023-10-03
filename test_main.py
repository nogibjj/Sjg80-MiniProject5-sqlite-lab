"""
Test goes here
"""

from mylib.query import query


def test_query():
    assert query("SELECT value FROM DataSet_withNames ORDER BY value DESC LIMIT 2") == [
        ("Jane Doe",),
        ("John Doe",),
    ]

    pass


def test_extract():
    pass


def test_transform_load():
    pass
