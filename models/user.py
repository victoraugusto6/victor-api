from sqlmodel import SQLModel, Field
from typing import Optional, List


# --- model ---

class User(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    username: str
    password: str


# --- serializers ---

class UserOut(SQLModel):
    username: str


class UserIn(SQLModel):
    username: str
    password: str
    confirm_password: str


UserList = List[UserOut]
