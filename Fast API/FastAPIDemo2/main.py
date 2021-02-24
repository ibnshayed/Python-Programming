from fastapi import FastAPI, Query, Path, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional, List

from app.apis import user

app = FastAPI()

app.include_router(user.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get('/')
async def index():
    return {'message': 'Welcome to FastAPI'}

# with path parameter
@app.get('/{id}')
async def method1(id: int):
    return {'message': F"The path parameter value is = {id}"}


@app.get('/{user_id}')
async def method2(id: int, q: Optional[str] = None):
    return {'message': F"The path parameter value is = {id}"}

@app.get('/{user1_id}')
async def method3(
    id: int, q: Optional[str] = None,
     s: Optional[str] = Query(None, min_length = 1, max_length= 5, regex='^emu')
     ):
    return {'message': F"The path parameter value is = {id}"}

@app.get('/{user2_id}')
async def method4(
    id: int, q: Optional[str] = None,
     s: Optional[str] = Query(..., min_length = 1, max_length= 5, regex='^emu')
     ):
    return {'message': F"The path parameter value is = {id}"}


@app.get('/{user3_id}')
async def method5(
    id: int, q: Optional[str] = None,
     s: Optional[List[str]] = Query(None)
     ):
    return {'message': F"The path parameter value is = {id}"}



@app.get('/{user4_id}')
async def method6(
    id: int,
    q: Optional[str] = None,
    s: Optional[List[str]] = Query(
         None,
         title="Query string",
         description="Description of this api",
         min_length=5
        )
):
    return {'message': F"The path parameter value is = {id}"}


@app.get('/{user5_id}')
async def method7(
    id: int,
    q: Optional[str] = None,
    s: Optional[List[str]] = Query(
         None,
         alias="item-query",
         title="Query string",
         description="Query string for the items to search in the database that have a good match",
         min_length=3,
         max_length=50,
         regex="^fixedquery$",
         deprecated=True,
        )
):
    return {'message': F"The path parameter value is = {id}"}

@app.get('/{user6_id}')
async def method8(*, id: int = Path(..., ge=1), q: Optional[str] = None):
    return {'message': F"The path parameter value is = {id}"}