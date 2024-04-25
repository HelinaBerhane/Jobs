import logging
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from databases import Database
from databases.interfaces import Record
from exceptions import ResourceNotFoundException
from models import Job


def parse_job(row: Record) -> Job:
    created_date = datetime.fromisoformat(row["created_date"])
    created_date = created_date.replace(tzinfo=timezone.utc)
    return Job(
        id=UUID(row["id"]),
        name=str(row["name"]),
        created_date=created_date,
    )


class JobsRepository:
    # TODO: add docstrings

    def __init__(self, database: Database) -> None:
        self.database = database

    async def create(
        self,
        job: Job,
    ) -> Job:
        query = """
            INSERT INTO jobs(
                id,
                name,
                created_date
            ) VALUES(
                :id,
                :name,
                :created_date
            );
            """
        async with self.database as db:
            values = job.model_dump()
            await db.execute(query, values)
        return job

    async def read_one(
        self,
        job_id: UUID,
    ) -> Job:
        # TODO: check whether we need datetime(created_date,'utc') as created_date or not
        query = """
            SELECT
                id,
                name,
                datetime(created_date,'utc') as created_date
            FROM 
                jobs
            WHERE
                id = :id
            ;
            """
        async with self.database as db:
            values = {"id": job_id}
            row = await db.fetch_one(query, values)
            if row is None:
                raise ResourceNotFoundException(
                    message=f"Job not found for ID={job_id}"
                )

        logging.debug(f"Getting Job with ID={job_id}")
        return parse_job(row)

    async def read_many(
        self,
        job_ids: Optional[list[UUID]] = None,
    ) -> list[Job]:
        query = """
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
                    id IN ({','.join(':' + str(i) for i, _ in enumerate(job_ids))})
                ;
                """
        else:
            query += ";"

        if job_ids:
            async with self.database as db:
                values = {str(i): job_id for i, job_id in enumerate(job_ids)}
                rows = await db.fetch_all(query, values)

        else:
            async with self.database as db:
                rows = await db.fetch_all(query)

        if job_ids:
            logging.debug("Getting all Jobs")
        else:
            logging.debug(f'Getting Jobs with IDs={",".join(str(job_ids))}')

        return [parse_job(row) for row in rows]

    async def update(
        self,
        job: Job,
    ) -> Job:
        update_fields = ", ".join(
            [
                f"{key} = :{key}"
                for key in job.model_dump(exclude={"id", "created_date"})
            ]
        )
        query = f"""
            UPDATE jobs
            SET
                {update_fields}
            WHERE
                id = :id
            ;
            """

        async with self.database as db:
            values = job.model_dump(exclude={"created_date"})
            await db.execute(query, values)
            # TODO: handle ResourceNotFoundExceptions
        logging.info(f"Updated Job with ID='{job.id}'")
        return await self.read_one(job_id=job.id)

    async def delete(
        self,
        job_id: UUID,
    ) -> None:
        query = """
            DELETE FROM jobs 
            WHERE
                id = :id
            ;
            """
        async with self.database as db:
            values = {"id": job_id}
            await db.execute(query, values)

            try:
                job = await self.read_one(job_id=job_id)
                if job is not None:
                    logging.info(f"Failed to delete Job with ID='{job_id}'")
                    # TODO: find a better exception
                    raise Exception("Resource not deleted")
            except ResourceNotFoundException:
                logging.info(f"Deleted Job with ID='{job_id}'")
