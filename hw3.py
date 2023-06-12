# ДЗ

# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#  + сумма площин двох екземплярів ксласу
#  - різниця площин двох екземплярів ксласу
#  == площин на рівність
#  != площин на не рівність
#  >, < меньше більше
#  при виклику метода len() підраховувати сумму сторін

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.x * self.y
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __sub__(self, other):
#         return self.area() - other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __ne__(self, other):
#         return self.area() != other.area()
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __gt__(self, other):
#         return self.area() > other.area()
#
#     def __len__(self):
#         return 2 * (self.x + self.y)
#
#
# rect1 = Rectangle(2, 6)
# rect2 = Rectangle(3, 6)
#
# print(rect1 + rect2)
# print(rect1 - rect2)
# print(rect1 == rect2)
# print(rect1 != rect2)
# print(rect1 < rect2)
# print(rect1 > rect2)
# print(len(rect1))
# print(len(rect2))

###############################################################################

# створити класс Human (name, age) створити два класси Prince и Cinderella які наслідуються від Human: у попелюшки
# мае бути ім'я, вік, розмір нонги у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий
# буде приймати список попелюшок, та шукати ту саму в класі попелюшки має бути count який буде зберігати кількість
# створених екземплярів классу також має бути метод классу який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, leg_size):
#         super().__init__(name, age)
#         self.leg_size = leg_size
#         Cinderella.__count += 1
#
#     @classmethod
#     def amount_of_cinderellas(cls):
#         print(cls.__count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, founded_shoe):
#         super().__init__(name, age)
#         self.founded_shoe = founded_shoe
#
#     def my_princes(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if self.founded_shoe == cinderella.leg_size:
#                 print(f"The {self.name}'s princes is {cinderella.name}")
#                 return
#             else:
#                 print(f"The {cinderella.name} isn't {self.name}'s princes")
#         print(f"The {self.name}'s princes wasn't there")
#
#
# cinderellas = [Cinderella('Ann', 20, 38), Cinderella('Liz', 18, 36), Cinderella('Elsa', 21, 37)]
#
# Cinderella.amount_of_cinderellas()
#
# prince = Prince('Brendon', 20, 35)
#
# prince.my_princes(cinderellas)

###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде: - змінна класу printable_list яка буде зберігати книжки та журнали - метод add за
# допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або
# Magazine инакше ігрнорувати додавання - метод show_all_magazines який буде виводити всі журнали викликаючи
# метод print абстрактного классу - метод show_all_books який буде виводити всі книги викликаючи метод print
# абстрактного классу

# Приклад:
# Main.add(Magazine('Magazine1'))
#    Main.add(Book('Book1'))
#    Main.add(Magazine('Magazine3'))
#    Main.add(Magazine('Magazine2'))
#    Main.add(Book('Book2'))

#    Main.show_all_magazines()
#    print('-' * 40)
#    Main.show_all_books()


# для перевірки ксассів використовуємо метод isinstance, приклад:
# user = User('Max', 15)
# shape = Shape()

# isinstance(max, User) -> True
# isinstance(shape, User) -> False

# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def print(self):
#         pass
#
#
# class Book(Printable):
#     def print(self):
#         print(f'This is a book - {self.name}')
#
#
# class Magazine(Printable):
#     def print(self):
#         print(f'This is a magazine - {self.name}')
#
#
# class Main:
#     __printable_list: list[Printable] = []
#
#     @classmethod
#     def add(cls, item: Printable):
#         if isinstance(item, (Book, Magazine)):
#             cls.__printable_list.append(item)
#         else:
#             print(f"The {item.name} wasn't a book or magazine")
#
#     @classmethod
#     def show_all_books(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Book):
#                 item.print()
#
#     @classmethod
#     def show_all_magazines(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Magazine):
#                 item.print()
#
#
# Main.add(Book('Math'))
# Main.add(Book('Geography'))
# Main.add(Magazine('Smile'))
# Main.add(Book('History'))
# Main.add(Magazine('Angel'))
# Main.add(Magazine('Kangaroo'))
# Main.add(Book('English'))
# Main.add(Magazine('Emoticon'))
#
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
