import datetime
import pytest
from instrument.schema import InstrumentData

# This allows to change the input data for the tests
INSTRUMENT_NAME_A = "INSTRUMENT1"
INSTRUMENT_NAME_B = "INSTRUMENT2"
INSTRUMENT_NAME_C = "INSTRUMENT3"

SQL_DB_TABLE_NAME = "INSTRUMENT_PRICE_MODIFIER"

# 28-09-2012
FREEZE_DATE_1 = datetime.datetime(
    year=2012, month=9, day=28, hour=17, minute=5, second=55, microsecond=3030
)

# 29-09-2013
FREEZE_DATE_2 = datetime.datetime(
    year=2013, month=9, day=29, hour=17, minute=5, second=55, microsecond=3030
)

# 30-09-2014
FREEZE_DATE_3 = datetime.datetime(
    year=2014, month=9, day=30, hour=17, minute=5, second=55, microsecond=3030
)


@pytest.fixture
def create_instruments_data():
    return [
        InstrumentData(name=INSTRUMENT_NAME_A, date=FREEZE_DATE_1, value=10.0),
        InstrumentData(name=INSTRUMENT_NAME_A, date=FREEZE_DATE_2, value=20.0),
        InstrumentData(name=INSTRUMENT_NAME_B, date=FREEZE_DATE_3, value=30.0),
        InstrumentData(name=INSTRUMENT_NAME_B, date=FREEZE_DATE_1, value=15.0),
        InstrumentData(name=INSTRUMENT_NAME_C, date=FREEZE_DATE_2, value=25.0),
        InstrumentData(name=INSTRUMENT_NAME_C, date=FREEZE_DATE_3, value=35.0),
    ]
