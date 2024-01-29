from typing import Any
from io_clients.sql_client import SqlClient
from io_clients.csv_client import CsvClient


class InstrumentPipeline:
    def __init__(self, csv_client: CsvClient, sql_client: SqlClient):
        self.csv_client = csv_client
        self.sql_client = sql_client

    async def _compute_on_records(
        self, chunk: list[dict[str, Any]], output_file: str
    ) -> None:
        async with self.sql_client.pool.acquire() as conn:
            async with conn.transaction():
                for row in chunk:
                    multiplier = await self.get_multiplier_from_database(
                        row["INSTRUMENT_NAME"]
                    )

                    if multiplier is not None:
                        row["VALUE"] *= multiplier

                    await self.write_to_output_file(row, output_file)

    async def process_large_csv_async(
        self,
        chunk_size: int = 1000,
        pool_size: int = 5,
        output_file: str = "output.csv",
    ) -> None:
        await self.sql_client.connect(min_size=pool_size, max_size=pool_size)

        try:
            async for chunk in self.csv_client.read_large_csv(chunk_size=chunk_size):
                await self._compute_on_records(chunk, output_file)
        except Exception as e:
            print(f"Error processing CSV file: {e}")
        finally:
            await self.sql_client.close()

    async def get_multiplier_from_database(self, instrument_name):
        pass  # TODO decide where/whom has this responsability
        # result = await self.sql_client.execute_query(
        #     "SELECT MULTIPLIER FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = $1",
        #     instrument_name,
        # )
        # return result["multiplier"] if result else None

    # async def write_to_output_file(self, row: Dict[str, Any], output_file: str) -> None:
    #     async with asyncio.Lock():
    #         self.csv_client.write(row, output_file) # TODO decide where/when write out results
