class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "имеет высшее образование" if self.higher_education else "не имеет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился(ась) {self.birth_date}. "
              f"Моя профессия — {self.occupation}, и я {education_status}.")

person1 = Person("Бекзат Акылбеков", "12.04.1998", "инженер", True)
person2 = Person("Сезим Саматова", "25.09.2001", "дизайнер", False)
person3 = Person("Алия Аманова", "10.10.1990", "айтишник", True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

print()  



person1.introduce()
person2.introduce()
person3.introduce()
