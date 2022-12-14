import bcrypt

from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4
from pydantic import constr

from sqlmodel import Field, Relationship, SQLModel


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    name: constr(min_length=1, max_length=64) = Field(primary_key=True)

    @staticmethod
    def get_instance(name: str):
        role = Role()
        role.name = name
        return role


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    login: constr(min_length=1, max_length=64)
    firstname: constr(min_length=1, max_length=64)
    surname: constr(min_length=1, max_length=64)
    verify: bool
    blocked: bool
    role: str = Field(foreign_key=f"{Role.__tablename__}.name")
    password: constr(min_length=60, max_length=60)
    accounts: List["Account"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    @staticmethod
    def get_instance(login: str, firstname: str, surname: str, password: str):
        user = User()
        user.login = login
        user.firstname = firstname
        user.surname = surname
        user.verify = False
        user.blocked = False
        user.role = "User"
        user.set_password(password)
        return user

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password: str) -> bool:
        if self.password is None:
            return False
        return bcrypt.checkpw(password=password.encode("utf-8"),
                              hashed_password=self.password.encode("utf-8"))


class Currency(SQLModel, table=True):
    __tablename__ = "currencies"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: constr(min_length=1, max_length=64)
    ticker: constr(min_length=1, max_length=8)
    symbol: constr(min_length=1, max_length=1)

    @staticmethod
    def get_instance(id: UUID, name: str, ticker: str, symbol: str):
        currency = Currency()
        currency.id = id
        currency.name = name
        currency.ticker = ticker
        currency.symbol = symbol
        return currency


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    user: User = Relationship(
        back_populates="accounts",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    user_id: UUID = Field(default=None, foreign_key="users.id")
    amount: float
    currency: Currency = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    currency_id: UUID = Field(default=None, foreign_key="currencies.id")
    transactions: List["Transaction"] = Relationship(
        back_populates="account",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    @staticmethod
    def get_instance(user: User, currency: Currency):
        account = Account()
        account.amount = 0
        account.user = user
        account.currency = currency
        return account


class Transaction(SQLModel, table=True):
    __tablename__ = "transactions"

    id: UUID = Field(primary_key=True, default_factory=uuid4)
    account: Account = Relationship(
        back_populates="transactions",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    account_id: UUID = Field(default=None, foreign_key="accounts.id")
    amount: float
    rate: float
    currency: Currency = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    currency_id: UUID = Field(default=None, foreign_key="currencies.id")
    bought_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    description: constr(min_length=1, max_length=64)

    @staticmethod
    def get_instance(account: Account, amount: float):
        transaction = Transaction()
        transaction.account = account
        transaction.amount = amount
        transaction.bought_at = datetime.now()
        transaction.currency = account.currency
        return transaction
