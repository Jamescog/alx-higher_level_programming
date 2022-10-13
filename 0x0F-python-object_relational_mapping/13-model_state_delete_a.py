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
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    
    for state in states:
        session.delete(state)
    session.commit()
