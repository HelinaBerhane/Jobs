import sqlite3
import pytest
from unittest.mock import MagicMock
from backend.util import dict_factory


@pytest.fixture
def mock_database_connection():
    # Mocking the cursor and row objects
    cursor = MagicMock(spec=sqlite3.Cursor)
    row = MagicMock(spec=sqlite3.Row)
    cursor.description = [("id", None), ("name", None), ("created_date", None)]
    return cursor, row


def test_dict_factory(mock_database_connection):
    cursor, row = mock_database_connection
    row_data = (1, "Test Job", "2024-03-07")
    row.__getitem__.side_effect = row_data.__getitem__

    result = dict_factory(cursor, row)

    assert result == {"id": 1, "name": "Test Job", "created_date": "2024-03-07"}


def test_dict_factory_empty_row(mock_database_connection):
    cursor, row = mock_database_connection

    # Mocking an empty row by returning None for all indices
    row.__getitem__.side_effect = lambda _: None

    result = dict_factory(cursor, row)

    # Check if the result is an empty dictionary with default values
    assert result == {"id": None, "name": None, "created_date": None}
