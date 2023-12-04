import CRUD

def update_user(column: str, login: str, new_value: str):
    data = {column: new_value}
    filter = {"login": login}
    CRUD.updateData("users", data, filter)
    return

def vibor(table: str, column: str, login: str):
    data = CRUD.selectData(table)
    for i in data:
        print(i)
    try:
        menu = int(input('Выберите новое значение: '))
        data = {column: menu}
        filter = {"login": login}
        CRUD.updateData("users", data, filter)
        return
    except:
        print('Такого нет')
        return

def use_user(login: str = None, password: str = None):
    if login == None and password == None:
        login = input('Логин: ')
        password = input('Пароль: ')
    columns = ['login', 'password']
    filter = {'login': login}
    data = CRUD.selectData("users", column=columns, filter=filter)
    if password != data[1]:
        print('Неверный логин или пароль')
        return
    print('Успешный вход')

    menu = 0
    while menu != 9:
        print('1. Выбрать абонемент ')
        print('2. Выбрать инструктора ')
        print('3. Поменять email ')
        print('4. Помять фамилию:')
        print('5. Помять имя ')
        print('6. Помять отчество ')
        print('7. Помять пароль ')
        print('8. Посмотреть профиль ')
        print('9. Выход ')
        try:
            menu = int(input('Выберите действие: '))
            if menu == 1:
                vibor("season_tickets", "season_ticket_id", login)
            elif menu == 2:
                vibor("instructors", "instructor_id", login)
            elif menu == 3:
                update_user("email", login, input('Введите новое значение: '))
            elif menu == 4:
                update_user("surname", login, input('Введите новое значение: '))
            elif menu == 5:
                update_user("first_name", login, input('Введите новое значение: '))
            elif menu == 6:
                update_user("middle_name", login, input('Введите новое значение: '))
            elif menu == 7:
                update_user("password", login, input('Введите новое значение: '))
            elif menu == 8:
                CRUD.inner_join_user(login)
            elif menu == 9:
                break
        except:
            print('Введите корректное значение')
    return
