from pydantic import BaseModel


class CreateUserDto(BaseModel):
    firstname: str
    surname: str
    password: str
