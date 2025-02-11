import unittest
import datetime
from main.rental.Renter import Renter
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.CarRentalCompany import CarRentalCompany
from main.utils.DatePeriod import DatePeriod
from concurrent.futures import ThreadPoolExecutor, as_completed


def rent_car(self, renter: Renter, car):


    from main.utils.DatePeriod import DatePeriod


class CarRentalTest(unittest.TestCase):

    def setUp(self):
        """
        Instead of creating the inventory list within each test, we do it once in the setup
        """
        self.CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
        self.CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
        self.CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
        self.CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

        self.RENTER1 = Renter("Hydrogen", "Joe", "HYDRO010190JX8NM", datetime.date(1990, 1, 1))
        self.RENTER2 = Renter("Calcium", "Sam", "CALCI010203SX8NM", datetime.date(2003, 2, 1))
        self.RENTER3 = Renter("Neon", "Maisy", "NEONN010398MX8NM", datetime.date(1998, 3, 1))
        self.RENTER4 = Renter("Carbon", "Greta", "CARBO010497GX8NM", datetime.date(1997, 4, 1))

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
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        criteria = Criteria(date_period=DatePeriod(start=from_date, end=to_date))

        # The first set of asserts checks that the instance of the Critera class supports the from and to dates

        self.assertEqual(criteria.date_period.get_start(), from_date)
        self.assertEqual(criteria.date_period.get_end(), to_date)

    def test_story_2_car_renter_should_not_be_show_any_cars_that_are_booked_in_the_period_supplied(self):
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        criteria = Criteria(date_period=DatePeriod(start=from_date, end=to_date))

        # In order to test this method, we should first be able to book a car
        # At this point, no cars are booked so we can just pick the first one
        car_to_rent = self._car_rental_company.cars[0]
        date_period_1 = DatePeriod(start=from_date, end=to_date)

        # For the purpose of this test, we do not use the booking functionality.  Instead, we directly insert the
        # date_period object into the car to indicate that it has been booked

        car_to_rent.renter = self.RENTER1
        car_to_rent.date_period = date_period_1

        self.assertEqual(car_to_rent.renter, self.RENTER1)
        self.assertEqual(car_to_rent.date_period, date_period_1)

        cars_available = self._car_rental_company.matching_cars(criteria)
        self.assertEqual(len(cars_available), 3)

        # Now let's imagine that another car gets booked up within the rental window

        date_period_2 = DatePeriod(start=datetime.date(year=2025, month=2, day=2), end=datetime.date(year=2025, month=2, day=4))
        car_to_rent_2 = self._car_rental_company.cars[1]

        car_to_rent_2.renter = self.RENTER2
        car_to_rent_2.date_period = date_period_2

        cars_available = self._car_rental_company.matching_cars(criteria)
        self.assertEqual(len(cars_available), 2)

    def test_story_2_one_method_returning_a_list_of_matching_cars_with_changed_filter(self):
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        criteria = Criteria(rental_group='A1', date_period=DatePeriod(start=from_date, end=to_date))

        # We know from the test data that A1 cars are in element 2 and 3.  This removes element 2 from the equation
        # as it is now booked out
        car_to_rent = self._car_rental_company.cars[2]
        date_period_1 = DatePeriod(start=from_date, end=to_date)

        car_to_rent.renter = self.RENTER1
        car_to_rent.date_period = date_period_1

        self.assertEqual(car_to_rent.renter, self.RENTER1)
        self.assertEqual(car_to_rent.date_period, date_period_1)

        cars_available = self._car_rental_company.matching_cars(criteria)
        self.assertEqual(len(cars_available), 1)
        self.assertEqual(cars_available[0].registration_number, 'XX14 4UR')

    def test_story_3_the_car_rental_should_be_stored_in_an_object_model(self):
        # The acceptance test criteria here is very vague

        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        date_period = DatePeriod(start=from_date, end=to_date)
        car_to_rent = self._car_rental_company.cars[0]

        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=car_to_rent, date_period=date_period)

        self.assertTrue(success)

        # Let us assume that if we can interrogate all the properties in the rental, then it is an object
        self.CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)

        self.assertEqual(self._car_rental_company.cars[0].make, 'VW')
        self.assertEqual(self._car_rental_company.cars[0].model, 'Golf')
        self.assertEqual(self._car_rental_company.cars[0].registration_number, 'XX11 1UR')
        self.assertEqual(self._car_rental_company.cars[0].rental_group, 'B2')
        self.assertEqual(self._car_rental_company.cars[0].cost_per_day, 90)
        self.assertEqual(self._car_rental_company.cars[0].renter, self.RENTER1)
        self.assertEqual(self._car_rental_company.cars[0].date_period, date_period)

    def test_story_3_there_should_not_be_able_to_have_overlapping_car_rentals_for_the_same_car(self):
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        date_period = DatePeriod(start=from_date, end=to_date)
        car_to_rent = self._car_rental_company.cars[0]

        # The first booking is successful
        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=car_to_rent, date_period=date_period)
        self.assertTrue(success)

        # The second booking fails as it is an overlap
        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=car_to_rent, date_period=date_period)
        self.assertFalse(success)

    def test_story_3_two_renters_should_not_be_able_to_book_the_same_car_at_the_same_time_for_an_overlapping_period(self):
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        date_period = DatePeriod(start=from_date, end=to_date)
        car_to_rent = self._car_rental_company.cars[0]

        futures = []
        results = []

        # This is a very rudimentary test to indicate that if you make 5 simultaneous bookings, only one will succeed
        # TODO: Consider diversifying the inputs such that we can check that the rental isn't overwritten by
        # TODO: any subsequent/simultaneous updates

        with ThreadPoolExecutor(max_workers=5) as executor:
            for _ in range(5):
                futures.append(executor.submit(self._car_rental_company.rent_car, renter=self.RENTER1, car=car_to_rent, date_period=date_period))

            for future in as_completed(futures):
                result = future.result()
                results.append(result)


        self.assertEqual(car_to_rent.renter, self.RENTER1)
        self.assertEqual(car_to_rent.date_period, date_period)

        # One successful booking
        self.assertEqual(len([x for x in results if x]), 1)

        # Four failed booking
        self.assertEqual(len([x for x in results if not x]), 4)

    def test_story_3_one_method_allowing_the_car_renter_to_book_a_car_for_a_period(self):
        from_date = datetime.date(year=2025, month=2, day=1)
        to_date = datetime.date(year=2025, month=2, day=10)
        date_period = DatePeriod(start=from_date, end=to_date)
        car_to_rent = self._car_rental_company.cars[0]

        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=car_to_rent, date_period=date_period)

        self.assertTrue(success)

    def test_additional_non_overlapping_dates_rent_car(self):
        # This test is actually the bad test.  What happens is if you have a date that does not overlap, you can
        # overwrite the booking data completely.

        date_period_1 = DatePeriod(start=datetime.date(year=2025, month=2, day=1), end=datetime.date(year=2025, month=2, day=5))
        date_period_2 = DatePeriod(start=datetime.date(year=2025, month=2, day=10), end=datetime.date(year=2025, month=2, day=15))

        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=self._car_rental_company.cars[0], date_period=date_period_2)

        self.assertTrue(success)
        self.assertEqual(self._car_rental_company.cars[0].renter, self.RENTER1)
        self.assertEqual(self._car_rental_company.cars[0].date_period, date_period_2)

        success = self._car_rental_company.rent_car(renter=self.RENTER2, car=self._car_rental_company.cars[0], date_period=date_period_1)

        self.assertTrue(success)
        self.assertEqual(self._car_rental_company.cars[0].renter, self.RENTER2)
        self.assertEqual(self._car_rental_company.cars[0].date_period, date_period_1)

    def test_additional_non_overlapping_dates_get_match(self):

        date_period_1 = DatePeriod(start=datetime.date(year=2025, month=2, day=1), end=datetime.date(year=2025, month=2, day=5))
        date_period_2 = DatePeriod(start=datetime.date(year=2025, month=2, day=10), end=datetime.date(year=2025, month=2, day=15))

        success = self._car_rental_company.rent_car(renter=self.RENTER1, car=self._car_rental_company.cars[0], date_period=date_period_2)

        self.assertTrue(success)
        self.assertEqual(self._car_rental_company.cars[0].renter, self.RENTER1)
        self.assertEqual(self._car_rental_company.cars[0].date_period, date_period_2)

        # We know that there is only a single car in the B2 group and this what we booked above
        criteria = Criteria(rental_group='B2', date_period=date_period_2)

        available_cars = self._car_rental_company.matching_cars(criteria=criteria)

        # If you use an overlapping booking date we get zero matches
        self.assertEqual(len(available_cars), 0)

        # However if there is no overlap the car is returned as available

        criteria = Criteria(rental_group='B2', date_period=date_period_1)
        available_cars = self._car_rental_company.matching_cars(criteria=criteria)
        self.assertEqual(len(available_cars), 1)







