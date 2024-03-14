from typing import Annotated, Optional
from uuid import UUID

from exceptions import handle_http_exceptions
from fastapi import APIRouter, Query
from models import Job
from repositories.jobs import JobsRepository

from api.db import DatabaseDep

router = APIRouter(
    prefix="/jobs",
)


@router.post("")
@handle_http_exceptions
async def create_job(
    database: DatabaseDep,
    job: Job,
) -> Job:
    jobs_repository = JobsRepository(database)
    return await jobs_repository.create(job)


@router.get("")
@handle_http_exceptions
async def get_jobs(
    database: DatabaseDep,
    job_ids: Annotated[Optional[list[UUID]], Query()] = None,
) -> list[Job]:
    # note: Query() means this needs to go in the query of the request, not the body
    # because get requests shouldn't have a json body
    jobs_repository = JobsRepository(database)
    return await jobs_repository.read_many(job_ids)


@router.get("/{job_id}")
@handle_http_exceptions
async def get_job(
    database: DatabaseDep,
    job_id: UUID,
) -> Job:
    jobs_repository = JobsRepository(database)
    job = await jobs_repository.read_one(job_id)
    return job


@router.delete("/{job_id}")
@handle_http_exceptions
async def delete_job(
    database: DatabaseDep,
    job_id: UUID,
) -> None:
    jobs_repository = JobsRepository(database)
    await jobs_repository.delete(job_id)


@router.patch("")
@handle_http_exceptions
async def update_job(
    database: DatabaseDep,
    job: Job,
) -> Job:
    # TODO: add job_id to the update path
    jobs_repository = JobsRepository(database)
    return await jobs_repository.update(job)
