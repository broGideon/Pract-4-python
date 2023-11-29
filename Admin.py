import CRUD
import Modyl

def update():
    pass

def create_instructor():
    try:
        surname = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        middle_name = input('Введите отчество (необязательно: )')
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
    while menu != 10:
        print('1. Добавить инструктора')
        print('2. Добавить абонемент')
        print('3. Вывести список инструкторов')
        print('4. Вывести список абонементов')
        print('5. Вывести список пользователей')
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
        except:
            print('Введите корректное значение')