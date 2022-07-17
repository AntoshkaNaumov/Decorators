# 1. Написать декоратор - логгер. Он записывает в файл дату
# и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.
from functools import wraps
import os
import datetime


def logger_decorator(func, filename='log.txt', path='logs'):
    """Функция декоратор - логгер"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        today = datetime.datetime.today()
        date_time = today.strftime("%Y-%m-%d-%H.%M.%S")
        result = func(*args, **kwargs)
        func_name = func.__name__
        input_data = f'входные аргументы: {args}'
        result_line = f'вызвана функция {func_name} \n' \
                      f'дата и время вызова: {date_time} \n' \
                      f'{input_data} \n' \
                      f'возвращаемое значение функции {func_name}: {result}\n' \
                      f'-------------------------------\n'
        try:
            os.mkdir(path)
        except OSError:
            file_path = os.path.join(path, filename)
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(result_line)

        return result

    return wrapper


@logger_decorator
def recursive_flatten(arr):

    for i in arr:
        if isinstance(i, list):
            yield from recursive_flatten(i)
        else:
            yield i


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None], ]
    res = recursive_flatten(nested_list)
    print(res)
