import logging
from typing import Any
from uuid import UUID

from databases import Database
from databases.interfaces import Record
from models import Job
from pypika import Query, Table
from repositories.query import format_where_in_list
from repositories.util import fmt_query_log


def serialize_job(job: Job, columns: tuple[str]) -> tuple[Any]:
    serialised_job = tuple(getattr(job, field) for field in columns)
    return serialised_job


def deserialize_job(row: Record) -> Job:
    return Job(
        id=row._mapping["id"],
        name=row._mapping["name"],
        created_date=row._mapping["created_date"],
    )


def deserialize_jobs(rows: list[Record]) -> Job:
    # TODO: consider using map(deserialize_job, rows) when connection.execute returns an iterator instead of a list
    return [deserialize_job(row) for row in rows]


# TODO: make sure the logging is the same as the fastAPI logging
# TODO: look into structured logs

# note: the format logging.warn("thing = %s", object) is a specific format for logging so won't generate the message unless this log is sent
# TODO: use this format for logs everywhere
# TODO: write a doc for coding guidelines like this
# TODO: consider using f strings for logs in python3.12, it might be support for the better performance with f strings then

# TODO: pull generic parts out into a separate CRUDRepository class

# TODO: check whether the way queries are built might allow sql injection
# option 1: figure out how to use parameterised queries with lists https://github.com/kayak/pypika/issues/113
# option 2: find some other way to escape job_ids
# option 2.1: ideally we would see if connection can give a way to excape job_ids, so it will be aware of the driver to the database
# option 2.2: see https://github.com/kayak/pypika/issues/3


class JobsRepository:
    def __init__(
        self,
        database: Database,
        table: Table = Table("jobs"),
    ):
        self.database = database
        self.table = table
        # TODO: consider adding a self.columns and referencing that elsewhere

    async def create_table(self):
        # TODO: use the query builder
        query = """
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_date TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
        async with self.database as db:
            async with db.transaction():
                await db.execute(query)

    async def create(self, job: Job) -> Job:
        """
        Store a Job in the database

        Parameters:
            job (Job): The job to store

        Returns:
            Job: The stored job
        """
        # TODO: implement this then add it back to the docstring
        # Raises:
        #     ResourceAlreadyExistsException: If the job already exists
        #     ResourceNotFoundException: If the job does not exist
        # TODO: consider ResourceAlreadyExistsException idempotent instead

        logging.info("Create")

        # TODO: rewrite this now that serialize_job returns a dict
        columns = (
            "id",
            "name",
            "created_date",
        )
        query = (
            Query.into(
                self.table,
            )
            .columns(
                columns,
            )
            .insert(serialize_job(job, columns=columns))
        )
        logging.info(" - query = %s", query)

        # Must use this instead of prior system to connect
        # TODO: use this syntax for connections everywhere
        # TODO: check if the transactions automatically rollback errors
        async with self.database as db:
            async with db.transaction():
                await db.execute(query=str(query))
                logging.info(" - job = %s", job)
                return job

    async def read(
        self,
        job_ids: list[UUID] | None = None,
    ) -> list[Job]:
        """
        Read a list of jobs from the database

        Parameters:
            job_ids (list[UUID] | None): The job IDs to read. If None then returns all jobs

        Returns:
            jobs (list[Job]): The jobs that were read
        """
        # TODO: implement this then add it back to the docstring
        # Raises:
        #     ResourceNotFoundException: If any requested jobs do not exist

        # TODO: consider to do if a subset of resources fail to be read
        # current option: raise ResourceNotFoundException with the failing IDs in the description so the requester can update their requests

        # TODO: consider making a separate ResourcesNotFoundException for plural failures. look up rest conventions

        # TODO: check whether we need the datetime(created_date,'utc') as created_date if we're handling things in deserialize_job?
        #       - extra duplication or at the very least mixing conserns.
        #       - could open us up to more issues if this is done inconsistently elsewhere.

        # TODO: write tests

        logging.info("Read")
        logging.info(" - job_ids = %s", job_ids)

        query = f"""
            SELECT
                id,
                name,
                datetime(created_date,'utc') as created_date
            FROM 
                jobs
            """
        if job_ids:
            query += f"""
                WHERE 
                    id
                IN 
                    {format_where_in_list(job_ids)}
                """
        query += f";"

        # TODO: consider using textwrap.dedent()
        logging.info(" - query = %s", fmt_query_log(query))

        async with self.database as db:
            async with db.transaction():
                # note: we're using connection.execute instead of database.fetch_one
                # because database.fetch_one will spin up a connection on the fly
                # instead of using any reserved pools of connections

                if job_ids is None:
                    rows = await db.fetch_all(query)
                else:
                    rows = await db.fetch_all(
                        query, {str(i): str(job_ids[i]) for i in range(len(job_ids))}
                    )
                logging.info(" - rows = %s", rows)

                jobs = deserialize_jobs(rows)
                logging.info(" - jobs = %s", jobs)
                return jobs

    # Update
    async def update(
        self,
        job: Job,
    ) -> Job:
        """
        Update a job in the database

        Parameters:
            job (Job): The job to update. a row with job.id should exist in the database, and all other mutable fields will be updated to match job

        Returns:
            updated_job (list[Job]): The job as it currently is in the database
        """
        # logging.info("Update")
        # logging.info(" - job = %s", job)

        # # TODO: rewrite this now that serialize_job returns a dict
        # updated_columns = ("name",)

        # query = Query.update(
        #     self.table,
        # )

        # for column in updated_columns:
        #     query = query.set(column, getattr(job, column))

        # query = query.where(
        #     self.table.id == job.id,
        # )

        # logging.info(" - query = %s", query)

        # TODO: decide - do we want batch updates?
        # TODO: write the query
        # TODO: consider how we want to handle partial updates
        # TODO: get the rows
        # TODO: log the action
        # TODO: return the rows
        # TODO: raise ResourceNotFoundExceptions
        # TODO: write tests
        # TODO: implement this then add it back to the docstring
        # Raises:
        #     ResourceNotFoundException: If any requested jobs do not exist

        # TODO: consider to do if a subset of resources fail to be read
        # current option: raise ResourceNotFoundException with the failing IDs in the description so the requester can update their requests

        # TODO: consider making a separate ResourcesNotFoundException for plural failures. look up rest conventions

        # TODO: check whether we need the datetime(created_date,'utc') as created_date if we're handling things in deserialize_job?
        #       - extra duplication or at the very least mixing conserns.
        #       - could open us up to more issues if this is done inconsistently elsewhere.

        # TODO: write tests

        # Grab connection from pool
        # TODO: use this syntax for connections everywhere
        # async with self.database as db:
        #     async with db.transaction():
        #         await db.execute(str(query))
        #         rows = self.read([job.id])
        #         logging.info(" - rows = %s", rows)

        #         job = deserialize_jobs(rows[0])
        #         logging.info(" - job = %s", job)
        #         return job
        pass

    # Delete
    async def delete(self, job_id: UUID) -> None:
        # TODO: write a docstring
        # TODO: write the query
        # TODO: get the rows
        # TODO: log the action
        # TODO: return the rows
        # TODO: raise ResourceNotFoundExceptions
        # TODO: write tests
        pass
