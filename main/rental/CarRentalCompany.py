class CarRentalCompany:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def matching_cars(self, criteria):
        return self.cars

    def rent_car(self, renter, car):
        pass

    def return_car(self, renter, car):
        pass
