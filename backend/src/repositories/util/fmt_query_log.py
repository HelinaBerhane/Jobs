import re

import sqlparse


def fmt_query_log(sql: str) -> str:
    """
    Format a query for logging.

    Args:
        sql (str): The query to format.

    Returns:
        str: The formatted query.
    """
    # Get the formatted SQL without newlines
    formatted_sql = sqlparse.format(sql, reindent=False, keyword_case='upper')

    # Remove all newlines
    formatted_sql = formatted_sql.replace('\n', '')

    # Remove consecutive spaces with a single space
    formatted_sql = re.sub(r'\s+', ' ', formatted_sql)

    # Remove leading and trailing spaces
    formatted_sql = formatted_sql.strip()

    return formatted_sql
