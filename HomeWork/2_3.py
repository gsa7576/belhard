# Заполнить список степенями числа 2 (от 2^1 до 2^n).

# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры.

print("Введите число n")
n = int(input())
slovar1 = dict()
slovar2 = dict()
for i in range(0, n+1):
    slovar1[i] = slovar2['name'] = 'email'+str(i)
print(slovar1)

# Введите число n
# 5
# {0: 'email0', 1: 'email1', 2: 'email2', 3: 'email3', 4: 'email4', 5: 'email5'}
#
# Process finished with exit code 0