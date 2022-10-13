#!/usr/bin/python3
"""
    Deletes all State objects with a name containing the letter a
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__name__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all = session.query(State).all()
    a_list = []
    for state in all:
        if 'a' in state.name:
            a_list.append(state.id)
    for id in a_list:
        state = session.query(State).get(id)
        session.delete(state)
    session.commit()
