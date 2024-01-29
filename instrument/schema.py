import datetime
from dataclasses import dataclass

# TODO: add validations inside of the dataclass / pydantic model could be used as well


@dataclass
class InstrumentData:
    name: str
    date: datetime.datetime
    value: float


@dataclass
class InstrumentMultiplier:
    id: str
    name: str
    multiplier: float
