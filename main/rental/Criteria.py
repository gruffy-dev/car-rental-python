import datetime
from main.utils.DatePeriod import DatePeriod

class Criteria:
    def __init__(self, rental_group: str = None, date_period: DatePeriod = None):
        """
        A Criteria class that allows is to pass the filter criteria required to obtain a short list of cars
        :param rental_group: (str) A car rental group
        :param date_period: (DatePeriod)  An instance od the DatePeriod object that contains the start and end time of the rental
        """

        self._rental_group = rental_group
        self._date_period = date_period

    # There may not be a need to modify the values once the instance is created by the constructor so for the moment
    # we do not add any setter methods

    @property
    def rental_group(self) -> str:
        return self._rental_group

    @property
    def date_period(self) -> DatePeriod:
        return self._date_period



