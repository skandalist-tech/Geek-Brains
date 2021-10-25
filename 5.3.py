tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

import itertools

tut_klas = ((tut, klass) for tut, klass in itertools.zip_longest(tutors, klasses))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
print(next(tut_klas))
