import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXIST students (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,              
        name TEXT NOT NULL,       
        age INTEGER,
        sity TEXT                     
    )
    """)

def add_student(conn, name, age, sity):    
    conn.execute("""
    INSERT INTO students (name, age, sity)
    VALUES (?, ?, ?')             
    """,
    
    (name, age, sity)
    )
    conn.commit()



if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_tables(conn)