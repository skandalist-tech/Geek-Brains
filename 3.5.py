
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num, repeat = True):
    """Очень плохое чуство юмора"""
    joke_list = []
    if repeat == True:
        for i in range(num):
            joke_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        return joke_list
    elif repeat != True:
        for i in range(num):
            joke_list.append(f'{nouns.pop(random.randrange(0, len(nouns)))}'
                             f' {adverbs.pop(random.randrange(0, len(adverbs)))}'
                             f' {adjectives.pop(random.randrange(0, len(adjectives)))}')
        return joke_list

print(get_jokes(1, True))
print(get_jokes(5, False))
