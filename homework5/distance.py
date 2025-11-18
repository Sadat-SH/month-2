from dataclasses import dataclass

@dataclass
class Distance:
    value: float
    unit: str

    conversion_to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "inch": 0.0254,
        "ft": 0.3048,
    }

    @staticmethod
    def _ensure_valid_unit(unit: str):
        if unit not in Distance.conversion_to_meters:
            raise ValueError(f"Неизвестная единица измерения: '{unit}'")

    def to_meters(self) -> float:
        Distance._ensure_valid_unit(self.unit)
        return self.value * Distance.conversion_to_meters[self.unit]

    @classmethod
    def from_meters(cls, meters_value: float, unit: str):
        Distance._ensure_valid_unit(unit)
        factor = Distance.conversion_to_meters[unit]
        return cls(meters_value / factor, unit)

    # Строковое представление
    def __str__(self):
        return f"{self.value} {self.unit}"

    # Сложение
    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_meters = self.to_meters() + other.to_meters()
        return Distance.from_meters(result_meters, self.unit)

    # Вычитание
    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_meters = self.to_meters() - other.to_meters()
        if result_meters < 0:
            raise ValueError("Результат вычитания не может быть отрицательным.")
        return Distance.from_meters(result_meters, self.unit)

    # Сравнения
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