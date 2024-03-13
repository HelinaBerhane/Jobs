from typing import Optional

from databases import Database
from fastapi import Depends
from typing_extensions import Annotated

db: Optional[Database] = None


def init_db(database: Database):
    """
    Sets the global database instance.

    This should be called only once, when the application starts to configure the database.

    Args:
        database (Database): The database instance.

    Raises:
        Exception: If the global database instance is already defined.
    """
    global db
    if db is not None:
        # TODO: replace with more specific exception
        raise Exception("Database already initialized")
    db = database


def get_db() -> Database:
    """
    Gets the global database instance.

    Returns:
        The global database instance if defined.

    Raises:
        Exception: If the global database instance is not defined.
    """
    global db
    if not db:
        # TODO: replace with more specific exception
        raise Exception("Database not initialized")
    return db


DatabaseDep = Annotated[Database, Depends(get_db)]
