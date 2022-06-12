from app.tools.wrapers import async_comand
from app.tools.db import get_db_engine, Base
from app.config import Config

import click


@click.group()
def db():
    pass


@click.command()
@async_comand
async def init():
    engine = get_db_engine(Config.DB_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@click.command()
@async_comand
async def drop_all():
    engine = get_db_engine(Config.DB_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


db.add_command(init)
db.add_command(drop_all)
