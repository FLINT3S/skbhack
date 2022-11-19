import os

from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ["CONNECTION_STRING"])
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
