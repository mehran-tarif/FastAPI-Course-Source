from fastapi import FastAPI , Depends
from dependencies import get_greeting, get_query_params, get_path_params, get_token

app = FastAPI()

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




