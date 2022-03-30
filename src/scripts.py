import os
import typer
from datetime import date
from random import choice
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions
from logging_settings import logging
from models import Hero, Moto, Story, Battle

load_dotenv()

DB_URI_FOR_DEVELOPMENT = os.getenv("CURRENT_DATABASE_URL")
DB_URI = os.getenv("DATABASE_URL", DB_URI_FOR_DEVELOPMENT)

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()
app = typer.Typer()

@app.command()
def add_hero(name: str,
             side: str,
             birthday: str = None,
             power: int = 0):

    new_hero = Hero(name=name, birthday=birthday, side=side, power=power)
    session.add(new_hero)
    session.commit()
    logging.info(f"Hero created. {new_hero}")


@app.command()
def add_moto(hero_id: int, moto: str):
    hero = session.query(Hero).get(hero_id)

    if hero:
        moto_id = len(hero.motos) + 1
        hero.motos.append(Moto(moto_id=moto_id, moto=moto))
        session.commit()
        logging.info(f"Moto for {hero_id=} added")


@app.command()
def add_battle():
    hero_1 = session.query(Hero).order_by(functions.random()).first()
    hero_2 = session.query(Hero).filter(Hero.side != hero_1.side).order_by(functions.random()).first()
    hero_1_moto = hero_1.get_moto()
    hero_2_moto = hero_2.get_moto()
    winner = choice([0, 1, 2])
    battle = Battle(
        hero_id_1=hero_1.id,
        hero_id_2=hero_2.id,
        moto_id_1=hero_1_moto.id,
        moto_id_2=hero_2_moto.id,
        winner=winner
        )

    session.add(battle)
    session.commit()
    logging.info(f"Battle: 1-{hero_1.name} VS 2-{hero_2.name} finished. Result-{winner}")


@app.command()
def add_story(hero_id: int, story: str):
    hero = session.query(Hero).get(hero_id)

    if hero:
        hero.story = Story(story=story)
        logging.info(f"Story for {hero_id=} added")
        session.commit()


@app.command()
def delete_hero(hero_id: int):

    hero = session.query(Hero).get(hero_id)

    if hero:
        session.delete(hero)
        session.commit()
        logging.info(f"Hero {hero_id=} deleted")


if __name__ == "__main__":
    app()