import unittest
from datetime import date
from main.rental.Renter import Renter
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.CarRentalCompany import CarRentalCompany
from main.utils.DatePeriod import DatePeriod


def rent_car(self, renter: Renter, car):


    from main.utils.DatePeriod import DatePeriod


class CarRentalTest(unittest.TestCase):

    CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
    CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
    CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
    CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

    RENTER1 = Renter("Hydrogen", "Joe", "HYDRO010190JX8NM", date(1990, 1, 1))
    RENTER2 = Renter("Calcium", "Sam", "CALCI010203SX8NM", date(2003, 2, 1))
    RENTER3 = Renter("Neon", "Maisy", "NEONN010398MX8NM", date(1998, 3, 1))
    RENTER4 = Renter("Carbon", "Greta", "CARBO010497GX8NM", date(1997, 4, 1))

    def setUp(self):
        """
        Instead of creating the inventory list within each test, we do it once in the setup
        """
        self._car_rental_company = CarRentalCompany()
        self._car_rental_company.add_car(self.CAR1)
        self._car_rental_company.add_car(self.CAR2)
        self._car_rental_company.add_car(self.CAR3)
        self._car_rental_company.add_car(self.CAR4)

    def test_list_cars_available_to_rent_gives_more_than_one_car(self):
        criteria = Criteria()
        cars_available = self._car_rental_company.matching_cars(criteria)

        self.assertGreater(len(cars_available), 1)

    def test_story_1_one_method_returning_a_list_of_matching_cars(self):
        # Here we assume that we extend the Criteria object to start with a simple match in rental_group
        criteria = Criteria(rental_group='A1')
        cars_available = self._car_rental_company.matching_cars(criteria)
        # Using the "A1" rental group, we can see that this matches 2 cars
        self.assertEqual(len(cars_available), 2)

    def test_story_2_matching_criteria_for_a_renter_to_rent_a_car_should_include_from_and_to_date(self):
        from_date = date(year=2025, month=2, day=1)
        to_date = date(year=2025, month=2, day=10)
        criteria = Criteria(from_date=from_date, to_date=to_date)

        # The first set of asserts checks that the instance of the Critera class supports the from and to dates
        self.assertEqual(criteria.from_date, from_date)
        self.assertEqual(criteria.to_date, to_date)

    def test_story_2_car_renter_should_not_be_show_any_cars_that_are_booked_in_the_period_supplied(self):
        # In order to test this method, we should first be able to book a car
        # At this point, no cars are booked so we can just pick the first one
        car_to_rent = self._car_rental_company.cars[0]
        date_period = DatePeriod()
        self._car_rental_company.rent_car(renter=self.RENTER1, car=car_to_rent)

    def test_story_2_one_method_returning_a_list_matching_cars_with_changed_filter(self):
        pass
