from typing import Optional
from exceptions import InvalidTokenException    
from fastapi.security import APIKeyHeader
from fastapi import Depends

api_key_header = APIKeyHeader(name="Token", auto_error=False)

def get_greeting():
    return "Hello, World! from Depends"

def get_query_params(page: Optional[int] = None):
   return {"page": page}

def get_path_params(user_id: int):
    return {"user_id": user_id}

def get_token(token: str = Depends(api_key_header)):
    if not token or token != "1234":
        raise InvalidTokenException()
    return {"token": token}
