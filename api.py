from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
# pydantic is libary and basemodel is class
app=FastAPI()


API_KEY="1234abcds"

@app.middleware("http")
async def check_api_key(request,call_next):
    key=request.headers.get("X_API_KEY")
    if(key!=API_KEY):
        return JSONResponse(status_code=401,content={"error":"unauthorized"})
    return await call_next(request)
@app.get("/welcome")
def welcome():
    return {"message":"Welcome to FastAPI app!"}


@app.get("/user")
def user_profile():
    return {
        "Name":"Pavithra",
        "Course":"AIDS",
        "Year":"3rd"
    }


@app.get("/user/{user_id}")
def user_profile(user_id:int):
    if (user_id==1):
        return {
               "Name":"Pavithra",
                "Course":"AIDS",
                "Year":"3rd"
        }
    else:
        return{
               "Name":f"Pavithra{user_id}",
                "Course":"AIML",
                "Year":"3rd"
        }
        
        
class User(BaseModel):
    name:str
    age:int
    email:str

users=[]
        
@app.post("/users")

def create_user(user:User):
    users.append(user.dict())
    return {"message":"user added successfully","total_user":len(users)}