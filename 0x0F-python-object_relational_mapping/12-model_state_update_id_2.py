#!/usr/bin/python3
"""
    changes the name of a State object
"""


from sys import argv
from zipapp import create_archive
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb//{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    temp = session.get(2)
    temp.name = 'New Mexico'
    session.commit()
    session.close()
