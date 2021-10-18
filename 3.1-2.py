numbers = {'one': "Один", 'two': "Два", 'three': "три", 'four': "четыре", 'five': "пять", 'six': "шесть",\
           'seven': "семь", 'eight': "восемь", 'nine': "девять", 'zero': "ноль"}
def num_translate_adv(num):
    if num.islower():
        print(numbers.get(num.lower(), []).lower())
    elif num.istitle():
        print(numbers.get(num.lower(), []).title())

num_translate_adv('four')
num_translate_adv('Four')


