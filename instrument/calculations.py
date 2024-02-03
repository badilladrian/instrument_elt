from datetime import datetime
from typing import Optional
from helpers.utils import mean_value
from instrument.schema import InstrumentData, InstrumentMultiplier

# TODO: add logging


def apply_multiplier(
    data: InstrumentData, db_multiplier: InstrumentMultiplier
) -> InstrumentData:
    multiplier = db_multiplier.multiplier
    if multiplier is not None:
        data.value *= multiplier
    return data


def apply_name_filter(
    data: list[InstrumentData], name: Optional[str]
) -> list[InstrumentData]:
    if name is not None:  # filter by instrument name
        data = [entry for entry in data if entry.name == name]
    return data


def apply_date_range_filter(
    data: list[InstrumentData], start_dt: Optional[datetime], end_dt: Optional[datetime]
) -> list[InstrumentData]:
    if start_dt is None and end_dt is None:
        return data  # as it is

    if start_dt is not None and end_dt is not None:  # data range
        return [entry for entry in data if start_dt <= entry.date <= end_dt]

    if start_dt is not None:  # min date
        return [entry for entry in data if entry.date >= start_dt]

    if end_dt is not None:  # max date
        return [entry for entry in data if entry.date <= end_dt]


def filter_data(
    data: list[InstrumentData],
    name: Optional[str] = None,
    start_dt: Optional[datetime] = None,
    end_dt: Optional[datetime] = None,
) -> list[InstrumentData]:
    """
    Filter data by name and date range.

    Returns:
        list[InstrumentData]: The filtered list of instrument data
                             or the original list if no filter args are provided.
    """
    filtered_by_name = apply_name_filter(data, name)
    filtered_by_date_range = apply_date_range_filter(filtered_by_name, start_dt, end_dt)
    return filtered_by_date_range


def calculate_mean(
    instrument_data: list[InstrumentData],
    instrument_name: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> float:
    filtered_data = filter_data(instrument_data, instrument_name, start_date, end_date)
    values = [data.value for data in filtered_data]
    return mean_value(values)
