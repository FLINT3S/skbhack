import os

from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv


load_dotenv()

engine = create_engine(os.environ["CONNECTION_STRING"])
SQLModel.metadata.create_all(engine)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
