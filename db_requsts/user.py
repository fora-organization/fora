from models import (
    User,
    Session
)

def  get_all_users():
    with Session() as session:
        return session.query(User).all()