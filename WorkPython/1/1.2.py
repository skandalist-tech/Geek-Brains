# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
indx = 1
cube_numbers = []
summa = 0
while indx < 1000:
    cube = indx**3
    cube_numbers.append(cube)
    indx += 2
print(cube_numbers)
for indx_array, number in enumerate(cube_numbers):
    var = 0
    while number:
        var += number % 10
        number //= 10
    if var % 7 == 0:
        summa += cube_numbers[indx_array]
    cube_numbers[indx_array] += 17
print(summa)
summa = 0
for indx_array, number in enumerate(cube_numbers):
    var = 0
    while number :
        var += number % 10
        number //= 10
    if var % 7 == 0:
        summa += cube_numbers[indx_array]
print(summa)
