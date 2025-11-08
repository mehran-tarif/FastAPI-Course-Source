from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

app = FastAPI()

def get_greeting():
    return "Hello, World! from Depends"

def get_query_params(page: Optional[int] = None):
    return {"page": page}

def get_path_params(user_id: int):
    return {"user_id": user_id}

def get_token(token: int ):
    if token != 1234:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"token": token}


@app.get("/{user_id:int}")
def read_root(
    message: str = Depends(get_greeting),
    query_params: dict = Depends(get_query_params),
    path_params: dict = Depends(get_path_params),
    token: str = Depends(get_token)
):
    return {
        "Message": message, 
        "query_params": query_params, 
        "path_params": path_params,
        "token": token
        }




