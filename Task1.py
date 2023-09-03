"""
Задача №5
📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для
    проверки наличия пользователя в множестве используйте
    магический метод проверки на равенство пользователей.
    Если такого пользователя нет, вызывайте исключение
    доступа. А если пользователь есть, получите его уровень из
    множества пользователей.
📌 добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""

"""
Задача №6
📌 Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
📌 Передавайте необходимые данные из основного кода проекта.
"""

# Решение взято ваше. Разбор посмотрел.


import json

class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def to_dict(self):
        return {"name": self.name, "id": self.id, "access_level": self.access_level}

    def __str__(self):
        return f"User(name={self.name}, id={self.id}, access_level={self.access_level})"

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

class CustomException(Exception):
    pass

class LevelError(CustomException):
    def __init__(self, message="Ошибка уровня доступа"):
        super().__init__(message)

    def __str__(self):
        return f"Ошибка уровня доступа: {self.message}"

class AccessError(CustomException):
    def __init__(self, message="Ошибка доступа"):
        super().__init__(message)

    def __str__(self):
        return f"Ошибка доступа: {self.message}"

class Project:
    def __init__(self, owner_level):
        self.owner_level = owner_level
        self.users = set()

    def load_users_from_json(self):
        try:
            with open("users.json", "r") as file:
                user_data = json.load(file)
                for user_info in user_data:
                    user = User(user_info["name"], user_info["id"], user_info["access_level"])
                    self.users.add(user)
        except FileNotFoundError:
            pass

    def login(self, name, id):
        user = User(name, id, 0)
        if user in self.users:
            user = next(u for u in self.users if u == user)
            if user.access_level < self.owner_level:
                raise AccessError(f"Доступ к проекту запрещен. Ваш уровень доступа: {user.access_level}")
            return user.access_level
        else:
            raise AccessError(f"Пользователь {name} с ID {id} не найден.")

    def add_user(self, user):
        if user.access_level < self.owner_level:
            raise LevelError("Недостаточный уровень доступа для добавления пользователя.")
        self.users.add(user)
        print(f"Пользователь {user.name} добавлен.")

project = Project(owner_level=5)
project.load_users_from_json()

try:
    while True:
        name = input("Введите имя пользователя (или 'exit' для завершения): ")
        if name == 'exit':
            break
        id = input("Введите личный идентификатор: ")
        access_level = int(input("Введите уровень доступа (от 1 до 7): "))
        user = User(name, id, access_level)
        project.add_user(user)
except LevelError as le:
    print(le)
except AccessError as ae:
    print(ae)