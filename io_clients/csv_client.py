import csv
from typing import Any
import aiofiles
from collections import deque

from helpers.utils import is_valid_date
from settings import MAX_DATE

HEADERS = ("INSTRUMENT_NAME", "DATE", "VALUE")


class CsvClient:
    def __init__(
        self, file_path: str, delimiter=",", chunk_size=1000, max_date=MAX_DATE
    ):
        self.file_path = file_path
        self.delimiter = delimiter
        self.chunk_size = chunk_size
        self.max_date = max_date

    @staticmethod
    async def read_large_csv(self):
        async with aiofiles.open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=self.delimiter, fieldnames=HEADERS)
            current_chunk = deque(maxlen=self.chunk_size)

            for row_index, row in enumerate(reader):
                try:
                    # Step 1: Validate the date and skip invalid rows
                    if not is_valid_date(row.get("DATE")):
                        continue

                    # Step 2: Append the row to the current chunk
                    current_chunk.append(dict(row))

                    # Step 3: Yield the chunk when it reaches the specified size
                    if row_index > 0 and row_index % self.chunk_size == 0:
                        yield list(current_chunk)
                except Exception as e:
                    # Step 4: Handle errors during row processing
                    print(f"Error processing row {row_index + 1}: {e}")

            # Step 5: Yield the remaining rows in the last chunk
            if current_chunk:
                yield list(current_chunk)

    @staticmethod
    async def write(row: Any, file_path: str):
        async with aiofiles.open(file_path, "a", encoding="utf-8") as file:
            await file.write(f"{row}\n")
