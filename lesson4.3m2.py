class Car:
    cars_total = 0


    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.cars_total
    
    def drive(self, location):
        print(f"Driving in {location}")

    @classmethod
    def create(cls, color, model):
        new_car = cls(color,model)
        return new_car
    
    car_mazda = Car.create("red", "Mazda")
    print(car_mazda.color)
    print(Car.cars_total)