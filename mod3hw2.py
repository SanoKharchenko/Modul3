
# Первое задание. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()

print_params(17, 'Book', False)

print_params(3, 'sea')

print_params(b = 25)

print_params(c = [1,2,3])

# Второе задание. Распаковка параметров:

values_list = ['cat', 9, False]
values_dict = {'a': 7, 'b': True, 'c': 'Dog'}

print_params(*values_list)

print_params(**values_dict)

# Третье задание. Распаковка + отдельные параметры:

values_list_2 = [ 3.1417 , 'Music']

print_params(*values_list_2, 42)