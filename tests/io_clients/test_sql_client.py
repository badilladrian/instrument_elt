from sqlalchemy import sql
import pytest
from pytest_mock_resources import create_postgres_fixture

mock_postgres_async = create_postgres_fixture(async_=True)


@pytest.mark.asyncio
async def test_sql_client_with_mocked_postgres(mock_postgres_async):
    async with mock_postgres_async.connect() as conn:
        # Create table
        await conn.execute(
            sql.text(
                """
CREATE TABLE IF NOT EXISTS INSTRUMENT_PRICE_MODIFIER (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL,
    MULTIPLIER FLOAT NOT NULL
)
"""
            )
        )

        # Insert data
        await conn.execute(
            sql.text(
                """
INSERT INTO INSTRUMENT_PRICE_MODIFIER (NAME, MULTIPLIER) VALUES ('Instrument1', 1.2)
"""
            )
        )

        # Query inserted data
        result = await conn.execute(
            sql.text(
                """
SELECT * FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = 'Instrument1'
"""
            )
        )

        # Fetch the first row from the result
        result = result.fetchone()

        # Assert data is correct
        assert result._data is not None
        assert result._data[0] == 1  # INSTRUMENT_PRICE_MODIFIER.ID
        assert result._data[1] == "Instrument1"  # INSTRUMENT_PRICE_MODIFIER.NAME
        assert result._data[2] == 1.2  # INSTRUMENT_PRICE_MODIFIER.MULTIPLIER
