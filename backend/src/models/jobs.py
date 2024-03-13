from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Job(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))

    name: Optional[str]
