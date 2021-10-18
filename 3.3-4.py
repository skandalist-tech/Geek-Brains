dict = {}
def thesaurus_adv(*name_surname):
    for name_sur in name_surname:
        name, sur = name_sur.split()
        dict.setdefault(sur[0], {})
        dict[sur[0]].setdefault(name[0], [])
        dict[sur[0]][name[0]].append(name_sur)
    return dict



print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                   "Анна Савельева"))