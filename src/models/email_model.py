from dataclasses import dataclass
from datetime import datetime
from typing import Annotated

from annotated_types import Ge, Lt
from pydantic import BaseModel, Field, Strict
from src.modules.db import db


@dataclass
class EMAIL:
    TABLE: str = "email_db"


@dataclass
class EMAIL_STATUS:
    CHECKING: str = "checking"
    PROCESSING: str = "processing"
    DONE: str = "done"


class EmailValidate(BaseModel):
    email: Annotated[
        str,
        Strict(),
        Field(
            description="Email address to send the email to",
            pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        ),
    ]
    # 0 ~ 9
    partition: Annotated[int, Field(description="Partition number"), Ge(0), Lt(10)] = 0

    status: Annotated[
        EMAIL_STATUS,
        Field(
            description="Status of the email request",
        ),
    ] = EMAIL_STATUS.CHECKING
    creaded_at: Annotated[datetime, Field(description="Created at timestamp")] = (
        datetime.now()
    )


class EmailModel:
    def insert_email(self, email_request: EmailValidate):
        try:
            # data = email_request.model_dump()
            db[EMAIL.TABLE].insert_one(email_request.model_dump())
        except Exception:
            return False
        return True

    def get_all_email(self):
        try:
            data = db[EMAIL.TABLE].find({})
            return [EmailValidate(**item).model_dump_json() for item in data]
        except Exception:
            raise Exception("Failed to fetch email requests")
