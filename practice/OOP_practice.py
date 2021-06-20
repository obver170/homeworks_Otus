# Создать класс User со следующими атрибутами:
# имя, фамилия, почтовый адрес, мобильный номер, пароль, животные
# Создать геттер и сеттер для пароля.
# Создайте класс Pet и добавьте к нему следующие атрибуты:
# кличка, порода, год рождения, хозяин (User)
# Добавьте список из Pet как атрибут экземпляра для User.
# Создайте несколько экземпляров класса User, добавьте к юзерам 1-4 домашних животных

class User:

    def __init__(self, name='', surname='', index='', phone_number=''):
        self.name = name
        self.surname = surname
        self.index = index
        self.phone_number = phone_number
        self.__password = 'default'
        self.__pets = []

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def pets(self):
        return self.__pets

    @pets.setter
    def pets(self, pet):
        self.__pets.append(pet)



class Pet:

    def __init__(self, name='', breed='', yob='', master=''):
        self.name = name
        self.breed = breed
        self.year_of_birth =yob
        self.master = master


    def __repr__(self):
        return f'Имя - {self.name}, порода - {self.breed}, год рождения - {self.year_of_birth}, хозяин - {self.master}'


pet1 = Pet(name='pet1')
pet2 = Pet(name='pet2')
pet3 = Pet(name='pet3')
pet4 = Pet(name='pet4')

list_pets = [pet3, pet4]

user1 = User(name='user1')
user1.pets = pet1
user2 = User(name='user2')
user2.pets = pet2
user3 = User(name='user3')
user3.pets = list_pets

print(user1.pets)
print(user2.pets)
print(user3.pets)