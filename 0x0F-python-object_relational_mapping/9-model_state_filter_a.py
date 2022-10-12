#!/usr/bin/python3
"""
    lists all State objects that contain the letter
"""


from ast import arg
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for obj in result:
        if 'a' in obj.name:
            print('{}: {}'.format(obj.id, obj.name))
