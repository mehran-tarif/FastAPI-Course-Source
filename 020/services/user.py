from exceptions import EmailAlreadyExistsException, UserNotFoundException
from schemas import UserOutput, UserRequest, UserPatchRequest

class UserService:
    def __init__(self):
        self.users = []

    def _get_user_or_404(self, user_id: int):
        existing_user = next((u for u in self.users if u.id == user_id), None)
        if not existing_user:
            raise UserNotFoundException()
        return existing_user
    
    def _email_already_exists(self, email: str):
        if any(u.email == email for u in self.users):
            raise EmailAlreadyExistsException()

    def _email_already_exists_update(self, email: str, existing_user: UserOutput):
        if any(u.email == email and u.email != existing_user.email for u in self.users):
            raise EmailAlreadyExistsException()

    def create_user(self, user: UserRequest):
        self._email_already_exists(user.email)
        new_user = UserOutput(
            id=len(self.users) + 1,
            **user.model_dump()
        )
        self.users.append(new_user)
        return new_user

    def get_users(self):
        return self.users

    def get_user(self, user_id: int):
        return self._get_user_or_404(user_id)

    def update_user(self, user_id: int, user: UserRequest):
        existing_user = self._get_user_or_404(user_id)
        self._email_already_exists_update(user.email, existing_user)
        existing_user.update(user.model_dump())
        return existing_user
    
    def patch_user(self, user_id: int, user: UserPatchRequest):
        existing_user = self._get_user_or_404(user_id)
        self._email_already_exists_update(user.email, existing_user)
        existing_user.update(user.model_dump())
        return existing_user
    
    def delete_user(self, user_id: int):
        self.users.remove(self._get_user_or_404(user_id))