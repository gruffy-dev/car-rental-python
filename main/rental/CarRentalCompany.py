from main.rental.Criteria import Criteria
from main.rental.Car import Car
from main.rental.Renter import Renter
from main.utils.DatePeriod import DatePeriod
from main.utils.DatePeriodUtil import DatePeriodUtil
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
            short_listed_cars = self.cars

            if criteria.rental_group:
                short_listed_cars  = [car for car in short_listed_cars if car.rental_group == criteria.rental_group]

            if criteria.date_period:
                results = []
                for car in short_listed_cars:
                    # TODO: This is not great for cyclomatic complexity. Refactor.
                    if car.date_period:
                        if not DatePeriodUtil.are_overlapping(criteria.date_period, car.date_period):
                            results.append(car)
                    else:
                        # This means that the car does not have a rental period so it is open for rent
                        results.append(car)
                    short_listed_cars = results

            return short_listed_cars


    def rent_car(self, renter: Renter, car: Car, date_period: DatePeriod) -> bool:
        # This makes modifications to the inventory so this is where we need to have a lock to support multi threaded
        # access
        with self._rental_lock:
            if car.date_period:
                # There is rental data here.
                # TODO: This method is fairly limited as you cannot book a car more than once.  If the car is
                # TODO: booked in the future, it is considered a non overlap and can be overwritten!

                if not DatePeriodUtil.are_overlapping(date_period, car.date_period):
                    car.date_period = date_period
                    car.renter = renter
                    return True
                else:
                    return False
            else:
                # We can just book it here
                car.date_period = date_period
                car.renter = renter
                return True


    def return_car(self, renter, car):
        pass
