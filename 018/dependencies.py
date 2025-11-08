from services.user import UserService
from fastapi import Request
# from functools import lru_cache

# user_service = UserService()

# def get_user_service():
#     return user_service

# @lru_cache
# def get_user_service():
#     return UserService()

def get_user_service(request: Request):
    return request.app.state.user_service