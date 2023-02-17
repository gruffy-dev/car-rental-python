from datetime import date


class DatePeriod:
    def __init__(self, start, end):
        assert start <= end, "Start date must be less than or equal to end date"
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
