class Car:
    cars_total = 0


    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed
        Car.cars_total += 1
    
    @staticmethod
    def validate_speed(location):
        if speed < 0:
           raise ValueError(f"Speed cannot be")
        return True
                            

    @classmethod
    def create(cls, color, model):
        new_car = cls(color,model)
        return new_car
    
    car_mazda = Car.create("red", "Mazda")
    car_mazda = Car.create("red", "Mazda")
    print(car_mazda.color)
    print(Car.cars_total)