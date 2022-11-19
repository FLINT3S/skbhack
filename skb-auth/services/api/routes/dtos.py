from uuid import UUID

from pydantic import BaseModel


class CreateUserDto(BaseModel):
    login: str
    firstname: str
    surname: str
    password: str


class LoginUserDto(BaseModel):
    login: str
    password: str


class LoginDto(BaseModel):
    login: str


class RoleChangeDto(BaseModel):
    login: str
    role_name: str
