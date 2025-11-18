from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date  
        self.__occupation = occupation 
        self.__higher_education = higher_education 

    # Геттеры 
    def get_birth_date(self):
        return self.__birth_date

    def get_occupation(self):
        return self.__occupation

    def has_higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.__higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. {edu_text}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.has_higher_education() else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия {self.get_occupation()}. "
              f"Я учился в группе {self.group_name}. {edu_text}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.has_higher_education() else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия {self.get_occupation()}. "
              f"Мое хобби {self.hobby}. {edu_text}")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()

print("\nВозраст Айбека:", fr1.age)
print("Возраст Ивана:", cl1.age)

    def __str__(self):
        return f"{self.get_value()} {self.get_unit()}"
