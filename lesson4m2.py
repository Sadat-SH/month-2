class Car:
    #инициализатор объектов 
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._max_speed = 0
        self.__fined = False

    def drive(self, location):
        print    