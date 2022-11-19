from sqlmodel import Session, SQLModel, create_engine

from .models import Hero

hero_1 = Hero(name="Deadblonde", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("postgresql://skb:skb123456789@db:5432/skb")
SQLModel.metadata.create_all(engine)

def test():
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()
        print("Heroes added to the database.")
