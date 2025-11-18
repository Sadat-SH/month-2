from homework_5.distance import Distance

if name == "__main__":
    a = Distance(10, "m")
    b = Distance(2, "km")
    c = Distance(500, "cm")
    d = Distance(39.3701, "inch")

    print("a:", a)
    print("b:", b)
    print("c:", c)

    print("\nСложение:")
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
    print("d == Distance(1, 'm') ->", d == Distance(1, "m"))