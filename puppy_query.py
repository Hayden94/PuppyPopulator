from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from puppies_database_setup import Base, Shelter, Puppy
import datetime


engine = create_engine('sqlite:///puppy.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def query_1():
    # query all puppies and return results in alphabetical order
    result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()

    for item in result:
        print item[0]

def query_2():
    '''query all of the puppies that are less than
    6 months old organized by the youngest first'''
    today = datetime.date.today()
    sixMonthsAgo = today - datetime.timedelta(days = 183)

    name = Puppy.name
    dob = Puppy.dateOfBirth

    result = session.query(name, dob).filter(dob >= sixMonthsAgo).order_by(dob.desc())

    for item in result:
        print "{p_name}: {p_dob}",format(p_name=item[0], p_dob=item[1])


def query_3():
    # query all puppies weight and return results in asc order
    result = session.query(Puppy.name, Puppy.weight).order_by(Puppies.weight.asc()).all()

    for item in result:
        print item[0], item[1]

def query_4():
    #query all puppies grouped by the shelter in which they are staying
    result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()

    for item in result:
        print item[0].id, item[0].name, item[1]

