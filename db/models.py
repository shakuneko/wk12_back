from .database import Base
from sqlalchemy import Column, Integer, String


class DbProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    name = Column(String)
    image = Column(String)
    description_long = Column(String)
