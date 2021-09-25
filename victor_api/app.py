"""
victor_api base module.
"""
from fastapi import Depends, FastAPI

from db import Session, get_session, init_db
from models.user import User, UserIn, UserList, UserOut

app = FastAPI(
    title="API de Usuários do Victor", version="0.1.0", on_startup=[init_db]
)


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/user", response_model=UserList)
def list_users(session: Session = Depends(get_session)):
    return session.query(User).all()


@app.post("/user", response_model=UserOut)
def create_user(user: UserIn, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.delete("/user/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    session.delete(user)
    session.commit()
    return {"ok": "Usuário deletado"}
