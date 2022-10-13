#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = []
    make_query = session.query(State).all()

    for state in make_query:
        if 'a' in state.name:
            states.append(state.id)
    for state_id in states:
        obj = session.query(State).filter(State.id == state_id).first()
        session.delete(obj)
    session.commit()
