from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, email: str, login: str, password: str):
        self.email = email
        self.login = login
        self.password = password
    @abstractmethod
    def create_data(self):
        pass

class User(Human):
    def __init__(self, email: str, login: str, password: str, surname: str, first_name: str, middle_name: str = None):
        super().__init__(email, login, password)
        self._surname = surname
        self._first_name = first_name
        self._middle_name = middle_name
    @property
    def create_data(self):
        return {"email": self.email, "login": self.login, "password": self.password, "surname": self._surname, "first_name": self._first_name, "middle_name": self._middle_name}

class Admin(Human):
    def __init__(self, email: str, login: str, password: str):
        super().__init__(email, login, password)
    def create_data(self):
        return {"email": self.email, "login": self.login, "password": self.password}

class Season_ticket:
    def __init__(self, name_season_tickets: str, cost: float):
        self._name_season_tickets = name_season_tickets
        self._cost = cost
    @property
    def create_data(self):
        return {"name_season_tickets": self._name_season_tickets, "cost": self._cost}

class Instructor:
    def __init__(self, surname: str, first_name: str, middle_name: str, salary: float):
        self._surname = surname
        self._first_name = first_name
        self._middle_name = middle_name
        self._salary = salary
    @property
    def create_data(self):
        return {"surname": self._surname, "first_name": self._first_name, "middle_name": self._middle_name, "salary": self._salary}