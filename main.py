import Modyl
import bd
import CRUD
import Admin
import User
import sqlite3
bd

def register_admin():
    email = input('Электронная почта: ')
    login = input('Логин: ')
    password = input('Пароль: ')
    admin = Modyl.Admin(email, login, password)
    data = admin.create_data()
    CRUD.insertData("admins", data)
    Admin.use_admin(login, password)
    return

def register_user():
    email = input('Электронная почта: ')
    login = input('Логин: ')
    password = input('Пароль: ')
    surname = input('Фамилия: ')
    first_name = input('Имя: ')
    middle_name = input('Отчество(необязательно): ')
    if middle_name == '': middle_name = None
    user = Modyl.User(email, login, password, surname, first_name, middle_name)
    data = user.create_data
    CRUD.insertData("users", data)
    User.use_user(login, password)
    return

menu = 0
while menu != 5:
    print('1. Вход в качестве администратора')
    print('2. Регистрация администратора')
    print('3. Вход в качестве пользователя')
    print('4. Регистрация пользователя')
    print('5. Выход')
    try:
        menu = int(input('Выберите один из пунктов: '))
        if menu == 1: Admin.use_admin()
        elif menu == 2: register_admin()
        elif menu == 3: User.use_user()
        elif menu == 4: register_user()
        elif menu == 5: break
        else: print('Такого в меню нет')
    except:
        print('Введите корректное значение')