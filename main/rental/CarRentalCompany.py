from main.rental.Criteria import Criteria
from main.rental.Car import Car
from main.rental.Renter import Renter
from main.utils.DatePeriod import DatePeriod
import threading


class CarRentalCompany:
    def __init__(self):
        self.cars = []
        # At this point we do not need a reentrant lock so a normal lock should work
        self._rental_lock = threading.Lock()


    def add_car(self, car: Car):
        self.cars.append(car)

    def matching_cars(self, criteria: Criteria) -> list:
        # This is a read operation so the lock really isn't going to do much within this context
        with self._rental_lock:
            # This method of filtering is extremely crude and should really not be used
            if criteria.rental_group:
                return [car for car in self.cars if car.rental_group == criteria.rental_group]
            else:
                return self.cars

    def rent_car(self, renter: Renter, car: Car, date_period: DatePeriod):
        # This makes modifications to the inventory so this is where we need to have a lock to support multi threaded
        # access
        with self._rental_lock:
            pass


    def return_car(self, renter, car):
        pass
