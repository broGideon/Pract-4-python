import sqlite3

def executeQuerry(query, values = None):
    try:
        with sqlite3.connect("database.bd") as conn:
            cursor = conn.cursor()
            if values: cursor.execute(query, values)
            else: cursor.execute(query)
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
        return

def insertData(table, data):
    columns = ", ".join(data.keys())
    placeholders = ", ".join("?" for _ in data)
    querry = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    executeQuerry(querry, list(data.values()))
    return

def updateData(table, data, filter):
    columns = ", ".join(f"{column} = ?" for column in data.keys())
    for item in filter.values():
        value = item
    for item in filter.keys():
        key = item
    querry = f"UPDATE {table} SET {columns} WHERE {key} = {value}"
    data_list = []
    for i in data.values():
        data_list.append(i)
    executeQuerry(querry, data_list)
    return

def deleteData(table, data):
    for item in data.keys():
        key = item
    for item in data.values():
        value = item
    querry = f"DELETE FROM {table} WHERE {key} = {value}"
    executeQuerry(querry)
    return

def selectData(table, column = None, filter = None):
    try:
        with sqlite3.connect("database.bd") as conn:
            cursor = conn.cursor()
            if column != None and filter != None:
                columns = ', '.join(i for i in column)
                for item in filter.keys():
                    key = item
                for item in filter.values():
                    value = item
                querry = f"SELECT {columns} FROM {table} WHERE {key} = '{value}'"
                return cursor.execute(querry).fetchone()
            elif column != None:
                columns = ', '.join(i for i in column)
                querry = f"SELECT {columns} FROM {table}"
            elif filter != None:
                for item in filter.keys():
                    key = item
                for item in filter.values():
                    value = item
                querry = f"SELECT * FROM {table} WHERE {key} = {value}"
            else: querry = f"SELECT * FROM {table}"
            return cursor.execute(querry).fetchall()
    except sqlite3.Error as e:
        print(e)
        return

def inner_join_user(login):
    columns_user = ['surname', 'first_name', 'middle_name', 'email', 'season_ticket_id', 'instructor_id']
    filter_user = {'login': login}
    user_data = selectData("users", columns_user, filter_user)
    filter_instructor = {'id_instructor': user_data[5]}
    columns_instructor = ['surname', 'first_name', 'middle_name']
    instructor_data = selectData('instructors',column=columns_instructor, filter=filter_instructor)
    filter_season_tickets = {'id_season_ticket': user_data[4]}
    columns_season_tickets = ['name_season_tickets', 'cost']
    season_ticket_data = selectData('season_tickets', column=columns_season_tickets, filter=filter_season_tickets)
    columns_user = ['surname', 'first_name', 'middle_name', 'email']
    user_data = ', '.join(selectData("users", columns_user, filter_user))
    print(f"Пользователь: {user_data}")
    print(f"Инструктор: {instructor_data}")
    print(f"Абонемент: {season_ticket_data}")
    return