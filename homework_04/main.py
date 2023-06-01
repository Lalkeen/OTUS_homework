"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from typing import Iterable
from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import fetch_data, USERS_DATA_URL, POSTS_DATA_URL
from models import User, Post, async_engine, Session, Base
import asyncio


async def fetch_users_data() -> list[User]:
    datas: list = await fetch_data(USERS_DATA_URL)
    users = []
    for data in datas:
        a = User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
        )
        users.append(a)

    return users


async def fetch_posts_data() -> list[Post]:
    datas: list = await fetch_data(POSTS_DATA_URL)
    posts = []
    for data in datas:
        a = Post(
            id=data["id"],
            user_id=data["userId"],
            title=data["title"],
            body=data["body"],
        )
        posts.append(a)

    return posts


async def create_db(table_name: str):
    async with async_engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all, tables=[Base.metadata.tables[table_name]]
        )


async def create_user_db(session: AsyncSession, data: Iterable[User]) -> Iterable[User]:
    await create_db("User")
    user = data
    session.add_all(user)
    await session.commit()

    return user


async def create_post_db(session: AsyncSession, data: Iterable[Post]) -> Iterable[Post]:
    await create_db("Post")
    post = data
    session.add_all(post)
    await session.commit()

    return post


async def async_main():
    async with Session() as session:
        users_data: Iterable[User]
        posts_data: Iterable[Post]
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )
        await create_user_db(session, users_data)
        await create_post_db(session, posts_data)
        


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
