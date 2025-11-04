from schemas import UserOutput
from exceptions import EmailAlreadyExistsException, UserNotFoundException

def get_user_or_404(users: list[UserOutput], user_id: int):
    existing_user = next((u for u in users if u.id == user_id), None)
    if not existing_user:
        raise UserNotFoundException()
    return existing_user

def email_already_exists(users: list[UserOutput], email: str):
    if any(u.email == email for u in users):
        raise EmailAlreadyExistsException()

def email_already_exists_update(users: list[UserOutput], email: str, existing_user: UserOutput):
    if any(u.email == email and u.email != existing_user.email for u in users):
        raise EmailAlreadyExistsException()