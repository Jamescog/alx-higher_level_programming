#!/usr/bin/python3
"""
    prints all City objects
"""


from sqlalchemy import create_engine
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(State.id == City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
