def is_six_digit(number: int) -> bool:
    if len(str(number)) == 6:
        return True
    else:
        raise ValueError("The number is not six digit")

class Car:
    amount_of_cars = 0
    def __init__(self, brand, model, year, max_speed, plate: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.velocity = 0
        self.color = "Not Defined"
        self.plate = plate
        is_six_digit(self.plate)
        Car.amount_of_cars += 1
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"Color changed to {self.color}")

    def run(self):
        self.velocity = self.max_speed * 0.75
        print(f"Running with {self.velocity} km/h")
    
    def stop(self):
        self.velocity = 0
        print("Stopped")
    
    @classmethod
    def amount(cls):
        return f"This is car class. Currently there is {Car.amount_of_cars} cars defined"
    
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Max Speed: {self.max_speed}, Color: {self.color}, Plate: {self.plate}"
   
   

print(Car.amount())

car1 = Car("Toyota", "idk", 2021, 200, 123456)

print([dir for dir in dir(car1) if not dir.startswith("__")])


car2 = Car("Honda", "idk2", 2021, 200, 123457)

car2.run()
car2.stop()
car2.change_color("Green")



car3 = Car("BMW", "idkanymodel3", 2021, 200, 123458)

print(car3)
print(Car.amount())

class CarDealer:
    def __init__(self, name, brand = None) -> None:
        self.name = name
        self.brand = brand
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def show_cars(self):
        for car in self.cars:
            print(car)
    
    def sell_car(self, car):
        self.cars.remove(car)
        print(f"{car} sold")
    
    def __str__(self):
        cars = ""
        for car in self.cars:
            cars += car.__str__() + "\n"
        return f"Car Dealer {self.name} sells {self.brand} cars. Currently has {len(self.cars)} cars in stock. \nCars: \n{cars}"
    
car_dealer = CarDealer("John", "Mercedes")
car_dealer.add_car(car1)
car_dealer.add_car(car2)
car_dealer.add_car(car3)
print("Showing Cars")
car_dealer.show_cars()
print("Selling car")
car_dealer.sell_car(car1)
print("Showing Cars")
car_dealer.show_cars()
print("Dealer Info")
print(car_dealer)
