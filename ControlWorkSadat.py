class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
          self.__age = age
        else:
            print( "Возраст не может быть отрицательным!" )

    def make_sound(self):
        print("Животное издает звук")   

class Dog(Animal):
    def make_sound(self):
        print(f"{self.get_name()} говорит: Гав-гав!")  

class Cat(Animal):
    def make_sound(self):
        print(f"{self.get_name()} говорит:  Мяу!")  

dog = Dog("Ричард", 3)   
cat = Cat("Муся", 2)      

dog.make_sound()
cat.make_sound()

dog.set_name("Бобик")
dog.set_age(5)
cat.set_name("Снежинка")
cat.set_age(3)

print(f"\nНовые данные: {dog.get_name()} ({dog.get_age()} лет), {cat.get_name()} ({cat.get_age()} года)")



