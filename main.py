from fastapi import FastAPI, HTTPException
from typing import Optional,List
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str
 

@app.get('/dict')
async def get_dict() -> dict[str,str]:
    return {"name":"Bekdaulet","age":"19"}



posts = [
    {"id": 1, "title":"news1","content":"content 1"},
    {"id": 2, "title":"news2", "content":"content 2"},
    {"id": 3, "title":"news3", "content":"content 3"}

]

# @app.get('/posts')
# async def get_posts() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'],title=post['title'],content=post['content']))
#     return post_objects

@app.get('/posts')
async def get_posts() -> List[Post]:
    return [Post(**post)for post in posts]

@app.get('/posts/{id}')
async def get_posts(id:int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post

    raise HTTPException(status_code=404,detail='Post not found')


@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404,detail='Post not found')

    else:
        return {"data":"No post id"}