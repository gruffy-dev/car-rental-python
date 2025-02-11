import datetime

class Criteria:
    def __init__(self, rental_group: str = None, from_date: datetime.date = None, to_date: datetime.date = None):
        """
        A Criteria class that allows is to pass the filter criteria required to obtain a short list of cars
        :param rental_group: (str) A car rental group
        :param from_date: (datetime.date) The date the rental starts
        :param to_date:  (datetime.date) The date the rental ends
        """

        self._rental_group = rental_group
        self._from_date = from_date
        self._to_date = to_date


    # There may not be a need to modify the values once the instance is created by the constructor so for the moment
    # we do not add any setter methods

    @property
    def rental_group(self) -> str:
        return self._rental_group

    @property
    def from_date(self) -> datetime.date:
        return self._from_date

    @property
    def to_date(self) -> datetime.date:
        return self._to_date


