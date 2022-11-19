import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

from .models import *

load_dotenv()

engine = create_engine(os.environ["CONNECTION_STRING"])
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.merge(Role.get_instance("User"))
    session.merge(Role.get_instance("Admin"))

    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000000"), "Рубль", "RUB", "₽"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000001"), "Доллар", "USD", "$"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000002"), "Евро", "EUR", "€"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000003"), "Юань", "CNY", "¥"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000004"), "Фунт стерлингов", "GBP", "£"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000005"), "Новый шекель", "ILS", "₪"))
    session.merge(Currency.get_instance(UUID("00000000-0000-0000-0000-000000000006"), "Тенге", "KZT", "₸"))
    session.commit()


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
