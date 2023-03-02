"""
Module for the createion of TradeDate class
"""

from dataclasses import dataclass
from typing import List


@dataclass
class TradeDate:
    """
    Dataclass containing a TradeDate used by an Engine
    """

    year: int
    month: int
    day: int

    def __post_init__(self):
        if self.day < 0 or self.day > 31:
            raise ValueError("Day value is incorrect!")

        if self.month < 0 or self.month > 12:
            raise ValueError("Month value is incorrect!")

        if self.year < 0:
            raise ValueError("Year value is incorrect!")


class TradeIndex:
    AVAILABLE_DATE_FORMATS = frozenset(["YYYY-MM-DD"])

    def __init__(self):
        self.dates = None

    def _set_dates(self, dates: List[str], format: str = "YYYY-MM-DD"):
        if format not in self.AVAILABLE_DATE_FORMATS:
            raise KeyError(
                "Such date format is not supported!\n"
                + f"Avaialble date formats are {self.AVAILABLE_DATE_FORMATS}"
            )

        self.dates = tuple(
            [TradeDate(**self._process_date(date, format)) for date in dates]
        )

    def _process_date(self, date, format):
        check_idx = 0
        while check_idx < len(format):
            if format[check_idx] == "Y":
                try:
                    year = int(date[check_idx : check_idx + 4])
                    check_idx += 4
                except ValueError:
                    print(
                        f"Year of date {date} is specified incorrectly "
                        + f"from the given format {format}!"
                    )
            elif format[check_idx] == "M":
                try:
                    month = int(date[check_idx : check_idx + 2])
                    check_idx += 2
                except ValueError:
                    print(
                        f"Month of date {date} is specified incorrectly "
                        + f"from the given format {format}!"
                    )
            elif format[check_idx] == "D":
                try:
                    day = int(date[check_idx : check_idx + 2])
                    check_idx += 2
                except ValueError:
                    print(
                        f"Day of date {date} is specified incorrectly "
                        + f"from the given format {format}!"
                    )
            else:
                raise ValueError("Internal error regarding date format!")

            # Check date separator
            if check_idx < len(format):
                self._check_date_separator(
                    date=date, date_sep=date[check_idx], format_sep=format[check_idx]
                )
                check_idx += 1
        return {"year": year, "month": month, "day": day}

    def _check_date_separator(self, date: str, date_sep: str, format_sep: str):
        if date_sep != format_sep:
            raise ValueError(
                f"Separator of date {date} is specified incorrectly"
                + "from the given format!"
            )
