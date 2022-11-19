import bcrypt

from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4
from pydantic import constr

from sqlmodel import Field, Relationship, SQLModel


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    name: constr(min_length=1, max_length=64) = Field(primary_key=True)


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    firstname: constr(min_length=1, max_length=64)
    surname: constr(min_length=1, max_length=64)
    verify: bool
    blocked: bool
    role: str = Field(foreign_key=f"{Role.__tablename__}.name")
    password: constr(min_length=60, max_length=60)
    avatar_link: str
    accounts: List["Account"] = Relationship(
        back_populates="users",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())

    def check_password(self, password: str) -> bool:
        if self.password is None:
            return False
        return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=self.password)


class Currency(SQLModel, table=True):
    __tablename__ = "currencies"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: constr(min_length=1, max_length=64)
    cost: int
    ticker: constr(min_length=1, max_length=8)


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    user: User = Relationship(
        back_populates="accounts",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    value: int
    currency_id: UUID = Field(foreign_key=f"{Currency.__tablename__}.id")


class Transaction(SQLModel, table=True):
    __tablename__ = "transactions"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    account: Account = Relationship(
        back_populates="transactions",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    amount: float
    rate: float
    currency: Currency = Relationship(
        back_populates="transactions",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    bought_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    description: constr(min_length=1, max_length=64)
