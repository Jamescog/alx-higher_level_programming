#!/usr/bin/python3
"""
    adds the State object "Lousiana"
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
