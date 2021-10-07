procent = int(input('Введите число'))
for procent in range(procent):
    if procent % 10 == 1 and procent % 100 != 11:
        print (procent, " проценТ")
    elif 1 < procent % 10 < 5 and not 11 < procent % 100 < 15:
        print(procent, " процентА")
    else:
        print(procent, " процентОВ")