from pydantic import BaseModel, EmailStr
from .events import Event

class User(BaseModel):
    email:str
    password: str
    events: list[Event] | None = None

class UserSignIn(BaseModel):
    email: str
    password: str