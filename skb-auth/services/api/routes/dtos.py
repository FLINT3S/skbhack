from pydantic import BaseModel


class CreateUserDto(BaseModel):
    login: str
    firstname: str
    surname: str
    password: str


class LoginUserDto(BaseModel):
    login: str
    password: str
