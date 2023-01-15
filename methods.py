import uuid
from datetime import timedelta

from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload

import models, schemas



def get_tours(db: Session):
    tours = db.query(models.Tournaments).all()
    parts = db.query(models.Participants).options(joinedload(models.Participants.team), joinedload(
        models.Participants.user)).all()
    return [schemas.TourView.from_model(x, parts) for x in tours]


# получение списка участников по айди турнира (клик по названию турнира в таблице турниров)
def get_participants_by_tour(db: Session, t_guid: uuid.UUID):
    parts = db.query(models.Participants).filter(
        models.Participants.tour_guid == t_guid).options(joinedload(models.Participants.team),
                                                         joinedload(models.Participants.user)).order_by(models.Participants.place).all()
    return [schemas.PartView.from_model(x) for x in parts]

# получение команды по ее айди (клик по названию команды на странице участника)
def get_team_by_part(db: Session, t_guid):
    links = db.query(models.TeamUserLink).filter(
        models.TeamUserLink.team_guid == t_guid).options(joinedload(models.TeamUserLink.team),
                                                         joinedload(models.TeamUserLink.user)).all()
    if links:
        team = links[0].team
        users = [x.user for x in links]
        return(schemas.TeamView(name=team.name, users=users))


# получение юзера по его айди
def get_user_by_part(db: Session, u_guid):
    return db.query(models.Users).filter(models.Users.guid == u_guid).first()

# получение списка решенных задач участника (клик по участнику в таблице участников турнира)


def get_completed_by_part(db: Session, p_guid: uuid.UUID):
    com = db.query(models.CompletedTask).filter(models.CompletedTask.participant_guid==p_guid).options(joinedload(models.CompletedTask.task)).all()
    return [schemas.ComView(**x.dict(), name=x.task.name, t_guid=x.task.guid) for x in com]

# получение данных задачи по ее айди
def get_task_by_guid(db: Session, t_guid: uuid.UUID):
    return db.query(models.Tasks).filter(models.Tasks.guid==t_guid).all()

# вывод среднего кол-ва решенных задач по всем турнирам (вывести на главной страние перед таблицей турниров)
def get_medim_tasks(db: Session):
    parts = db.query(models.Participants).all()
    coms = db.query(models.CompletedTask).all()
    return schemas.MediumTaskView(value=(len(coms) // len(parts)))

# вывод среднего призового фонда (вывести на главной страние перед таблицей турниров)
def get_medim_prize(db: Session):
    tours = db.query(models.Tournaments).all()
    sum1 = 0
    for x in tours:
        sum1 += x.prize_fond
    return schemas.MediumPrizeView(value=(sum1 // len(tours)))