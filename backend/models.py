from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from backend.dates import datetime_now


class Job(BaseModel):
    # immutable fields
    id: UUID = Field(default_factory=uuid4)
    created_date: datetime = Field(default_factory=datetime_now)

    # mutable fields
    name: Optional[str]
