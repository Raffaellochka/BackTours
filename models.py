import uuid
from datetime import timedelta
from typing import Optional

from database import Base

from sqlmodel import Field, Column, Relationship, SQLModel


class Tournaments(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    prize_fond: int
    name: str
    type: str


class Tasks(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    text: str
    name: str


class Users(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str


class Teams(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str


class TeamUserLink(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    team_guid: uuid.UUID = Field(foreign_key=Teams.guid, nullable=True)
    user_guid: uuid.UUID = Field(foreign_key=Users.guid, nullable=True)
    user: Optional[Users] = Relationship()
    team: Optional[Teams] = Relationship()


class Participants(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    place: int
    team_guid: uuid.UUID = Field(foreign_key=Teams.guid, nullable=True)
    user_guid: uuid.UUID = Field(foreign_key=Users.guid, nullable=True)
    tour_guid: uuid.UUID = Field(foreign_key=Tournaments.guid, nullable=True)
    user: Optional[Users] = Relationship()
    team: Optional[Teams] = Relationship()

class CompletedTask(SQLModel, table=True):
    guid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    task_guid: uuid.UUID = Field(foreign_key=Tasks.guid, nullable=True)
    participant_guid: uuid.UUID = Field(foreign_key=Participants.guid, nullable=True)
    time: timedelta
    task: Optional[Tasks] = Relationship()