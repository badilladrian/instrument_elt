import datetime
from conftest import INSTRUMENT_NAME_A, INSTRUMENT_NAME_B
from instrument.calculations import mean_value, filter_data


def test_mean_value_empty():
    result = mean_value([])
    assert result == 0.0


def test_mean_values():
    result = mean_value([1, 2, 3, 4, 5])
    assert result == 3.0


def test_filter_instruments_data_only(create_instruments_data):
    filtered_data = filter_data(create_instruments_data)

    assert len(filtered_data) == 6  # The fixture data has six instruments
    assert (
        mean_value([data.value for data in filtered_data]) == 22.5
    )  # Check mean value against all instruments


def test_filter_data_by_name(create_instruments_data):
    filtered_data = filter_data(create_instruments_data, name=INSTRUMENT_NAME_B)
    assert (
        len(filtered_data) == 2
    )  # There are two entries with INSTRUMENT_NAME_B (Instrument2)
    assert mean_value([d.value for d in filtered_data]) == 22.5


def test_filter_data_by_date_range(create_instruments_data):
    start_date = datetime.datetime(year=2012, month=9, day=28)
    end_date = datetime.datetime(year=2013, month=9, day=29)
    filtered_data = filter_data(
        create_instruments_data, start_dt=start_date, end_dt=end_date
    )

    assert (
        len(filtered_data) == 2
    )  # There are two entries within the specified date range


def test_filter_data_by_name_and_date_range(create_instruments_data):
    start_date = datetime.datetime(year=2011, month=9, day=20)
    end_date = datetime.datetime(year=2013, month=9, day=30)
    filtered_data = filter_data(
        create_instruments_data,
        name=INSTRUMENT_NAME_A,
        start_dt=start_date,
        end_dt=end_date,
    )

    assert (
        len(filtered_data) == 2
    )  # There are two entries with INSTRUMENT_NAME_A within the specified date range
