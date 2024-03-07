import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from uuid import UUID
from typing import Dict, Any

from backend.exceptions import ResourceNotFoundException
from backend.util.dict_factory import dict_factory
from backend.models import Job


def read_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").astimezone(timezone.utc)


def read_job(row: Dict[str, Any]) -> Job:
    return Job(
        id=UUID(row.get("id")),
        name=str(row.get("name")),
        created_date=read_date(str(row.get("created_date"))),
    )


class JobsDB:
    path = "backend/jobs.db"

    def __init__(self) -> None:
        super().__init__()
        self.create_tables()

    def create_tables(self):
        self.create_jobs_table()

    def create_jobs_table(self):
        with closing(sqlite3.connect(self.path)) as connection:
            with closing(connection.cursor()) as cursor:
                connection.execute("PRAGMA foreign_keys = ON")
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS jobs (
                        id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        created_date TEXT DEFAULT CURRENT_TIMESTAMP
                    );
                    """
                )

    def create_job(
        self,
        job: Job,
    ):
        with closing(sqlite3.connect(self.path)) as connection:
            with closing(connection.cursor()) as cursor:
                connection.execute("PRAGMA foreign_keys = ON")
                cursor.execute(
                    """
                    INSERT INTO jobs(
                        id,
                        name,
                        created_date
                    ) VALUES(?,?,?);
                    """,
                    [
                        str(job.id),
                        job.name,
                        job.created_date,
                    ],
                )
                connection.commit()

    def get_jobs(
        self,
    ) -> list[Job]:
        with closing(sqlite3.connect(self.path)) as connection:
            connection.row_factory = dict_factory
            with closing(connection.cursor()) as cursor:
                connection.execute("PRAGMA foreign_keys = ON")
                cursor.execute(
                    """
                    SELECT
                        id,
                        name,
                        datetime(created_date,'utc') as created_date
                    FROM 
                        jobs
                    ;
                    """,
                )

                return [read_job(row) for row in cursor.fetchall()]

    def get_job(
        self,
        job_id: UUID,
    ) -> Job:
        with closing(sqlite3.connect(self.path)) as connection:
            connection.row_factory = dict_factory
            with closing(connection.cursor()) as cursor:
                connection.execute("PRAGMA foreign_keys = ON")
                cursor.execute(
                    """
                    SELECT
                        jobs.id,
                        jobs.name,
                        datetime(jobs.created_date,'utc') as created_date
                    FROM 
                        jobs
                    WHERE
                        jobs.id=?
                    ;
                    """,
                    [
                        str(job_id),
                    ],
                )

                row = cursor.fetchone()
                if row is None:
                    raise ResourceNotFoundException(
                        message=f"Job not found for id={job_id}"
                    )

                return read_job(row)

    def update_job(
        self,
        job: Job,
    ) -> Job:
        with closing(sqlite3.connect(self.path)) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    """
                    UPDATE jobs
                    SET name = ?
                    WHERE id = ?
                    RETURNING *;
                    """,
                    [
                        job.name,
                        str(job.id),
                    ],
                )

                row = cursor.fetchone()
                if row is None:
                    raise ResourceNotFoundException(
                        message=f"Job not found for id={job.id}"
                    )
                connection.commit()

                return Job(
                    id=row[0],
                    name=str(row[1]),
                )

    def delete_job(
        self,
        job_id: UUID,
    ):
        with closing(sqlite3.connect(self.path)) as connection:
            with closing(connection.cursor()) as cursor:
                connection.execute("PRAGMA foreign_keys = ON")
                cursor.execute(
                    """
                    DELETE FROM jobs 
                    WHERE id=?
                    """,
                    [
                        str(job_id),
                    ],
                )
                connection.commit()


jobs_db = JobsDB()
