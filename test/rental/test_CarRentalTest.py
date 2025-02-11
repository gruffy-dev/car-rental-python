import unittest
from datetime import date
from main.rental.Renter import Renter
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.CarRentalCompany import CarRentalCompany


class CarRentalTest(unittest.TestCase):

    CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
    CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
    CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
    CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

    RENTER1 = Renter("Hydrogen", "Joe", "HYDRO010190JX8NM", date(1990, 1, 1))
    RENTER2 = Renter("Calcium", "Sam", "CALCI010203SX8NM", date(2003, 2, 1))
    RENTER3 = Renter("Neon", "Maisy", "NEONN010398MX8NM", date(1998, 3, 1))
    RENTER4 = Renter("Carbon", "Greta", "CARBO010497GX8NM", date(1997, 4, 1))

    def test_list_cars_available_to_rent_gives_more_than_one_car(self):
        car_rental_company = CarRentalCompany()
        car_rental_company.add_car(self.CAR1)
        car_rental_company.add_car(self.CAR2)
        car_rental_company.add_car(self.CAR3)
        car_rental_company.add_car(self.CAR4)

        criteria = Criteria()
        cars_available = car_rental_company.matching_cars(criteria)

        self.assertGreater(len(cars_available), 1)
