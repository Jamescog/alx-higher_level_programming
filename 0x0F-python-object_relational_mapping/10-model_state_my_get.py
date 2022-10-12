#!/usr/bin/python3
"""
    prints the State object with the name passed as arguement
"""


from pydoc import cram
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == '{}'.format(argv[4])).first()
    if result:
        print(result.id)
    else:
        print("Not found")

