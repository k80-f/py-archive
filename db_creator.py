# db_creator.py
 
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()
 
 
class Owner(Base):
    __tablename__ = "owners"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
 
    def __repr__(self):
        return "{}".format(self.name)
 
 
class Title(Base):
    """"""
    __tablename__ = "titles"
 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    subject_matter = Column(String)
    publisher = Column(String)
    media_type = Column(String)
 
    owner_id = Column(Integer, ForeignKey("owners.id"))
    owner = relationship("Owner", backref=backref(
        "owners", order_by=id))
 
# create tables
Base.metadata.create_all(engine)