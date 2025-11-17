# homework_5.py
from dataclasses import dataclass

@dataclass
class Distance:
    """
    Класс для работы с расстояниями.
    Атрибуты:
      - value: численное значение (int/float)
      - unit: строка единицы измерения ('cm', 'm', 'km', 'mm', 'inch' и т.д.)
    Поддерживает: __str__, __add__, __sub__, сравнения.
    """
    value: float
    unit: str

    conversion_to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "inch": 0.0254,
        "ft": 0.3048,  # фут
    }

    @staticmethod
    def _ensure_valid_unit(unit: str):
        if unit not in Distance.conversion_to_meters:
            raise ValueError(f"Неизвестная единица измерения: '{unit}'")

    def to_meters(self) -> float:
        """Конвертировать self в метры (float)."""
        Distance._ensure_valid_unit(self.unit)
        return float(self.value) * Distance.conversion_to_meters[self.unit]

    @classmethod
    def from_meters(cls, meters_value: float, unit: str):
        """Создать Distance из значения в метрах, вернув в указанной unit."""
        Distance._ensure_valid_unit(unit)
        factor = Distance.conversion_to_meters[unit]
        return cls(meters_value / factor, unit)

    def __str__(self):
        return f"{self.value} {self.unit}"

    def _binary_op_prepare(self, other):
        """Вспомогательная проверка и получение значений в метрах."""
        if not isinstance(other, Distance):
            raise TypeError("Операнды должны быть экземплярами Distance.")
        
        Distance._ensure_valid_unit(self.unit)
        Distance._ensure_valid_unit(other.unit)
        return self.to_meters(), other.to_meters()

    def __add__(self, other):
        meters_a, meters_b = self._binary_op_prepare(other)
        result_meters = meters_a + meters_b
    
        return Distance.from_meters(result_meters, self.unit)

    def __sub__(self, other):
        meters_a, meters_b = self._binary_op_prepare(other)
        result_meters = meters_a - meters_b
        if result_meters < 0:
            raise ValueError("Результат вычитания не может быть отрицательным.")
        return Distance.from_meters(result_meters, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return abs(self.to_meters() - other.to_meters()) < 1e-9

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() >= other.to_meters()


if __name__ == "__main__":
    a = Distance(10, "m")
    b = Distance(2, "km")
    c = Distance(500, "cm")  
    d = Distance(39.3701, "inch")  

    print("a:", a)  
    print("b:", b)  
    print("c:", c)  

    print("\nСложение (лево-единица сохраняется):")
    print("a + c =", a + c) 
    print("a + b =", a + b) 

    print("\nВычитание:")
    print("b - a =", b - a)  
    try:
        print("a - b =", a - b) 
    except ValueError as e:
        print("Ошибка при a - b:", e)

    print("\nСравнения:")
    print("a == Distance(1000, 'cm') ->", a == Distance(1000, "cm")) 
    print("a < b ->", a < b) 
    print("c <= Distance(5, 'm') ->", c <= Distance(5, "m"))  
    print("d ~ 1 m ->", d, "equals Distance(1, 'm')?", d == Distance(1, "m"))
