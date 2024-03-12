from databases import Database
from databases.interfaces import Record
from example_repo.qb import compile_sql, Parameter
from models import Job
from uuid import uuid4, UUID
from datetime import datetime, timezone
from typing import Optional, List


def parse_job(row: Record) -> Job:
    created_date = datetime.fromisoformat(row["created_date"])
    created_date = created_date.replace(tzinfo=timezone.utc)
    return Job(
        id=UUID(row.id),
        created_date=created_date,
        name=row.name
    )


class JobsRepository:
    def __init__(self, database: Database):
        self.database = database

    async def create(self, job: Job) -> Job:
        query = "INSERT INTO jobs (id, created_date, name) VALUES (:id, :created_date, :name)"
        async with self.database as db:
            await db.execute(query, job.model_dump())
        return job

    async def read_one(self, job_id: UUID) -> Optional[Job]:
        query = "SELECT id, created_date, name FROM jobs WHERE id = :id"
        async with self.database as db:
            row = await db.fetch_one(query, {"id": job_id})
        return parse_job(row) if row else None

    async def read_many(self, job_ids: Optional[List[UUID]] = None) -> List[Job]:
        if job_ids:
            placeholders = ','.join([str(job_id) for job_id in job_ids])
            query = f"SELECT id, created_date, name FROM jobs WHERE id IN ({placeholders})"
            async with self.database as db:
                rows = await db.fetch_all(query)
        else:
            query = "SELECT id, created_date, name FROM jobs"

            async with self.database as db:
                rows = await db.fetch_all(query)
        return [parse_job(row) for row in rows]

    async def update_partial(self, job: Job) -> Optional[Job]:
        update_fields = ', '.join(
            [f"{key} = :{key}" for key in job.model_dump(exclude={"id"})])
        values = job.model_dump()
        query = f"UPDATE jobs SET {update_fields} WHERE id = :id"
        async with self.database as db:
            await db.execute(query, values)
        return job

    async def delete(self, job_id: UUID) -> None:
        query = "DELETE FROM jobs WHERE id = :id"
        async with self.database as db:
            await db.execute(query, {"id": job_id})
