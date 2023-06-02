# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
# 3) створити функцію котра буде повертати суму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2' expanded_form(42) # return '40 + 2' expanded_form(70304) # return '70000 + 300
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим
# декоратором, та буде виводити це значення після виконання функцій

from typing import Callable


def decor(func: Callable) -> Callable:
    counter: int = 0

    def inner(*args, **kwargs) -> None:
        nonlocal counter
        counter += 1
        print(counter)
        func(*args, **kwargs)
        print('-' * 20)

    return inner


@decor
def tasks() -> None:
    def todos() -> tuple[Callable[[], None], Callable[[], list[str]]]:
        todo_list: list[str] = []

        def add_todo() -> None:
            todo = input('Enter new todo: \n')
            todo_list.append(todo)

        def get_todos() -> list[str]:
            print(f'Your todos: {todo_list}')
            return todo_list

        return add_todo, get_todos

    list_of_todos = todos()
    get = list_of_todos[1]
    add = list_of_todos[0]
    add()
    get()
    add()
    get()


@decor
def sum_of_digits() -> str:
    number: str = input('Enter number: \n')
    result: str = '+'.join([figure + '0'*(len(number)-1-i) for i, figure in enumerate(number)])
    print(result)
    return result


tasks()
sum_of_digits()
sum_of_digits()
sum_of_digits()
tasks()
