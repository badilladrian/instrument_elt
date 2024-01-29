import asyncio
import logging
from io_clients.sql_client import SqlClient
from io_clients.csv_client import CsvClient
from instrument_pipeline import InstrumentPipeline
from settings import *

logger = logging.getLogger(__name__)
logger = logging.basicConfig(level=LOGGER_LEVEL)


async def main():
    sql_client = SqlClient(**DATABASE_CONFIG)
    csv_client = CsvClient(INPUT_CSV_FILE_PATH)

    instrument_pipeline = InstrumentPipeline(csv_client, sql_client)

    try:
        await instrument_pipeline.process_large_csv_async(
            chunk_size=CHUNK_SIZE,
            pool_size=POOL_SIZE,
            output_file=OUTPUT_CSV_RESULT_FILE,
        )
    except Exception as error:
        logger.exception("An error has occured %s !", error)


if __name__ == "__main__":
    asyncio.run(main())
