"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_data(
    url: str,
) -> list:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list = await response.json()
            if isinstance(data, list):
                return data
