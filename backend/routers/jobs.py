import logging
from uuid import UUID

from db import jobs_db
from exceptions import handle_http_exceptions
from fastapi import APIRouter
from models import Job

router = APIRouter(
    prefix="/jobs",
)


# Create
@router.post("")
@handle_http_exceptions
async def create_job(
    job: Job,
) -> None:
    jobs_db.create_job(
        job=job,
    )
    logging.info(f"Created '{job.name}'")


# Read one
@router.get("/{job_id}")
@handle_http_exceptions
async def get_job(
    job_id: UUID,
) -> Job:
    job = jobs_db.get_job(job_id)
    logging.debug(f"Getting Job '{job.name}'")
    return job


# Read all
@router.get("")
@handle_http_exceptions
async def get_jobs() -> list[Job]:
    logging.debug("Getting All Jobs")
    return jobs_db.get_jobs()


# Update
# TODO: add an update_job endpoint
# TODO: consider how you would handle updating an optional field to Null while also allowing partial updates


# Delete
@router.delete("/{job_id}")
@handle_http_exceptions
async def delete_job(
    job_id: UUID,
) -> None:
    job = jobs_db.get_job(job_id)
    jobs_db.delete_job(job_id)
    logging.info(f"Deleted '{job.name}'")
