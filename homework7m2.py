import sqlite3
from sqlite3 import Connection, Cursor
from typing import List, Tuple

DB_FILENAME = "books.db" 

def get_connection(db_filename: str = DB_FILENAME) -> Connection:
    """Создаёт и возвращает соединение с SQLite базой данных."""
    conn = sqlite3.connect(db_filename)
    return conn

def create_table(conn: Connection) -> None:
    """Создаёт таблицу books, если она ещё не существует."""
    sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    );
    """
    cur: Cursor = conn.cursor()
    cur.execute(sql)
    conn.commit()

def insert_books(conn: Connection, books: List[Tuple]) -> None:
    """
    Вставляет список книг в таблицу books.
    books — список кортежей в формате:
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    """
    sql = """
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cur: Cursor = conn.cursor()
    cur.executemany(sql, books)
    conn.commit()

def sample_books() -> List[Tuple]:
    """Возвращает минимум 10 примеров книг."""
    return [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 3),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 4),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика/Роман", 448, 5),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 2),
        ("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", 223, 6),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 4),
        ("Убить пересмешника", "Харпер Ли", 1960, "Роман", 281, 3),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 320, 2),
        ("Сто лет одиночества", "Габриэль Гарсия Маркес", 1967, "Магический реализм", 417, 3),
        ("Принц", "Макиавелли", 1532, "Политическая философия", 140, 1),
    ]

def table_count(conn: Connection) -> int:
    """Возвращает количество записей в таблице books (для проверки)."""
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM books;")
    (count,) = cur.fetchone()
    return count

if __name__ == "__main__":
    conn = get_connection()
    try:
        create_table(conn)

        if table_count(conn) == 0:
            insert_books(conn, sample_books())
            print("Таблица создана и добавлено 10 записей.")
        else:
            print("Таблица уже содержит записи — вставка пропущена.")

        cur = conn.cursor()
        cur.execute("SELECT id, name, author, publication_year FROM books LIMIT 3;")
        rows = cur.fetchall()
        print("Примеры записей (первые 3):")
        for r in rows:
            print(r)

    finally:
        conn.close()
