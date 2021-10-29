from itertools import zip_longest
user_hobby = {}
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('hobby.csv', encoding='utf-8') as h:
        line_h = 0
        for line in h:
            line_h += 1
            print(line_h)
        with open('users.csv', encoding='utf-8') as u:
            line_u = 0
            for line in u:
                line_u += 1
                print(line_u)
            if line_u < line_u:
                exit(1)
            u.seek(0)
            h.seek(0)
            for line_user, line_user_hobby in zip_longest(u, h):
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')