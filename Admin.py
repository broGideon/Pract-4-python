import CRUD
import Modyl

def update_user():
    data = CRUD.selectData("users")
    for item in data:
        print(f"ID: {item[0]}, login: {item[1]}, password: {item[2]}, surname: {item[3]}, first_name: {item[4]}, middle_name: {item[5]}, email: {item[6]}, season_ticket_id: {item[7]}, instructor_id: {item[8]}")
    punkt = input('Введите параметр для изменения: ')
    try:
        id = int(input('Введите ID: '))
        new = input('Введите новое значение: ')
        data = {punkt: new}
        filter = {'id_user': id}
        CRUD.updateData('users', data, filter)
    except:
        print("Что-то пошло нетак")
def update_instructor():
    data = CRUD.selectData("instructors")
    for item in data:
        print(f"ID: {item[0]}, surname: {item[1]}, first_name: {item[2]}, middle_name: {item[3]}, salary: {item[4]}")
    punkt = input('Введите параметр для изменения: ')
    try:
        id = int(input('Введите ID: '))
        new = input('Введите новое значение: ')
        data = {punkt: new}
        filter = {'id_instructor': id}
        CRUD.updateData('instructors', data, filter)
    except:
        print("Что-то пошло нетак")
def update_season_ticket():
    data = CRUD.selectData("season_tickets")
    for item in data:
        print(f"ID: {item[0]}, name_season_tickets: {item[1]}, cost: {item[2]}")
    punkt = input('Введите параметр для изменения: ')
    try:
        id = int(input('Введите ID: '))
        new = input('Введите новое значение: ')
        data = {punkt: new}
        filter = {'id_season_ticket': id}
        CRUD.updateData('season_tickets', data, filter)
    except:
        print("Что-то пошло нетак")

def create_instructor():
    try:
        surname = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        middle_name = input('Введите отчество (необязательно): ')
        cost = float(input('Введите зарплату: '))
        instructor = Modyl.Instructor(surname, first_name, middle_name, cost)
        data = instructor.create_data
        CRUD.insertData("instructors", data)
        return
    except:
        print('Введите корректные значения')
        return

def create_season_ticket():
    try:
        name = input('Введите название: ')
        cost = float(input('Введите цену: '))
        season_ticket = Modyl.Season_ticket(name, cost)
        data = season_ticket.create_data
        CRUD.insertData("season_tickets", data)
        return
    except:
        print('Введите корректные значения')

def read(table: str):
    data = CRUD.selectData(table=table)
    for item in data:
        print(item)
    return

def use_admin(login: str = None, password: str = None):
    if login == None and password == None:
        login = input('Логин: ')
        password = input('Пароль: ')
    columns = ['login', 'password']
    filter = {'login': login}
    data = CRUD.selectData("admins", column=columns, filter=filter)
    if password != data[1]:
        print('Неверный логин или пароль')
        return
    print('Успешный вход')

    menu = 0
    while menu != 9:
        print('1. Добавить инструктора')
        print('2. Добавить абонемент')
        print('3. Вывести список инструкторов')
        print('4. Вывести список абонементов')
        print('5. Вывести список пользователей')
        print('6. Изменить данные пользователя')
        print('7. Изменить данные инструктора')
        print('8. Изменить данные абонемента')
        print('9. Выход')
        try:
            menu = int(input('Выберите действие: '))
            if menu == 1:
                create_instructor()
            elif menu == 2:
                create_season_ticket()
            elif menu == 3:
                read("instructors")
            elif menu == 4:
                read("season_tickets")
            elif menu == 5:
                read("users")
            elif menu == 6:
                update_user()
            elif menu == 7:
                update_instructor()
            elif menu == 8:
                update_season_ticket()
            elif menu == 9:
                return
        except:
            print('Введите корректное значение')