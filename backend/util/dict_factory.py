from sqlite3 import Cursor, Row
from typing import Dict, Any


def dict_factory(cursor: Cursor, row: Row) -> Dict[str, Any]:
    """
    This function is used to convert the sqlite3.Row object to a dictionary.

    Usage:
        ```python
        connection.row_factory = dict_factory
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        for job in jobs:
            print(job['id'], job['name'], job['created_date'])
        ```

    Parameters:
        cursor (sqlite3.Cursor): The cursor object.
        row (sqlite3.Row): The row object.

    Returns:
        Dict[str, Any]: The row object keyed by column names.
    """

    return {column[0]: row[index] for index, column in enumerate(cursor.description)}
