import uuid
from datetime import timedelta
from typing import List, Union, Optional

from pydantic import BaseModel


class TourView(BaseModel):
    guid: uuid.UUID
    name: str
    type: str
    prize_fond: int
    winner: Optional[str]

    @staticmethod
    def from_model(model, parts):
        winner_m = None
        if model.type == 'командный':
            winner_m = list(filter(lambda x: x.tour_guid==model.guid and x.place == 1, parts))[0].team.name
        if model.type == 'индивидуальный':
            winner_m = list(filter(lambda x: x.tour_guid==model.guid and x.place == 1, parts))[0].user.name
        return TourView(**model.dict(), winner=winner_m)
class PartView(BaseModel):
    guid: uuid.UUID
    place: int
    name: str
    type: Optional[str]
    obj_guid: uuid.UUID

    @staticmethod
    def from_model(model):
        type = None
        name = None
        obj_guid = None
        if model.team:
            name = model.team.name
            obj_guid = model.team.guid
            type = 'команда'
        if model.user:
            name = model.user.name
            obj_guid = model.user.guid
            type = 'участник'
        return PartView(**model.dict(), type=type, name=name, obj_guid=obj_guid)


class ComView(BaseModel):
    time: timedelta
    t_guid: uuid.UUID
    name: str

class TaskView(BaseModel):
    text: str
    name: str

class UserView(BaseModel):
    name: str

class TeamView(BaseModel):
    name: str
    users: Optional[List[UserView]]

class MediumTaskView(BaseModel):
    value: int

class MediumPrizeView(BaseModel):
    value: int


