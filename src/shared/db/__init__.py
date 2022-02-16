from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common.path import project_path

from shared.db.models import Base


def connect_to_db(database="ulanoviny"):
    path = project_path(f'{database}.db')
    engine = create_engine(f'sqlite:///{path}')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return engine, Session


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance, True
