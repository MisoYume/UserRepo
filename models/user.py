from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Float,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    __table_args__ = (
        UniqueConstraint(
            'name', 
            'surname', 
            name='uq_user_name_surname'
        ),
    )

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    weight = Column(Float, nullable=False)
    birth_date = Column(Date, nullable=False)

    def __repr__(self):
        return (
            f"<User(user_id={self.user_id}, "
            f"name='{self.name}', surname='{self.surname}')>"
        )