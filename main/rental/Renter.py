from datetime import date


class Renter:
    def __init__(self, last_name, first_name, driving_license_number, date_of_birth):
        """
        A Renter class that captures details of the car renter
        :param last_name: (str)  Last name of the renter
        :param first_name:  (str) First name of the renter
        :param driving_license_number: (str) The renter's driver's licence number
        :param date_of_birth: (datetime.date) The renter's date of birth
        """
        self.last_name = last_name
        self.first_name = first_name
        self.driving_license_number = driving_license_number
        self.date_of_birth = date_of_birth
