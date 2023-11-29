import sqlite3

with sqlite3.connect("database.bd") as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id_admin INTEGER PRIMARY KEY,
            login VARCHAR(15) UNIQUE NOT NULL,
            password VARCHAR(15) NOT NULL,
            email VARCHAR(30) UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instructors(
            id_instructor INTEGER PRIMARY KEY,
            surname VARCHAR(30) NOT NULL,
            first_name VARCHAR(30) NOT NULL,
            middle_name VARCHAR(30),
            salary FLOAT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS season_tickets(
            id_season_ticket INTEGER PRIMARY KEY,
            name_season_tickets VARCHAR(15) UNIQUE NOT NULL,
            cost FLOAT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_user INTEGER PRIMARY KEY,
            login VARCHAR(15) UNIQUE NOT NULL,
            password VARCHAR(15) NOT NULL,
            surname VARCHAR(30) NOT NULL,
            first_name VARCHAR(30) NOT NULL,
            middle_name VARCHAR(30),
            email VARCHAR(30) UNIQUE NOT NULL,
            season_ticket_id INTEGER,
            instructor_id INTEGER,
            FOREIGN KEY (season_ticket_id) REFERENCES season_tickets (id_season_ticket),
            FOREIGN KEY (instructor_id) REFERENCES instructors (id_instructor)
        )
    ''')


