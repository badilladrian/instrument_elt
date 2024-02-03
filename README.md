# instrument_elt
Draft of a high I/O throughput ELT pipeline

This branch is now archived. Nevertheless, it displays OOP/Pythonistic code and async capacities.
:+1:  -  :shipit:

```
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
```

All the CALCULATIONS are tested from:
https://github.com/badilladrian/instrument_elt/blob/develop/instrument/calculations.py
@
https://github.com/badilladrian/instrument_elt/tree/develop/tests

![CleanShot 2024-02-03 at 01 04 58@2x](https://github.com/badilladrian/instrument_elt/assets/13179500/5be1a166-0e28-4949-90a7-4d7b1b43de14)
