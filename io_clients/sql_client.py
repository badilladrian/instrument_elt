import asyncpg
import contextlib
from settings import DATABASE_CONFIG

# TODO: add logging


class SqlClient:
    def __init__(self, db_config: dict = DATABASE_CONFIG):
        self.db_config = db_config
        self.pool = None

    @contextlib.asynccontextmanager
    async def connect(self, min_size=5, max_size=10):
        self.pool = await asyncpg.create_pool(
            user=self.db_config.get("user"),
            password=self.db_config.get("password"),
            database=self.db_config.get("database"),
            host=self.db_config.get("host", "localhost"),
            port=self.db_config.get("port", 5432),
            min_size=min_size,
            max_size=max_size,
        )
        try:
            yield self.pool
        finally:
            await self.pool.close()

    async def execute_query(self, query: str, *args):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.execute(query, *args)
