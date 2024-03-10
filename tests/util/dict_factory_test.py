import sqlite3
from unittest.mock import MagicMock

import pytest

from backend.util import dict_factory


@pytest.fixture
def mock_database_connection():
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
