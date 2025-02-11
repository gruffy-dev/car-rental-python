class Car:
    def __init__(self, make: str, model: str, registration_number: str, rental_group: str, cost_per_day: int):
        """
        A Car class representing a car in the rental inventory
        :param make: (str) The make of the car
        :param model: (str) The model of the car
        :param registration_number: (str) The registration number of the car
        :param rental_group: (str) The rental group of the car
        :param cost_per_day: (str) The cost per day of the car
        """
        self._make = make
        self._model = model
        self._registration_number = registration_number
        self._rental_group = rental_group
        self._cost_per_day = cost_per_day

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @property
    def rental_group(self) -> str:
        return self._rental_group

    @property
    def cost_per_day(self) -> int:
        return self._cost_per_day


