from datetime import date

# Refactoring to more pythonic syntax

class DatePeriod:
    def __init__(self, start, end):
        assert start <= end, "Start date must be less than or equal to end date"
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

