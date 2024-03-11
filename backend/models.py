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
    # team_name: str
    # title: str
    # company_id: UUID
    # job_spec: Document?

    # status = OneOf(
    #     "Reference Only",
    #     "Just Seen (Default)",
    #     "Interviewing",
    #     "Applied",
    #     "Dropped",
    #     "Ghosted",
    #     "Rejected",
    #     "Offered",
    #     "Declined Offer",
    #     "Accepted Offer",
    # )
    # TODO: consider whether to store this in a separate table and let users add statuses or more hardcoded

    # min_salary: Decimal
    # max_salary: Decimal
    # offered_salary: Decimal

    # derived_fields
    # average_salary_calculated: Decimal with some rounding and inflation adjustments
    # predicted_min_salary: Decimal based on traits or company
    # predicted_max_salary: Decimal based on traits or company


# future classes
# class Company:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   name: str
#   flexibility_location: Enum(
#       in_office = 1,
#       hybrid = 2,
#       remote = 3,
#       fully_optional = 4,
#   )
#   flexibility_hours: Enum(
#       flexible,
#       strict,
#   )


# class Location:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   name: str


# class CompanyOffice:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   name: str
#   rating: Enum(
#       NICE = 1
#       OK = 2
#       GROSS = 3
#   )

#   relationships
#   company_id: UUID
#   location_id: UUID


# class Interview:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   type: str


# class Flags:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   description: str
#   severity: Enum(
#       GREEN = 1
#       YELLOW = 2
#       RED = 3
#   )


# class Traits:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

#   mutable fields
#   description: str
#   severity: Enum(
#       GREEN = 1
#       YELLOW = 2
#       RED = 3
#   )

#   derived fields
#   average_min_salary: Decimal calculated from JobTraits and CompanyTraits
#   average_max_salary: Decimal calculated from JobTraits and CompanyTraits

# class JobTraits:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)

# class CompanyTraits:
#   immutable fields
#   id: UUID = Field(default_factory=uuid4)
#   created_date: datetime = Field(default_factory=datetime_now)
