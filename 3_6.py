# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

nums = [3, 5, 6, 1, 9, 12]
print(nums)
nums = list(filter(lambda x: (x%2 == 0) , nums))+list(filter(lambda x: (x%2 != 0) , nums))
print(nums)









#
# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
#
# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
#
# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

