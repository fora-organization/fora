from models import (
    User,
    Session
)

def  get_all_users():
    with Session() as session:
        return session.query(User).all()
    
def get_user_for_id(id):
    with Session() as session:
        user = session.query(User).where(id == User.id).one_or_none()

        if user:
            return user
        else:
            return None