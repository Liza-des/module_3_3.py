# Задача 1 (для тренировки)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()


def print_params(*args):
    print(*args)


print_params(541, 'cам раб', 56, 64, 85, 5, 5, 5, 8)


def print_params(a, b, c):
    print(a, b, c)


b = 25
c = [1, 2, 3]
print_params(1, b, c)


# Задача 2
def print_params(a, b, c):
    print(a, b, c)

values_list = [1, 'курс', True]
values_dict = {'a': 2, 'b': "строка", 'c': True}
print_params(*values_list)
print_params(**values_dict)


# Задача 3
def print_params(a, b, c):
    print(a, b, c)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)