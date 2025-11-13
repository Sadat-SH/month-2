from datetime import datetime as dt
from time import sleep
import asyncio

# === Основной декоратор ===
def checktime(func):
    def wrapper():
        time_now = dt.now()
        print(f"Функция была вызвана в {time_now.hour:02}:{time_now.minute:02}:{time_now.second:02} "
              f"{time_now.day:02}/{time_now.month:02}/{time_now.year}")
        func()
    return wrapper


@checktime
def hello_world():
    print("hello world")


# === Доп. задание 1: До и после ===
def checktime_before_after(func):
    def wrapper():
        start = dt.now()
        print(f"Функция была вызвана в {start.hour:02}:{start.minute:02}:{start.second:02} "
              f"{start.day:02}/{start.month:02}/{start.year}")
        func()
        end = dt.now()
        print(f"Функция была закончена в {end.hour:02}:{end.minute:02}:{end.second:02} "
              f"{end.day:02}/{end.month:02}/{end.year}")
    return wrapper


@checktime_before_after
def slow_function():
    print("Выполняется функция...")
    sleep(1)
    print("Функция завершена!")


# === Доп. задание 2: Для корутин ===
def async_check_time(func):
    async def wrapper():
        start = dt.now()
        print(f"Функция была вызвана в {start}")
        await func()
        end = dt.now()
        print(f"Вызов закончился в {end}")
    return wrapper


@async_check_time
async def my_coroutine():
    print("Hello from coroutine")
    await asyncio.sleep(3)
    print("Coroutine done!")


# === Примеры вызова ===
if __name__ == "__main__":
    # Основное задание
    hello_world()

    print("\n--- Доп. задание 1 ---")
    slow_function()

    print("\n--- Доп. задание 2 ---")
    asyncio.run(my_coroutine())
