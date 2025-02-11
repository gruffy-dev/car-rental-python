from datetime import date

# This class is not very pythonic but as there are unit tests written against it, we will not refactor

class DatePeriod:
    def __init__(self, start, end):
        assert start <= end, "Start date must be less than or equal to end date"
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
