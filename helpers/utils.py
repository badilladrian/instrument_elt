from datetime import datetime
from settings import DATE_FORMAT


def is_valid_date(date_str: str) -> bool:
    try:
        return bool(datetime.strptime(date_str, DATE_FORMAT))
    except ValueError:
        return False


def is_business_date(date_str: str) -> bool:
    date_obj = datetime.strptime(date_str, DATE_FORMAT)
    return date_obj.weekday() < 5  # Monday to Friday


def mean_value(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
