# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва
# записувати не потрібно)
#
# try:
#     with open('files/emails.txt', 'r') as file:
#         emails: list[str] = []
#
#         while file.readline():
#             line = file.readline().split()
#             if line[1].endswith('@gmail.com'):
#                 emails.append(line[1] + '\n')
# except Exception as err:
#     print(err)
#
# try:
#     with open('files/gmails.txt', 'w') as file:
#         file.writelines(emails)
# except Exception as err:
#     print(err)

#####################################################################################

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
# * вивід всіх покупок
# * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

# import json
#
#
# class Purchase:
#     def __init__(self, purchase_id: int, name: str, price: int):
#         self.price = price
#         self.name = name
#         self.id = purchase_id
#
#
# def save_to_notebook(list_of_purchases):
#     try:
#         with open('files/purchase_notebook.json', 'w') as file:
#             json.dump(list_of_purchases, file)
#     except Exception as err:
#         print(err)
#     return list_of_purchases
#
#
# def read_notebook(lists_of_purchases):
#     try:
#         with open('files/purchase_notebook.json', 'r') as file:
#             lists_of_purchases = json.load(file)
#     except Exception as err:
#         print(err)
#     return lists_of_purchases
#
#
# def add_purchase(purchase, list_of_purchases):
#     if isinstance(purchase, Purchase):
#         list_of_purchases.append(purchase.__dict__)
#     else:
#         print(f"We can't add the not purchase item to the purchase list")
#     return list_of_purchases
#
#
# def print_all_list(list_of_purchases):
#     print(f'{list_of_purchases}')
#
#
# def search_purchase(field_where_search, entered_value, list_of_purchases):
#     index_of_searched_purchase = int
#
#     for index, purchase in enumerate(list_of_purchases):
#         if purchase[field_where_search] == entered_value:
#             index_of_searched_purchase = index
#         elif purchase[field_where_search] != entered_value:
#             print(f'In your purchase notebook is not such purchase')
#     return index_of_searched_purchase
#
#
# def delete_purchase(id_to_delete, list_of_purchases):
#     index_of_purchase_to_delete = search_purchase('id', id_to_delete, list_of_purchases)
#     list_of_purchases.pop(index_of_purchase_to_delete)
#     return list_of_purchases
#
#
# def search_the_most_expensive_purchase(list_of_purchases):
#     purchases = [purchase['price'] for purchase in list_of_purchases if purchase['price']]
#     the_most_expensive_purchase_id = search_purchase('price', max(purchases), list_of_purchases)
#     print(f'The most expensive purchase in your notebook is: {list_of_purchases[the_most_expensive_purchase_id]}')
#     return the_most_expensive_purchase_id
#
#
# purchase_list: list[dict] = []
#
# while True:
#     print('Choose anything you want:\n'
#           '1. Add purchase\n'
#           '2. Print a list of all purchases\n'
#           '3. Find by (id, name, price)\n'
#           '4. The most expensive purchase\n'
#           '5. Delete purchase by id\n')
#
#     choice = input('Enter your choice: ')
#
#     match choice:
#         case '1':
#             choice_shop = 'y'
#             while choice_shop == 'y':
#
#                 purchase_name = input('Enter the purchase name : ')
#                 purchase_price = int(input('Enter the purchase price : '))
#
#                 if len(purchase_list) == 0:
#                     purchase_id = 1
#                 else:
#                     purchase_id = purchase_list[-1]['id'] + 1
#
#                 purchase = Purchase(purchase_id, purchase_name, purchase_price)
#                 add_purchase(purchase, purchase_list)
#                 choice_shop = input('Do you want to add one more purchase ? (y/n) : ')
#                 if choice_shop == 'n':
#                     save_to_notebook(purchase_list)
#                     read_notebook(purchase_list)
#
#         case '2':
#             print_all_list(purchase_list)
#
#         case '3':
#
#             print('Enter the field by which you want search : \n'
#                   '1 - Id \n'
#                   '2 - Name\n'
#                   '3 - Price')
#
#             user_choice = input('Enter your choice : ')
#
#             if user_choice == '1':
#                 field = int(input('Enter the purchase id: '))
#                 print(purchase_list[search_purchase('id', field, purchase_list)])
#
#             elif user_choice == '2':
#                 field = input('Enter the purchase name: ')
#                 print(purchase_list[search_purchase('name', field, purchase_list)])
#
#             elif user_choice == '3':
#                 field = int(input('Enter the purchase price: '))
#                 print(purchase_list[search_purchase('price', field, purchase_list)])
#
#             else:
#                 print('You entered something wrong, so we redirect you to main menu')
#
#         case '4':
#             search_the_most_expensive_purchase(purchase_list)
#
#         case '5':
#             id_to_delete = int(input('Enter the id of purchase you want to delete : '))
#             delete_purchase(id_to_delete, purchase_list)
#
#         case _:
#             break

########################################################################################

# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку
# то брати наступне з того ж підсписку

# в результат має записатись тільки 5 id

# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

def unique_elements(given_data: list[list[dict]]):
    res: list[int] = []
    for i in given_data:
        for m, j in enumerate(i):
            res.append(j['id'])
            for k in res:
                if k == j['id']:
                    m += 1
    print(res)
    return res


unique_elements(data)
