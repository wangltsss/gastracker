# This file contains the data types used in the project

from log_config import get_logger

logger = get_logger(__name__)


class Fuel:
    Regular: str = "A"
    Midgrade: str = "B"
    Premium: str = "C"
    Diesel: str = "D"


class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year: int = year
        self.month: int = month
        self.day: int = day
        logger.debug(f"Date object created: {self.to_str()}")

    def to_str(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
    
    @staticmethod
    def from_str(date_str: str) -> 'Date':
        logger.debug(f"Creating Date object from string: {date_str}")
        try:
            year, month, day = map(int, date_str.split("-"))
        except ValueError as e:
            logger.error(f"Invalid date string: {date_str}")
            raise e
        return Date(year, month, day)

    def __str__(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
