# from typing import Optional
#
#
# # def calc(n1: int, n2: Optional[int] = 5) -> int:
# def calc(n1: int, n2: Optional[int] = 5) -> int:
#     return n1 + n2
#
#
# print(calc(2, 3))
# print(calc(2, 2))

### PYDANTIC ###
# from pydantic import BaseModel, Field, validator
# import random
#
#
# class User(BaseModel):
#     username: str
#     password: int = Field(default_factory=lambda: random.randint(1, 10))
#
#     @validator("username")
#     def valdiate_username(cls, v):
#         if v == 'victor':
#             raise ValueError('Não pode ter outro Victor')
#         return v
#
#
# user = User(username='admin')
#
# print(user.username)
# print(user.password)
#
# print(user.json())

from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional

engine = create_engine(url="sqlite:///user.db", echo=False)


class User(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    username: str
    password: str


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
