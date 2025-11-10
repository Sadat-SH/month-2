# GIT -это -->
# --> Система контроля версий
# --> Это система, которая позволяет вести учет изменений в проекте, для работы с GIT нужно использовать терминал.

# Основные понятия:
#  --репозиторий - "проект" в понимании GIT 
#  --коммит - сохранение изменений(как checkpoint)
#  --удаленный репозиторий - удаленная копия проекта(на удаленном сервере, например на GITHUB)
#  --отслеживание(tracking) - git следит за изменениями в файлах(создание файлов, удаление, переименование, изменение содержимого)
#  --untracked files - (еще) не отслеживаемые git`ом файлы
#  --файл .gitignore - список игнорируемых файлов и директорий.


# Основные команды
#. - один раз на компьютере для всех проектов
#. -->  git config --global user.name "Your Name" - установить имя пользователя(для всех проектов, автор проектов)
#. --> git config --global user.email "Your email" - установить электронную почту пользователя(для всех проектовб, email автора проектов)

#. - каждый раз при создании нового проекта, один раз в проекте 
#  --> git init - создать репозиторий
#  --> git remote add origin https://github.com/username/repo.git ---добавить удаленный репозиторий(на сайте github)

# в репозитории в любой момент
#    --> git status -проверить состояние репозитория, какие файлы были изменены, какие файлы еще не отслеживаются 
#.   --> git add -добавить все изменения(со всех файлов)
#.   --> git add lesson1.py lesson2.py lesson3.py -добавить изменения в конкретный файл
#.   --> git commit -m "commit message" -создать коммит, сохранить изменения(со всех файлов), сделать checkpoint
#.       -m -(message): сообщение(описание) коммита
#.   --> git push -отправить изменения в удаленный репозиторий(сайт -github)


# Порядок выполнения действий и команд в проекте:
#    git init  -> инициализация репозитория 
#.   создание и заполнение  .gitignore .Если этот шаг пропустить или выполнить позже, лишние файлы будут добавлены в репозиторий.
#    git add . -> добавление изменений(любых)
#.   git commit -m "commit message" -сохранение изменений, коммит 
#.   git push -> отправка изменений на github.




# getter
# setter



# родитель, суперкласс
class Car:
    # инициализатор объектов
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")

    def test(self):
        self.drive("Karakol")

# дочерний, подкласс, потомок
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def drive(self, location):
        # super().drive(location)
        print(f"Bus {self.model} is driving in {location}")

    def test_bus(self):
        print(f"Bus test {self.model}")


class Truck(Car):
    pass

car_honda = Car("white", "Honda")
bus_1 = Bus("green", "Isuzu", 40)
print(bus_1.seats)
print(bus_1.color)
bus_1.drive("Bishkek")
# bus_1.test_bus()
truck_man = Truck("red", "Man") 