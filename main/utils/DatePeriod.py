import datetime

# Refactoring to more pythonic syntax

class DatePeriod:
    def __init__(self, start: datetime.date, end: datetime.date):
        assert start <= end, "Start date must be less than or equal to end date"
        self._start = start
        self._end = end

    @property
    def start(self) -> datetime.date:
        return self._start

    @property
    def end(self) -> datetime.date:
        return self._end

